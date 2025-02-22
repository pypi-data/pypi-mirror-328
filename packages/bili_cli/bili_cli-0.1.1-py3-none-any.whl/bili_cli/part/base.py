#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import pickle
import json
import time
import random
import os
import shutil
import pydantic
from collections import defaultdict
from typing import Dict, List, Callable
from datetime import datetime
from pysrt.srtitem import SubRipItem
from wpy.path import walkfile,  read_dict
from bili_cli.tools.path import write_dict
from bili_cli.video import ffmpeg_utils
from bili_cli.video import srt_utils
from bili_cli.video.models import Subtitle, SubtitlePart
from bili_cli.const import CACHE_DIR, DATA_DIR, PART_DIR
from bili_cli.tools.idiom import Idiom
from bili_cli.tools import logger
from bili_cli.base import BaseModel, MongoQuery
from bili_cli import dto, mod, const, utils
from bili_cli.config import get_album, AlbumConfig
from bili_cli.mod import Part


class Data(BaseModel):
    part_used: Dict[str, int] = pydantic.Field(defaultdict(int))
    history: List['History'] = pydantic.Field([])

    def add_part_use_times(self, part_id):
        times = self.part_used.get(part_id, 0)
        self.part_used[part_id] = times + 1

    def get_history(self, id) -> 'History':
        for h in self.history:
            if h.id == id:
                return h
        return None


class History(BaseModel):
    id: str = pydantic.Field("")
    name: str = pydantic.Field("")
    #  bili_name: str = pydantic.Field("")
    ts: list = pydantic.Field([])
    ctime: datetime = pydantic.Field(None)

    @classmethod
    def build(cls, bili_name: str, ts: list) -> 'History':
        ts_id = ts[0].split("/")[-1].rsplit(".", 1)[0]
        now = datetime.now()
        id = f"{ts_id}-{now.timestamp()}"
        name = f"{bili_name}-{id}"
        item = cls(
            id=id,
            name=name,
            ts=ts,
            ctime=datetime.now().isoformat()
        )
        return item


