#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import os
import sys
import inspect
import pydantic
import time
from typing import List, Type, Dict
import pprint

from bili_cli.base import BaseModel
from bili_cli.part.base import PartManage, Part, Data
from bili_cli.const import TOM_JERRY_BED, IPARTMENT_BED, IPARTMENT_PART_DATA
from bili_cli.dto import MixtureReqDTO
from bili_cli import dto, const
from bili_cli.video import ffmpeg_utils
from bili_cli.types import UserID
from bili_cli.mod import AuthUser

PART_WD512_2 = "/Volumes/WD512-2/bili_cli/part"
PART_GETEA = "/Volumes/Getea/bili_cli/part"
SOURCE_ROOT_GETEA = "/Volumes/Getea/Movies"


def get_third_part_root():
    return const.get_part_dir()


def get_source_root():
    return SOURCE_ROOT_GETEA


def get_source_dir(path):
    return os.path.join(get_source_root(), path)


class CommonManage(PartManage):

    class Config(PartManage.Config):
        name = "common"
        title = "公用"
        source_dir = get_source_dir('公用/片段合集')


class AbandonManage(PartManage):

    class Config(PartManage.Config):
        name = const.MANAGE_NAME_ABANDON
        title = const.ALBUM_ABANDON
        source_dir = get_source_dir(f'电视剧/{const.ALBUM_ABANDON}/搞笑切片')


class MovieManage(PartManage):

    class Config(PartManage.Config):
        name = const.MANAGE_NAME_MOVIE
        title = const.ALBUM_MOVIE
        source_dir = get_source_dir('电影/片段合集')
        episode_data = const.MOVIE_DATA


class IpartmentManage(PartManage):

    class Config(PartManage.Config):
        name = "ipartment"
        title = "爱情公寓"
        category = "电视剧"
        source_dir = get_source_dir("电视剧/爱情公寓/搞笑切片")
        video_bed = IPARTMENT_BED
        story = IPARTMENT_PART_DATA
        episode_data = const.IPARTMENT_DATA


class LordLoserManage(PartManage):

    class Config(PartManage.Config):
        name = "lord_loser"
        title = "破事精英"
        category = '电视剧'
        source_dir = get_source_dir("电视剧/破事精英/搞笑切片")
        episode_data = const.LORDLOSER_DATA


class YixiManage(PartManage):

    class Config(PartManage.Config):
        name = "yixi"
        title = "一年一度喜剧大赛"
        source_dir = get_source_dir("综艺/一年一度喜剧大赛/片段合集")
        mix_black_ids = set([
            '喜1.3.11',
            '喜1.8.1', '喜1.10.1', '喜1.10.3', '喜1.10.4', '喜1.11.2',
            '喜2.1.5', '喜2.2.2', '喜2.2.3', '喜2.2.5', '喜2.3.3', '喜2.3.4',
            '喜2.3.5', '喜2.3.6', '喜2.5.1', '喜2.5.2', '喜2.5.4', '喜2.6.1',
            '喜2.6.2', '喜2.6.5', '喜2.8.3', '喜2.9.5', '喜2.10.1', '喜2.10.2',
            '喜2.10.3', '喜2.10.5'
        ])
        story = const.STORY_YIXI


class MovieSongManage(PartManage):

    class Config(PartManage.Config):
        name = const.MANAGE_NAME_MOVIE_SONG
        title = "影视歌曲"
        source_dir = get_source_dir('歌曲/影视歌曲')


class MusicManage(PartManage):

    class Config(PartManage.Config):
        name = const.MANAGE_NAME_MUSIC
        title = const.ALBUM_MUSIC
        source_dir = get_source_dir('歌曲/音乐')


class OpusculeManage(PartManage):
    """小品"""

    class Config(PartManage.Config):
        name = "opus"
        title = "小品"
        #  source_dir = os.path.expanduser("~/Movies/小品/剪辑")
        source_dir = os.path.join(get_source_root(), "综艺/小品/单个作品")

    def path_to_part(self, path) -> Part:
        dirname = os.path.dirname(path).split("/")[-1]
        if '-' in dirname:
            return super().path_to_part(path)

        id, ep_name = os.path.basename(path).split(".")[0].split('-')
        part = self.init_part()
        part.id = id
        part.episode = id
        part.season = 1
        part.ep = int(id[1:])
        part.episode_name = ep_name
        part.name = ep_name
        part.order = part.ep
        return part


