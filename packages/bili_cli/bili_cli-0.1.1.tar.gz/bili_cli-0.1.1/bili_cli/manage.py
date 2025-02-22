#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import pydantic
import os
from typing import Union, List, Self
from bili_cli.base import BaseModel, QueryResult
from bili_cli import mod, const, dto
from .mod import AuthUser
from bili_cli.bili import BaseBili, get_bili, get_bilis, init_season_config as init_season
from bili_cli.config import (
    SeasonConfig, get_user_album, UserAlbumConfig, get_users, get_albums,
    init_album, init_ua
)
from bili_cli.config.celerys import celery_app
from bili_cli.part.base import PartManage
from bili_cli.part import manage as pm
from bili_cli.make import get_config, init_vc, VideoConfig
from bili_cli.base import Query
from bili_cli.service import get_part_by_type_rand_part
from bili_cli.tools import logger
from .types import UserID
from .tools import time_statistics
from bili_cli.config import settings
from bili_cli.tools import make_pagination


class Manage(BaseModel):
    user_id: UserID = pydantic.Field(title="")
    album_id: str = pydantic.Field("", title="专辑")
    bili_name: str = pydantic.Field("", title="")
    config: UserAlbumConfig = pydantic.Field(None, title="配置")
    bili: BaseBili = pydantic.Field(None)
    pm: PartManage = pydantic.Field(None, title="片段管理")

    @classmethod
    def build(cls, album_id: str, user_id: UserID) -> Self:
        item = cls(album_id=album_id, user_id=user_id)
        bili_name = user_id
        if isinstance(user_id, int):
            user = AuthUser.find_by_id(user_id)
            bili_name = user.bili_name

        item.config = get_user_album(album_id, bili_name)
        if not item.config:
            return None
        item.bili_name = bili_name
        item.bili = get_bili(user_id)
        item.pm = pm.get_manage(item.album_id, bili_name)
        return item

    def match_archive_to_episode(self, arc: Union[mod.ArcAuditModel, str]
                                 ) -> mod.EpisodeModel:
        if isinstance(arc, str):
            arc = self.bili.find_by_id(arc, mod.ArcAuditModel)
            if not arc:
                return None
        if self.config.archive_to_episode_func:
            return self.config.archive_to_episode_func(self.config, arc)
        item = self.config.match_archive_to_episode(arc)
        return item

    def match_archive_to_part(
        self, arc: Union[mod.ArcAuditModel, str]
    ) -> mod.MatchPart:
        if isinstance(arc, str):
            arc = self.bili.find_by_id(arc, mod.ArcAuditModel)
            if not arc:
                return None
        return self.config.match_title_to_part(arc.title)

    def match_archive_to_season(self, arc: mod.ArcAuditModel
                                ) -> SeasonConfig:
        return self.bili.match_title_to_season_config(arc.title)

    #  @profile
    def refresh_archive_ext(self, arch: str | mod.ArcAuditModel
                            ) -> mod.ArcAuditModel:
        '''刷新稿件的扩展信息'''
        if isinstance(arch, str):
            arch: mod.ArcAuditModel = self.bili.find_archive(arch)

        # 刷新合集
        sea = self.match_archive_to_season(arch)
        sea_title = sea.title if sea else ""
        arch.set_ext_season_title(sea_title)

        # 刷新season_id
        if sea_title:
            sea_mod = self.bili.find_season(sea_title)
            if sea_mod:
                arch.set_ext_field('season_id', sea_mod.id)

        # 刷新cid
        if not arch.cid and arch.aid:
            res = self.bili.member_api.get_archive_videos(arch.archive.aid)
            arch.set_ext_cid(res.videos[0].cid)

        episode = self.match_archive_to_episode(arch)
        if episode:
            arch.set_ext_episode_id(episode.id)
            arch.ext.album_id = episode.album_id
        part = self.match_archive_to_part(arch)
        if part:
            arch.ext.part = part.part
        logger.info(f"{self.bili.log_prefix()} 刷新稿件: {arch.bvid} 扩展信息: {arch.ext}")
        self.bili.save(arch)
        return arch

    def refresh_archive_history_id(self, arch: str | mod.ArcAuditModel
                                   ) -> mod.ArcAuditModel:
        if isinstance(arch, str):
            arch: mod.ArcAuditModel = self.bili.find_by_id(
                arch, mod.ArcAuditModel)

        # 刷新 history_id
        if not arch.ext.history_id:
            history = self.find_history_by_archive(arch)
            if history:
                arch.ext.history_id = history.id
                self.bili.save(arch)
        return arch

    def find_history_by_archive(self, arch: mod.ArcAuditModel
                                ) -> mod.HistoryModel:
        q = Query.build(mod.HistoryModel).sort(
            'ctime', 'desc').eq('user_id', self.bili_name)
        result = mod.HistoryModel.find(q)
        historys: List[mod.HistoryModel] = result.data
        for h in historys:
            if arch.title == h.title:
                return h
        return None

    def split_episode(self, episode_id: str):
        logger.info(f"{self.bili.log_prefix()} split {self.album_id} {episode_id}")

        episode = self.pm.get_episode_by_id(episode_id)
        logger.info(f"episode: {episode.episode_id} bed: {episode.bed}")
        req = self.config.get_split_req_by_episode(episode)
        req.path = episode.path
        if req.prefix:
            req.prefix = req.prefix.format(**episode.get_format_kwargs())
        #  return
        if req.suffix_func:
            self.pm.get_suffix = req.suffix_func
        else:
            self.pm.get_suffix = self.get_split_suffix

        # 使用库里的名称
        if req.use_exist_part_title:
            req = self.fill_split_req_part_title(req, episode)

        logger.info(f"{self.bili.log_prefix()} split count: {req.count} is_remove_bed: {req.is_remove_bed}")
        logger.info(f"split episode: {episode_id} split req: {req}")
        #  raise Exception()
        dir = self.pm.split_video(req)
        # 复制封面
        self.pm.copy_episode_image_to_dir(episode, dir)

        return dir

    def fill_split_req_part_title(
            self, req: dto.SplitReqDTO, episode: mod.EpisodeModel):
        arc_data = self.bili.find_split_episode_last_archives(
            album_id=self.album_id, episode_id=episode.id)

        for p, arc in arc_data.items():
            p_title = arc.title
            if self.bili_name == const.BILI_NAME_XINXIN:
                if ' ' in p_title:
                    p_title = p_title.rsplit(' ', 1)[-1]
                    p_title = self.pm.format_part_title(
                        req, episode, p) + p_title
            req.part_data[p] = req.PartData(part=p, title=p_title)
        return req

    def get_suffix(self):
        return pm.get_suffix_ts(self.album_id, self.bili_name)

    def get_split_suffix(self):
        """获取分割需要的片尾片段"""
        ua_conf = get_user_album(self.album_id, self.bili_name)
        split_suffix = ua_conf.split_suffix
        ts_list = []
        for suffix_conf in split_suffix:
            part = get_part_by_type_rand_part(self.bili_name, suffix_conf)
            ts_list.append(part.get_ts_path())
        return ts_list

    def reply_archive_card(
            self, bvid: str,
    ) -> dto.ReplyAddResDTO:
        arc: mod.ArcAuditModel = self.bili.find_archive(bvid)
        if not arc.ext.history_id:
            return dto.BaseResDTO.default_error(message=f"找不到 history: {bvid}")
        history: mod.HistoryModel = mod.HistoryModel.find_by_id(
            arc.ext.history_id)
        message = history.build_card_reply()
        # 获取前缀
        episode = self.match_archive_to_episode(arc)
        if episode:
            prefix = self.config.get_reply(episode)
            message = prefix + "\n" + message
        print(message)
        return self.reply_archive(arc, message)
        #  return {}

    def reply_archive(
            self, arc: Union[str, mod.ArcAuditModel], message: str = ""
    ) -> dto.ReplyAddResDTO:
        if isinstance(arc, str):
            bvid = arc
            arc: mod.ArcAuditModel = self.bili.find_by_id(
                bvid, mod.ArcAuditModel)
        if not arc:
            return dto.BaseResDTO.default_error(message=f"找不到 bvid: {bvid}")
        if not message:
            episode = self.match_archive_to_episode(arc)
            message = self.config.get_reply(episode)
        if not message:
            return dto.BaseResDTO.default_error(message="message 不能为空")
        return self.bili.reply_add(arc.archive.aid, message)

    def move_screenshot(self, from_dir: str):

        for name in os.listdir(from_dir):
            if not name.endswith('.png'):
                continue
            episode = self.config.match_title_to_episode(name)
            if not episode:
                continue
            self.pm.move_path_to_episode(os.path.join(from_dir, name), episode)

    def load_video_config(self, id):
        config = get_config(self.bili_name, id)
        config.load(user_id=self.bili_name)
        return config

    def make_video_by_config(self, id: str):
        bili_name = self.bili_name
        config = self.load_video_config(id)
        # ts 列表总时长
        total_ts_dur: float = 1
        tmp_cards = []
        ts = []
        # 导航需要的配置列表
        #  nav_configs = []
        #  ts = config.get_ts_list()
        for conf in config.configs:
            conf_ts = conf.ts_list
            ts.extend(conf_ts)
            #  print(conf_ts)

            part_dur = self.pm.get_split_ts_list_duration(conf_ts)
            from_ = round(total_ts_dur)
            if from_ == 1:
                from_ = 0
            total_ts_dur += part_dur
            to = round(total_ts_dur)
            content = ""
            if conf.is_skip:
                content = "跳过"
            else:
                for p in conf.parts:
                    content += f"{p.name}"
            if conf.nav_title:
                content = conf.nav_title
            card = mod.Card.build(from_, to, content)
            #  card.to_dur = tools.format_duration(to)
            tmp_cards.append(card)

        # 合并跳过
        cards = [tmp_cards[0]]
        for i in range(1, len(tmp_cards)):
            tmp_card = tmp_cards[i]
            if cards[-1].content == tmp_card.content:
                cards[-1].to = tmp_card.to
                cards[-1].load()
            else:
                cards.append(tmp_card)

        # 隐藏正文后的跳过
        tmp_cards = cards
        cards = [tmp_cards[0]]
        for i in range(1, len(tmp_cards)):
            tmp_card = tmp_cards[i]
            if tmp_card.content == '跳过':
                cards[-1].to = tmp_card.to
                cards[-1].load()
            else:
                cards.append(tmp_card)

        # 是否使用随机后缀
        if config.with_random_suffix:
            suffix = pm.get_suffix_ts(config.manage_name, bili_name)
            ts.extend(suffix)

            part_dur = self.pm.get_split_ts_list_duration(conf_ts)
            total_ts_dur += part_dur
            to = round(total_ts_dur)
            cards[-1].to = to
            cards[-1].load()

        title = config.title
        if config.with_part_title:
            for conf in config.configs:
                if conf.is_skip:
                    continue
                for p in conf.parts:
                    title += f"《{p.name}》"
        #  保存历史数据
        h = mod.HistoryModel.find_by_id(id)
        if not h:
            h = mod.HistoryModel(
                id=id,
                user_id=self.bili_name,
                album_id=self.album_id,
            )
        h.cards = cards
        h.title = title
        h.save()
        cachedir = config.manage.concat_video(ts, title)
        # 复制封面
        for p in config.main_part.parts:
            config.manage.copy_part_image_to_dir(p, cachedir)
        if config.episode_ids:
            for ep_id in config.episode_ids:
                conf_episode = self.pm.get_episode_by_id(ep_id)
                config.manage.copy_episode_image_to_dir(conf_episode, cachedir)
        dump_path = os.path.join(cachedir, f"{h.id}.json")
        h.dump_file(dump_path)

        return cachedir