class PartManage(BaseModel):

    album_id: str = pydantic.Field("", title="")
    bili_name: str = pydantic.Field("", title="站点名称")
    data_dir: str = pydantic.Field("", title="数据存放位置")
    data_part_dir: str = pydantic.Field("", title="数据part目录")
    srt_dir: str = pydantic.Field("", title="字幕目录")
    data_path: str = pydantic.Field("", title="剪辑存储历史信息")
    part_dir: str = pydantic.Field("", title="切片总目录")
    origin_total_dir: str = pydantic.Field(
        os.path.expanduser("~/Movies/电视剧"), title="原始文件总目录")
    subtitles: List[Subtitle] = pydantic.Field([], title="原始文件字幕列表")
    get_suffix: Callable = pydantic.Field(None)
    custom_title: Callable = pydantic.Field(None)
    album: AlbumConfig = pydantic.Field(None)

    # 可选参数
    #  store_dir: str = os.path.expanduser("~/Downloads")  # 生成文件存储地址

    class Config:
        name: str = ""  # 管理名称
        title: str = ""  # 管理名称
        #  category: str = ""  # 分类
        source_dir: str = ""  # 切片资源目录
        store_dir: str = const.CACHE_DIR  # 生成文件存储地址
        video_bed: dict = {}
        story: dict = {}
        part_root: str = ''  # 片段根目录
        episode_data: dict = {}  # 每集数据
        mix_black_ids: set = set()  # 混合视频黑名单

    @property
    def common_ts(self):
        """The common_ts property."""
        return os.path.join(
            PART_DIR, self.bili_name, f"{self.bili_name}-common.ts")

    def get_root(self):
        """剪辑视频根目录"""
        return os.path.join(
            const.get_montage_root(), self.album.category,
            self.album.title,
        )

    @property
    def source_dir(self):
        """剪辑视频根目录"""
        return self.Config.source_dir or os.path.join(self.get_root(), '片段合集')

    @property
    def part_root(self):
        """片段根目录"""
        return self.Config.part_root or const.get_part_dir()

    @property
    def episode_data(self) -> dict:
        """剪辑视频根目录"""
        return self.Config.episode_data or self.album.episode_data

    def log_prefix(self):
        return f"album: {self.album_id} user: {self.bili_name}"

    def load(self):
        # 矫正 album_id
        if self.Config.name and not self.album_id:
            self.album_id = self.Config.name
        # 矫正 Config.name
        if not self.Config.name and self.album_id:
            self.Config.name = self.album_id
        if not self.album_id or not self.Config.name:
            raise ValueError((
                f"PartManage Config.name: {self.Config.name}"
                f"album_id: {self.album_id} must not None"
            ))

        self.album = get_album(self.album_id)

        self.data_dir = os.path.join(DATA_DIR, self.album_id)
        self.part_dir = os.path.join(self.part_root, self.album_id)
        self.data_path = os.path.join(self.data_dir, self.bili_name + ".json")
        self.srt_dir = os.path.join(self.data_dir, "srt")
        self.data_part_dir = os.path.join(self.data_dir, "part")
        try:
            os.makedirs(self.data_dir)
        except Exception:
            pass
        try:
            os.makedirs(self.srt_dir)
        except Exception:
            pass
        try:
            os.makedirs(self.part_dir)
        except Exception:
            pass
        try:
            os.makedirs(self.data_part_dir)
        except Exception:
            pass
        return self

    def save_subtitles(self):
        _path: str
        for _path in walkfile(self.origin_total_dir):
            if '爱情公寓' in _path and _path.endswith(".srt"):
                video = _path.replace(".srt", ".mp4")
                sub = srt_utils.get_subtitle(_path, with_pinyin=True)
                sub.video = video
                dump_path = os.path.basename(_path).rsplit(".", 1)[0] + ".dump"
                dump_path = os.path.join(self.srt_dir, dump_path)
                #  print(dump_path)
                with open(dump_path, 'wb') as f:
                    # 序列化对象到一个data.pickle文件中
                    # 指定了序列化格式的版本pickle.HIGHEST_PROTOCOL
                    pickle.dump(sub, f, pickle.HIGHEST_PROTOCOL)

        return self

    def init_subtitles(self):
        self.subtitles = []
        for _dump_path in walkfile(self.srt_dir):
            with open(_dump_path, 'rb') as f:
                data: Subtitle = pickle.load(f)
                self.subtitles.append(data)
        self.subtitles.sort(key=lambda o: o.video)
        #  for sub in self.subtitles:
        #  print(sub.video)
        return self

    def get_data(self) -> 'Data':
        print(self.data_path)
        if os.path.exists(self.data_path):
            data = read_dict(self.data_path)
            return Data(**data)
        return Data()

    def save_data(self, data: 'Data'):
        write_dict(self.data_path, json.loads(data.json()))

    def get_part_by_id(self, id: str) -> 'Part':
        item = self.find_part(id)
        if item:
            return item
        path = os.path.join(self.data_part_dir, id+".json")
        if not os.path.exists(path):
            return None
        data = read_dict(path)
        data['manage_name'] = self.album_id
        p = Part(**data)
        p.source_dir = os.path.join(
            self.source_dir, f"{self.album.title}{p.season}",
            f"{p.ep:0>2}-{p.episode_name}"
        )
        if not p.id:
            p.id = id
        return p

    def format_part(self, p: Part) -> Part:
        if not p:
            return p
        p.source_dir = os.path.join(
            self.source_dir,
            f"{self.album.title}{p.season}",
            f"{p.ep:0>2}-{p.episode_name}"
        )
        p.path = os.path.join(p.source_dir, f"{p.id}-{p.name}.mp4")
        return p

    def find_part(self, id: str) -> Part:
        p = Part.find_by_id(id)
        return self.format_part(p)

    def get_part(self, path: str) -> 'Part':
        id = os.path.basename(path).rsplit(".", 1)[0].split('-')[0]
        print(id)
        part = self.get_part_by_id(id)
        part.path = path
        return part

    def create_cache_dir(self, prefix=""):
        dir = os.path.join(
            CACHE_DIR,
            f"{self.bili_name}-{prefix}-{int(time.time() * 1000)}"
        )
        os.makedirs(dir)
        return dir

    def create_split_cache_dir(self, req: dto.SplitReqDTO):
        basename = os.path.basename(req.path).rsplit(".", 1)[0]
        cachedir = self.create_cache_dir(
            prefix=f"{basename}-{self.album_id}")
        req_id = os.path.basename(cachedir)
        req.id = req_id
        return cachedir

    def get_suffix_ts_list(self):
        suffix = []
        print(self.common_ts)
        if os.path.exists(self.common_ts):
            suffix.append(self.common_ts)
        if self.get_suffix:
            suffix.extend(self.get_suffix())
        else:
            part_dir = os.path.join(PART_DIR, self.bili_name)
            random_ts_list = []
            for _part in os.listdir(part_dir):
                if 'part' in _part and _part.endswith(".ts"):
                    random_ts_list.append(os.path.join(part_dir, _part))
            random.shuffle(random_ts_list)
            suffix.extend(random_ts_list)
        logger.info(f"album: {self.album_id} bili: {self.bili_name} suffix: {suffix}")
        return suffix

    def get_all_parts(self):
        for _path in walkfile(self.source_dir):
            if not _path.endswith(".mp4") or _path.startswith("."):
                continue
            yield self.get_part(_path)

    def get_all_ts_parts(self):
        for _path in walkfile(self.part_dir):
            if not _path.endswith(".ts") or _path.startswith("."):
                continue
            yield self.get_part(_path)

    def get_all_json_parts(self):
        for _path in walkfile(self.data_part_dir):
            if not _path.endswith(".json") or _path.startswith("."):
                continue
            id = os.path.basename(_path).rsplit(".", 1)[0].split('-')[0]
            yield self.get_part_by_id(id)

    def find_parts(self, page: int = 1, pagesize: int = 10):
        q = (
            MongoQuery.default()
            .eq('manage_name', self.album_id)
            .page(page).pagesize(pagesize)
            .sort('order')
        )
        res = Part.find_page_items(q)
        for item in res.data:
            self.format_part(item)
        return res

    def get_story(self, story_id):
        return self.album.get_story(story_id) or self.Config.story

    def get_story_part_ids(self, story_id):
        return self.album.get_story_part_ids(
            story_id) or self.Config.story[story_id]['part_ids']

    def get_story_parts(self, story_id):
        ids = self.get_story_part_ids(story_id)
        parts = []
        for id in ids:
            parts.append(self.get_part_by_id(id))
        return parts

    def get_parts_by_id(self, id):
        if id in self.Config.story:
            return self.get_story_parts(id)
        else:
            return [self.get_part_by_id(id)]

    def get_random_ids(self, total_minute: int, max_part_duration: int = 0):
        return self.make_mixture_video(
            "", total_seconds=total_minute * 60, with_suffix_video=False,
            is_get_id=True, max_part_duration=max_part_duration)

    def make_mixture_video(
        self, name: str = "", ids: list = [], seasons: list = [],
        total_seconds: int = 30 * 60, with_suffix_video=True,
        is_get_ts: bool = False, suffix_ts_list: list = [],
        max_part_duration: int = 0, is_get_id: bool = False,
    ):
        """制作混合视频"""
        #  cache_dir = self.create_cache_dir()
        data = self.get_data()
        # 总片段列表
        total_parts = []
        # 优先片段列表
        priority_parts = []
        # 废弃片段列表
        abandon_parts = []
        for part in self.get_all_ts_parts():
            times = data.part_used.get(part.id, 0)
            part.used_times = times
            total_parts.append(part)
        total_parts.sort(key=lambda o: o.used_times)
        for part in total_parts:
            print(part)
            if part.used_times == total_parts[0].used_times:
                priority_parts.append(part)
            else:
                abandon_parts.append(part)

        print("----------")
        print(len(priority_parts))
        #  for part in priority_parts:
        #  print(part)
        print("=============")
        print(len(abandon_parts))
        #  for part in abandon_parts:
        #  print(part)

        # 需要输出的 ts 列表
        work_ts_list = []
        # 需要输出的 id 列表
        work_id_list = []
        # 总时长
        total_duration = 0
        # 已经使用的集数
        used_episodes = set()
        # 指定了使用哪些id
        if ids:
            part_ids = []
            for _id in ids:
                if _id in self.Config.story:
                    part_ids.extend(self.Config.story[_id]['part_ids'])
                else:
                    part_ids.append(_id)
            for _id in part_ids:
                first_part = self.get_part_by_id(_id)
                print(_id, first_part)
                work_ts_list.append(self.get_part_ts(first_part))
                total_duration += first_part.info.duration
                used_episodes.add(first_part.episode)
                data.add_part_use_times(first_part.id)

        # 拼接 ts 列表
        def _append_ts(_duration, _parts):
            print('+++++++')
            part: Part
            for i, part in enumerate(_parts):
                # 同集不再出现
                if part.episode in used_episodes:
                    continue
                if seasons and part.season not in seasons:
                    continue
                print(part.path)
                print(part.info)
                if max_part_duration and part.info.duration > max_part_duration:
                    continue
                # 使用黑名单
                mix_black_ids = self.Config.mix_black_ids
                if mix_black_ids and part.id in mix_black_ids:
                    continue

                _duration += part.info.duration
                print(os.path.basename(part.path),
                      part.info.duration, _duration)
                data.add_part_use_times(part.id)
                ts = self.get_part_ts(part)
                work_ts_list.append(ts)
                work_id_list.append(part.id)
                used_episodes.add(part.episode)
                if _duration > total_seconds:
                    break
            return _duration

        print('use priority')
        random.shuffle(priority_parts)
        total_duration = _append_ts(total_duration, priority_parts)
        if total_duration < total_seconds:
            print('use abandon')
            random.shuffle(abandon_parts)
            _append_ts(total_duration, abandon_parts)

        if with_suffix_video:
            work_ts_list.extend(self.get_suffix_ts_list())
        if suffix_ts_list:
            work_ts_list.extend(suffix_ts_list)
        if is_get_ts:
            self.save_data(data)
            return work_ts_list
        if is_get_id:
            self.save_data(data)
            return work_id_list

        print(name)
        self.concat_video(work_ts_list, name)
        # 保存使用数据
        self.save_data(data)
        return data

    def concat_video(self, ts: list, name) -> str:
        if not name.endswith(".mp4"):
            name += ".mp4"
        dir = os.path.join(self.Config.store_dir,
                           f"{self.bili_name}-{str(time.time())}")
        os.makedirs(dir)
        path = os.path.join(dir, name)
        ffmpeg_utils.concat_ts_to_mp4(ts, path)

        # 复制封面
        first_id = os.path.basename(ts[0]).rsplit('.', 1)[0]
        first_part = self.get_part_by_id(first_id)
        if first_part:
            self.copy_part_image_to_dir(first_part, dir)
        return dir

    def copy_episode_image_to_dir(self, episode, to_dir):
        img_dir = episode.part_source_dir
        if os.path.exists(img_dir):
            for name in os.listdir(img_dir):
                if not name.endswith(".png"):
                    continue
                img = os.path.join(img_dir, name)
                shutil.copy(img, to_dir)
        ep_path = episode.path
        ep_dir = os.path.dirname(ep_path)
        if os.path.exists(ep_dir):
            for name in os.listdir(ep_dir):
                if not name.endswith(".png"):
                    continue
                if not name.startswith(episode.episode_id):
                    continue
                img = os.path.join(ep_dir, name)
                shutil.copy(img, to_dir)

    def copy_part_image_to_dir(self, part, to_dir):
        print(part.source_dir)
        if os.path.exists(part.source_dir):
            for name in os.listdir(part.source_dir):
                if not name.endswith(".png"):
                    continue
                img = os.path.join(part.source_dir, name)
                print(img, to_dir)
                try:
                    shutil.copy(img, to_dir)
                except Exception as e:
                    print(e)

    def get_part_ts(self, part: Part) -> str:
        ts_path = os.path.join(self.part_dir, f"{part.id}.ts")
        if not os.path.exists(ts_path):
            return None
        return ts_path

    def get_or_create_part_ts(self, part: Part) -> str:
        ts_path = os.path.join(self.part_dir, f"{part.id}.ts")
        if not os.path.exists(ts_path):
            ffmpeg_utils.to_ts(part.path, ts_path)
        return ts_path

    def make_story(
        self, store_id: str, suffix_ts_list: list = [], with_suffix=True,
    ) -> Data:
        """制作制定故事集"""
        name = ""
        if store_id in self.Config.story:
            part_detail = self.Config.story[store_id]
            ids = part_detail.get("part_ids")
            name = part_detail.get("title")
            name = f"{self.bili_name}-{name}-{str(time.time())}"
        elif store_id in self.episode_data:
            ep = self.get_episode(store_id)
            ids = ep.story
            titles = ep.subtitles
            random.shuffle(titles)
            name = titles[0]
        else:
            ids = [store_id]
            name = f"{self.bili_name}-{store_id}-{str(time.time())}"
        data = self.get_data()
        ts_list = []
        for id in ids:
            part = self.get_part_by_id(id)
            data.add_part_use_times(part.id)
            ts_list.append(self.get_part_ts(part))

        if with_suffix:
            if suffix_ts_list:
                ts_list.extend(suffix_ts_list)
            else:
                ts_list.extend(self.get_suffix_ts_list())

        for ts in ts_list:
            print(ts)
        self.concat_video(ts_list, name)
        self.save_data(data)
        return data

    def save_id_used(self, ids) -> Data:
        data = self.get_data()
        for id in ids:
            part = self.get_part_by_id(id)
            data.add_part_use_times(part.id)
        self.save_data(data)

    def search_parts(self, keywords):
        parts = []
        for sub in self.subtitles:
            #  print(sub)
            _parts = srt_utils.search_srt_parts(sub, keywords)
            parts.extend(_parts)

        #  for _part in parts:
            #  print(_part)
        print(f"找到{len(parts)}个片段")
        return parts

    def split_video_by_keyword(self, keywords):
        store_dir = os.path.join(
            self.Config.store_dir, 'part-' + ''.join(keywords) + str(time.time()))
        os.makedirs(store_dir)
        parts = self.search_parts(keywords)
        part: SubtitlePart
        for i, part in enumerate(parts):
            #  part.start -= timedelta(seconds=5)
            #  part.time += timedelta(seconds=5)
            name = os.path.basename(part.video).rsplit(".", 1)[0]
            #  if name != "S04E23":
            #  continue
            output = os.path.join(
                store_dir, name + part.text.split("\n")[0] + f"-{i}.mp4")
            print(part.video, output)
            ffmpeg_utils.cut_part(part.video, output, part)

    def search_idiom_parts(self):
        idiom = Idiom().load()
        parts = []
        for sub in self.subtitles:
            _srt: SubRipItem
            for _srt in sub.srt.data:
                text = _srt.text
                idioms = idiom.find_idioms(text)
                if idioms:
                    print(idioms)
                    break
        print(f"找到{len(parts)}个片段")
        return parts

    def init_part(self) -> Part:
        return Part(manage_name=self.album.id)

    def path_to_part(self, path) -> Part:
        id = os.path.basename(path).rsplit(".", 1)[0].split('-')[0]
        part = self.init_part()
        part.id = id
        part.episode = id.rsplit(".", 1)[0]
        part.season = int(id.split(".")[0][1:])
        path_list = path.split("/")
        ep, ep_name = path_list[-2].split("-")
        part.ep = int(ep)
        part.episode_name = ep_name
        part.name = path_list[-1].rsplit(".", 1)[0].split("-")[-1]
        part_order = id.rsplit(".", 1)[-1]
        part.order = (part.season * 100 + part.ep) * 100 + int(part_order)
        return part

    def save_parts_data(self):
        print(self.source_dir)
        for path in walkfile(self.source_dir):
            if not path.endswith(".mp4"):
                continue
            part = self.path_to_part(path)
            print(part.id)
            save_path = os.path.join(self.data_part_dir, part.id+".json")
            if os.path.exists(save_path):
                part_data = read_dict(save_path)
                part_data['manage_name'] = self.album.id
                Part(**part_data).save()
                #  p.manage_name = self.album.id
                continue
            info = ffmpeg_utils.get_video_info(path)
            part.info = info

            print(save_path)
            write_dict(save_path, part.dict())
            part.save()
            #  return
        #  for part in self.get_all_json_parts():

    def init_part_data(self, recreate: bool = False):
        print(self.source_dir)
        for path in walkfile(self.source_dir):
            if not path.endswith(".mp4"):
                continue
            logger.info(f"Part: {path} find")
            part = self.path_to_part(path)
            exist_part = Part.find_by_id(part.id)
            if exist_part and not recreate:
                continue
            if recreate:
                logger.info(f"Part: {path} 重新初始化")

            info = ffmpeg_utils.get_video_info(path)
            part.info = info
            part.save()

    def save_part(self, part: Part) -> Part:
        save_path = os.path.join(self.data_part_dir, part.id+".json")
        data = read_dict(save_path)
        data['name'] = part.name
        write_dict(save_path, data)
        data['manage_name'] = self.Config.name
        p = Part(**data)
        p.save()
        return p

    def remove_bed(self, path: str, output: str = ""):
        if not self.Config.video_bed:
            raise ValueError("video_bed can not be None")

        if not output:
            prefix, ext = path.rsplit(".", 1)
            output = f"{prefix}_remove_bed.{ext}"
        print(output)

        basename = os.path.basename(path).rsplit(".", 1)[0]
        time_data = self.Config.video_bed.get(basename)
        ru_parts = []
        for start, t in time_data[1:]:
            ru_parts.append(ffmpeg_utils.Part(start=start, time=t))
        ffmpeg_utils.remove_unnecessary_part(
            path, output, ru_parts,
        )
        return output

    def get_episode(self, path) -> mod.EpisodeModel:
        basename = os.path.basename(path).split(".")[0]
        return self.get_episode_by_id(basename)

    def get_episode_by_id(self, id) -> mod.EpisodeModel:
        item = self.album.get_episode(id)
        item.part_source_dir = os.path.join(
            self.source_dir, item.season_title,
            f"{item.ep_str}-{item.get_title()}"
        )
        return item

    def get_episodes(self, season: int = 0) -> List[mod.EpisodeModel]:
        episodes = []
        for id, data in self.episode_data.items():
            item = self.get_episode_by_id(id)
            #  print(item)
            if season > 0 and item.season != season:
                continue
            episodes.append(item)
        return episodes

    def move_path_to_episode(self, path: str, episode: mod.EpisodeModel):
        """移动文件到剧集文件夹"""
        def _get_split_cache(ep: mod.EpisodeModel):
            dirs = []
            for name in os.listdir(const.CACHE_DIR):
                if name.startswith(f"{self.bili_name}-{ep.id}-{self.album.id}"):
                    dirs.append(os.path.join(const.CACHE_DIR, name))
            return dirs

        from_dir, name = os.path.split(path)
        episode = self.get_episode_by_id(episode.id)
        path = os.path.join(from_dir, name)
        to_dir = episode.part_source_dir
        logger.info(f"{path} move to: {to_dir}")
        # 创建目标目录
        if not os.path.exists(to_dir):
            logger.info(f"创建目标目录 {to_dir}")
            os.makedirs(to_dir)
        to_file = os.path.join(to_dir, name)
        caches = _get_split_cache(episode)
        for dir in caches:
            if not os.path.exists(os.path.join(dir, name)):
                shutil.copy(path, dir)
                logger.info(f"复制到缓存目录 {name} {dir}")
        # 如果已经存在直接删除原图
        if os.path.exists(to_file):
            os.remove(path)
            logger.info(f"{to_file} 已存在，直接删除 {name}")
        else:
            shutil.move(path, to_dir)
            logger.info(f"移动到剧集目录 {name} {to_dir}")

    def move_screenshot(self, from_dir: str):
        for name in os.listdir(from_dir):
            if not name.endswith('.png'):
                continue
            part = utils.match_part(const.COMMON_PART_ID_REG, name)
            if not part:
                continue
            if not name.startswith(self.album.short):
                continue
            if not self.get_part_by_id(part.part_id):
                continue
            episode = self.get_episode_by_id(part.episode_id)
            if not episode:
                continue
            logger.debug(f"match {const.COMMON_PART_ID_REG} for {name} to {part}")
            self.move_path_to_episode(os.path.join(from_dir, name), episode)

    def split_video(self, req: dto.SplitReqDTO):
        logger.info(f"{self.log_prefix()} split req: {req}")
        if self.can_split_by_cache(req):
            return self.split_video_by_cache(req)
        origin_path = req.path
        count = req.count
        split_time = req.split_time
        basename = os.path.basename(origin_path).rsplit(".", 1)[0]
        episode = self.get_episode_by_id(basename)
        cachedir = self.create_split_cache_dir(req)
        # 复制一个新文件
        path = shutil.copyfile(
            origin_path, os.path.join(cachedir, f"{basename}-tmp.mp4"))
        logger.info(f"split video copy to {path}")
        remove_files = []
        remove_files.append(path)
        if req.is_remove_bed:
            output = os.path.join(cachedir, f"{basename}-rbed.mp4")
            logger.info(f"split video remove_bed: {output}")
            time_data = None
            if self.Config.video_bed:
                time_data = self.Config.video_bed.get(basename)
            else:
                time_data = episode.bed
            logger.info(f"{self.log_prefix()} {time_data}")
            #  ru_parts = []
            #  for start, t in time_data[1:]:
                #  ru_parts.append(ffmpeg_utils.Part(start=start, time=t))
            ffmpeg_utils.remove_unnecessary_part(
                path, output, time_data[1:],
            )
            path = output
            remove_files.append(path)

        if req.is_average:
            duration = int(ffmpeg_utils.get_duration(path))
            split_time = int(duration / count) + 1
            logger.debug(f"分割个数: {count} 分割时间: {split_time} / {duration}")

        if req.start_time:
            duration = int(ffmpeg_utils.get_duration(path))
            tmppath = os.path.join(cachedir,
                                   f"{basename}-start-{req.start_time}.mp4")
            ffmpeg_utils.cut_video(path, tmppath, req.start_time,
                                   duration - req.start_time)
            remove_files.append(tmppath)
            path = tmppath

        # 将视频切割为 ts 文件
        ts_files = ffmpeg_utils.to_ts_and_split(path, path, split_time)
        self.concat_split_ts(req, ts_files, cachedir)

        # 清理缓存
        remove_files.append(path)
        for file in remove_files:
            try:
                os.remove(file)
            except Exception:
                pass
        return cachedir

    def split_video_by_cache(self, req: dto.SplitReqDTO):
        print(f"使用缓存分割视频 {req.path}, {req.count}")
        cachedir = self.create_split_cache_dir(req)
        ts = self.get_split_cache_ts(req)
        self.concat_split_ts(req, ts, cachedir)
        return cachedir

    def concat_split_ts(
        self, req: dto.SplitReqDTO, ts_files: list, cachedir: str
    ):
        print(req)
        #  raise Exception()
        basename = os.path.basename(req.path).rsplit(".", 1)[0]
        episode = self.get_episode_by_id(basename)
        part_name = basename
        if req.prefix:
            part_name = req.prefix
        #  split_paths = []
        cache_ts_list = []
        full_ts_list = []
        # ts 列表总时长
        total_ts_dur: float = 0
        cards = []
        # 添加前缀
        if req.with_prefix:
            prefix_ts = self.get_suffix_ts_list()
            full_ts_list.extend(prefix_ts)
            part_dur = self.get_split_ts_list_duration(prefix_ts)
            from_ = round(total_ts_dur)
            total_ts_dur += part_dur
            to = round(total_ts_dur)
            card = mod.Card.build(from_, to, "跳过")
            #  card.to_dur = tools.format_duration(to)
            cards.append(card)

        split_name = ""
        for i, name in enumerate(ts_files):
            part = i + 1
            name = os.path.join(cachedir, name)
            names = [name]
            if req.with_suffix:
                names.extend(self.get_suffix_ts_list())
            # 如果有前缀，最后一个片段就不要后缀了
            if req.with_prefix and part == len(ts_files):
                names = [name]
            split_name = f"{part_name}.{part}"
            if req.use_custom_title:
                split_name = self.custom_title(part_name, part)
            elif req.get_part_title(part):
                split_name = req.get_part_title(part)
            elif req.part_title_fmt:
                split_name = self.format_part_title(req, episode, part)
            print(cachedir, split_name)
            split_path = os.path.join(cachedir, split_name)
            #  split_paths.append(split_path)
            print('=' * 100, req.is_concat_full)
            if req.is_concat_full:
                full_ts_list.extend(names)
                part_dur = self.get_split_ts_list_duration(names)
                from_ = round(total_ts_dur)
                #  total_ts_dur += round(part_dur)
                total_ts_dur += part_dur
                to = round(total_ts_dur)
                card = mod.Card.build(from_, to, f"P{part}")
                #  card.to_dur = tools.format_duration(to)
                cards.append(card)
            else:
                ffmpeg_utils.concat_ts_to_mp4(names, split_path)
            cache_ts_list.append(name)

        if req.is_concat_full:
            #  full_info = ffmpeg_utils.get_video_info(split_path)
            history = self.get_history_by_req(req)
            #  history.duration = full_info.duration
            history.cards = cards
            history.title = split_name
            history.save()
            dump_path = os.path.join(cachedir, f"{history.id}.json")
            history.dump_file(dump_path)
            ffmpeg_utils.concat_ts_to_mp4(full_ts_list, split_path)

        for name in cache_ts_list:
            try:
                shutil.move(name, self.get_split_cache_dir(req))
            except Exception:
                pass

    def get_history_by_req(self, req: dto.SplitReqDTO) -> mod.HistoryModel:
        item = mod.HistoryModel.find_by_id(req.id)
        if not item:
            item = mod.HistoryModel(
                id=req.id,
                user_id=self.bili_name,
                album_id=self.album.id
            )
            item.save()
        return item

    def get_split_ts_list_duration(self, ts_list: list) -> float:
        d = 0
        for ts in ts_list:
            info = ffmpeg_utils.get_or_create_video_info(ts)
            d += info.duration
        return d

    def format_part_title(
        self, req: dto.SplitReqDTO, episode: mod.EpisodeModel, part: int
    ) -> str:
        data = episode.get_format_kwargs()
        return req.part_title_fmt.format(
            part=part,
            part_fmt=part_fmt(req.count, part),
            **data
        )

    def get_split_cache_dir(self, req: dto.SplitReqDTO):
        basename = os.path.basename(req.path).rsplit(".", 1)[0]
        dir = os.path.join(
            const.get_part_dir(),
            "split",
            self.album.id,
            f"{basename}-{req.count}-{req.is_remove_bed}"
        )
        try:
            os.makedirs(dir)
        except Exception:
            pass
        return dir

    def get_split_cache_ts(self, req: dto.SplitReqDTO) -> List:
        dirs = []
        dir = self.get_split_cache_dir(req)
        for name in os.listdir(dir):
            if not name.endswith(".ts"):
                continue
            dirs.append(os.path.join(dir, name))
        dirs.sort()
        return dirs

    def can_split_by_cache(self, req: dto.SplitReqDTO) -> bool:
        ts = self.get_split_cache_ts(req)
        if len(ts) == req.count:
            return True
        return False


def part_fmt(count, part):
    if count == 2:
        return '上' if part == 1 else '下'


class SplitPart(mod.EpisodeModel):
    part: int = pydantic.Field(0, title="片段数")
    title: str = pydantic.Field("", title="片段名称")
    #  title: str = pydantic.Field("", title="片段名称")


if __name__ == "__main__":
    import sys
    #  args = sys.argv[1:]
    #  action = args[0]
    #  ipart = IpartmentManage(bili_name="xinxin").load()
    #  ipart.make_mixture_video(f"{time.time()}")