class TomJerryManage(PartManage):

    class Config(PartManage.Config):
        name = "tom_jerry"
        title = "猫和老鼠"
        #  source_dir = os.path.expanduser("~/Movies/视频制作/动漫/猫和老鼠")
        source_dir = os.path.join(get_source_root(), "动漫/猫和老鼠/去掉片头片尾")
        video_bed = TOM_JERRY_BED

    def path_to_part(self, path) -> Part:
        dirname = os.path.dirname(path).split("/")[-1]
        if '-' in dirname:
            return super().path_to_part(path)

        id, ep_name = os.path.basename(path).split(".")[0].split('-')
        part = self.init_part()
        part.id = id
        part.episode = id
        part.season = 1
        part.ep = int(id[1:])
        part.episode_name = ep_name
        part.name = ep_name
        part.order = part.ep
        return part

    def remove_bed(self, name, output):
        print(name)
        path = os.path.expanduser("~/Movies/动漫/猫和老鼠157集4K蓝光TV版")
        path = os.path.join(path, name + '.mp4')
        output = os.path.join(self.Config.store_dir,
                              name + f"_remove_bed_{int(time.time())}.mp4")
        return super().remove_bed(path, output)


MANAGE_MAP: Dict[str, PartManage] = {}


def init():
    clzs = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for name, clz in clzs:
        if clz.__base__.__name__ == 'PartManage':
            MANAGE_MAP[clz.Config.name] = clz


init()


class MakeManageConfig(BaseModel):
    manage_clz: Type[PartManage] = pydantic.Field()
    max_part_duration: int = pydantic.Field(0)


class MakeConfig(BaseModel):
    manage_name: str = pydantic.Field()
    bili_name: str = pydantic.Field()
    manages: List[MakeManageConfig] = pydantic.Field()
    title_fmt: str = pydantic.Field("")
    #  title_func: Callable = pydantic.Field(None)

    @classmethod
    def build(
        cls, bili_name: str, manage_name: str,  manages: List[Type[PartManage]]
    ) -> 'MakeManageConfig':
        return cls(
            manage_name=manage_name, bili_name=bili_name,
            manages=manages
        )

    def get_manage(self) -> PartManage:
        return MANAGE_MAP.get(self.manage_name)(
            bili_name=self.bili_name).load()

    def set_title_fmt(self, fmt) -> 'MakeConfig':
        self.title_fmt = fmt
        return self


MINUTE_10_SUFFIXS = [
    MakeManageConfig(manage_clz=LordLoserManage, max_part_duration=3 * 60),
    MakeManageConfig(manage_clz=IpartmentManage, max_part_duration=2 * 60),
]

MAKE_CONFIGS = [

]


class WxnacyConfig():
    pass


MAKE_CONFIGS.append(
    MakeConfig.build('wxnacy', YixiManage.Config.name, [
        #  MakeManageConfig(manage_clz=NogeManage, max_part_duration=3 * 60),
        MakeManageConfig(manage_clz=OpusculeManage),
        MakeManageConfig(manage_clz=TomJerryManage),
        #  MakeManageConfig(manage_clz=IpartmentManage, max_part_duration=2 * 60),
    ])
)


MAKE_CONFIGS.append(
    MakeConfig.build('wxnacy', MovieManage.Config.name, [
        MakeManageConfig(manage_clz=IpartmentManage, max_part_duration=2 * 60),
    ])
)


class WenConfig():
    pass


def get_make_config(bili_name: str, manage_name: str) -> MakeConfig:
    config: MakeConfig
    for config in MAKE_CONFIGS:
        if config.bili_name == bili_name and config.manage_name == manage_name:
            return config
    return None