_MANAGE = {}


def get_manage(album_id, user_id) -> Manage:
    key = f"{album_id}-{user_id}"
    m = _MANAGE.get(key)
    if not m:
        m = Manage.build(album_id, user_id)
        _MANAGE[key] = m
    return m


@celery_app.task
def move_screenshot():
    logger.info('move_screenshot')
    fromdir = settings.VIDEO_SHOT_DIR
    for album in get_albums():
        for user in get_users():
            pm.get_manage(album.id, user.id).move_screenshot(fromdir)

    for album in get_albums():
        for user in get_users():
            m = Manage.build(album.id, user.id)
            if m:
                m.move_screenshot(fromdir)


@celery_app.task
def split_episode(album_id, user_id, episode_id):
    m = get_manage(album_id, user_id)
    res = m.split_episode(episode_id)
    return res


def make_episode_part_video(album_id: str, user_id: int, episode_id: str, *, is_async=False):
    res = []
    make_func = make_video_by_config
    if is_async:
        make_func = make_func.delay
    configs = VideoConfig.find_configs(
        user_id=user_id,
        album_id=album_id,
        episode_id=episode_id,
        type_='one_part',
        pagesize=100
    ).data
    for conf in configs:
        d_res = make_func(album_id, user_id, conf.id)
        data = {"id": conf.id, "data": d_res}
        res.append(data)
    return res


@celery_app.task
def make_video_by_config(album_id, user_id, id):
    return get_manage(album_id, user_id).make_video_by_config(id)


@celery_app.task
@time_statistics
def refresh_archive_ext(user_id: int = 0, album_id: str = None):
    album_count = 0
    archive_count = 0
    for bili in get_bilis(auth_user_id=user_id):
        season_configs = bili.get_season_configs(album_id=album_id)
        album_ids = set([o.album_id for o in season_configs])
        album_count = len(album_ids)
        for aid in album_ids:
            res = bili.find_normal_archives()
            archives = res.data
            arch: mod.ArcAuditModel
            archive_count = len(archives)
            for arch in archives:
                if arch.is_lock:
                    continue
                m = get_manage(aid, bili.auth.mid)
                m.refresh_archive_ext(arch)
    logger.info(f"refresh_archive_ext album count: {album_count} archive count: {archive_count}")


@celery_app.task
@time_statistics
def refresh_episode_archive(user_id: int = 0):
    user_id = int(user_id)
    for bili in get_bilis(auth_user_id=user_id):
        res = bili.find_normal_archives()
        archives = res.data
        for arch in archives:
            if not arch.ext.album_id or not arch.ext.episode_id:
                continue
            ep = mod.EpisodeArchiveModel.build(
                arch.ext.album_id, arch.ext.episode_id)
            ep_id = ep.get_id()
            exist_ep: mod.EpisodeArchiveModel = bili.find_by_id(
                ep_id, mod.EpisodeArchiveModel)
            if exist_ep:
                ep = exist_ep
            ep.archive_ids.append(arch.get_id())
            ep.archive_ids = list(set(ep.archive_ids))
            logger.info(f"{bili.log_prefix()} {ep.album_id}/{ep.episode_id} archives: {ep.archive_ids}")
            bili.save(ep)