def get_manage(name, bid: UserID) -> PartManage:
    """获取片段管理器"""
    bili_name = bid
    if isinstance(bid, int):
        user = AuthUser.find_by_id(bid)
        bili_name = user.bili_name
    manage = MANAGE_MAP.get(name) or None
    if manage:
        return manage(album_id=name, bili_name=bili_name).load()
    else:
        return PartManage(album_id=name, bili_name=bili_name).load()


def get_manages() -> List[PartManage]:
    """获取片段管理器"""
    return list(MANAGE_MAP.values())


def get_suffix_ts(name, bili_name) -> List[str]:
    config = get_make_config(bili_name, name)
    #  manages = get_suffix_manages(name, bili_name)
    #  manages
    suffix = []
    for manage_conf in config.manages:
        mana = manage_conf.manage_clz(bili_name=bili_name).load()
        ts = mana.make_mixture_video(
            "", total_seconds=60, with_suffix_video=False, is_get_ts=True,
            max_part_duration=manage_conf.max_part_duration,
        )
        suffix.extend(ts)
    return suffix


def remake_history(manage_name: str, bili_name: str, id: str):
    manage = get_manage(manage_name, bili_name)
    history = manage.get_data().get_history(id)
    pprint.pprint(history.ts)
    ts_list = [o for o in history.ts if manage_name in o]
    suffix_ts = get_suffix_ts(manage_name, bili_name)
    ts_list.extend(suffix_ts)
    pprint.pprint(ts_list)
    manage.concat_video(ts_list, history.name)


def make_mixture(req: MixtureReqDTO) -> Data:
    """制作混合视频"""
    manage = get_manage(req.manage_name, req.bili_name)
    suffix = get_suffix_ts(req.manage_name, req.bili_name)
    ts_list = manage.make_mixture_video(
        "", ids=req.ids, total_seconds=req.minute * 60,
        with_suffix_video=False, suffix_ts_list=suffix,
        max_part_duration=20 * 60
    )
    pprint.pprint(ts_list)
    pprint.pprint(suffix)
    return manage.get_data()


def make_story(req: MixtureReqDTO) -> Data:
    """制作混合视频"""
    manage = get_manage(req.manage_name, req.bili_name)
    suffix = []
    if req.with_suffix:
        suffix = get_suffix_ts(req.manage_name, req.bili_name)
    data = manage.make_story(
        req.ids[0], suffix_ts_list=suffix, with_suffix=req.with_suffix)
    return data


def make_video(req: MixtureReqDTO) -> str:
    """制作混合视频"""
    manage = get_manage(req.manage_name, req.bili_name)
    suffix = get_suffix_ts(req.manage_name, req.bili_name)
    ts_list = []
    for path in req.paths:
        if path.endswith('.mp4'):
            out = os.path.join(manage.Config.store_dir, f"{time.time()}.ts")
            ffmpeg_utils.to_ts(path, out)
            ts_list.append(out)
        elif path.endswith(".ts"):
            ts_list.append(path)
    ts_list.extend(suffix)
    print("使用片段")
    for ts in ts_list:
        print(ts)
    return manage.concat_video(
        ts_list, f"{req.bili_name}-{os.path.basename(req.paths[0])}")


def split_video(req: dto.SplitReqDTO) -> list:
    """分割视频"""
    print(f"SplitReqDTO {req}")
    manage = get_manage(req.manage_name, req.bili_name)

    def _get_suffix():
        return get_suffix_ts(req.manage_name, req.bili_name)

    manage.get_suffix = _get_suffix
    return manage.split_video(req)


if __name__ == "__main__":
    from bili_cli.video.models import SubtitlePart, Subtitle
    m = get_manage(const.MANAGE_NAME_YIXI, const.BILI_NAME_WXNACY)
    #  m.copy_part_image_to_dir(
    #  m.get_part_by_id('喜1.3.11'),
    #  '/Users/wxnacy/Downloads/xinxin-1706376749.654604')
    m = IpartmentManage().load().init_subtitles()
    #  req = dto.SplitReqDTO.default()
    #  req.path = "/sss/we.mp4"
    #  m.get_split_cache_dir(req)
    #  .init_subtitles()
    parts = m.search_parts(['诺拉'])
    part: SubtitlePart
    for part in parts:
        print(part.video, part.text, part.start)