def init_part(album_id: str, recreate: bool = False):
    m = pm.get_manage(album_id, bid=settings.default_auth_user_id)
    m.init_part_data(recreate=recreate)
    for part in m.find_parts(pagesize=2000).data:
        m.get_or_create_part_ts(part)


def init_db(action: str = '', auth_user_id: int = 0):
    for init_func in (init_album, init_season, init_ua, init_vc):
        func_name = init_func.__name__
        if action and func_name != f"init_{action}":
            continue
        logger.info(f'初始化 {func_name}')
        kw = {}
        if action == 'vc':
            kw['auth_user_id'] = auth_user_id
        init_func(**kw)


def find_episodes(album_id: str, auth_user_id: int, *, season: int = 0,
                  page: int = 1, pagesize: int = 10) -> QueryResult:
    m = get_manage(album_id, auth_user_id)
    episodes = m.pm.get_episodes(season=season)
    d = make_pagination(episodes, page=page, pagesize=pagesize)
    items = d['data']['items']
    ep: mod.EpisodeModel
    eps = []
    for ep in items:
        ea = mod.EpisodeArchiveModel.build(album_id, ep.id)
        ea = m.bili.find_by_id(ea.get_id(), mod.EpisodeArchiveModel)
        if ea:
            archive_ids = ea.archive_ids
            for arch_id in archive_ids:
                arch: mod.ArcAuditModel = m.bili.find_archive(arch_id)
                if arch.is_open:
                    ep.archives.append(arch)
            ep.archives.sort(key=lambda o: o.archive.title)
        eps.append(ep)
    return QueryResult(data=eps, total=d['data']['total'])


if __name__ == "__main__":
    import time
    b = time.perf_counter()
    #  m = get_manage(const.MANAGE_NAME_ZHUI_FENG, const.BILI_NAME_WEN)
    split_episode(const.MANAGE_NAME_IPARTMENT, const.BILI_NAME_WEN, 'S02E01')
    #  make_video_by_config(const.MANAGE_NAME_YIXI, const.USER.WXNACY, 'wxnacy-yixi-10101')
    print(time.perf_counter() - b)
