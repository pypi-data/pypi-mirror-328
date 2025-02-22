# Author:
# Description:


import pydantic
import subprocess
import os
import shutil
import traceback
import time
import gevent
import json
from datetime import datetime
from typing import List, Union, Self, Optional
from bili_cli.api import MemberApi, Api, QYApi, DEFAULT_QY_API
from bili_cli.apis import PassportApi, DEFAULT_PASSPORT_API
from bili_cli import dtos as dto, mod, const
from bili_cli.base import MongoQuery
from bili_cli.bili.section_episode_sort import SectionEpisodeSort
from bili_cli.bili.orm import BiliORM
from bili_cli.tools import create_qrcode, logger, get_bvid_from_url
from bili_cli.config import (
    get_user,
    SeasonConfig, SectionConfig, UserConfig,
    SeasonType,
    SectionSortType
)
from bili_cli.mod import AuthUser


class BaseBili(BiliORM, SectionEpisodeSort):
    #  auth: AuthModel = pydantic.Field(None)
    member_api: MemberApi = pydantic.Field(None)
    api: Api = pydantic.Field(None)
    qy_api: QYApi = pydantic.Field(None)
    passport_api: PassportApi = pydantic.Field(None)
    config: UserConfig = pydantic.Field(None)
    auth: mod.AuthUser = pydantic.Field(None)

    class Meta():
        NAME: str = ''
        DB: str = ''

        season_configs: List[SeasonConfig] = []

        @classmethod
        def get_season_config(cls, title: str) -> SeasonConfig:
            for s in cls.season_configs:
                if s.title == title:
                    return s.load()
            return None

        @classmethod
        def get_season_configs(cls) -> List[SeasonConfig]:
            return [o.load() for o in cls.season_configs]

    def load(self):
        self.config = get_user(self.Meta.NAME)
        self.qy_api = DEFAULT_QY_API
        self.passport_api = DEFAULT_PASSPORT_API
        return self

    def load_api(self, auth: AuthUser = None):
        if not auth:
            auth = self.auth
        self.member_api = MemberApi.build(auth)
        self.api = Api.build(auth)
        return self

    @classmethod
    def build(cls, auth_user_id: int) -> Self:
        item = cls()
        #  logger.info(f"{item.log_prefix()} build bili mid: {auth_user_id}")
        if not item.Meta.NAME:
            item.Meta.NAME = f"{auth_user_id}"
        if not item.Meta.DB:
            item.Meta.DB = f'bili_{auth_user_id}'
        auth: mod.AuthUser = mod.AuthUser.find_by_id(auth_user_id)
        item.auth = auth
        item.load_api()
        # 检查是否需要刷新
        if auth.is_need_refresh():
            logger.info(f"{item.log_prefix()} 进行刷新")
            item.refresh_auth()
            item.load_api()

        return item

    def log_prefix(self):
        auth_msg = ""
        if self.auth:
            auth_msg = f"{self.auth.name}({self.auth.mid})"
        return f"{auth_msg}"

    def match_title_to_season_config(self, title: str) -> SeasonConfig:
        for sea_conf in self.Meta.season_configs:
            if sea_conf.is_match_archive_title(title):
                return sea_conf

    def get_season_configs(self, album_id: str = None) -> List[SeasonConfig]:
        seasons: List[mod.SeasonModel] = [o for o in self.find_items(
            MongoQuery.build(mod.SeasonModel))]
        season_map = {o.title: o for o in seasons}

        configs = []
        for s in self.Meta.season_configs:
            if s.is_delete:
                continue
            if album_id and s.album_id != album_id:
                continue
            sea: mod.SeasonModel = season_map.get(s.title)
            if sea and sea.is_delete == 0:
                s.id = sea.id
                s.mtime = sea.mtime
            configs.append(s)
        return configs

    @classmethod
    def get_season_config(cls, title: str) -> SeasonConfig:
        for s in cls.Meta.season_configs:
            if s.title == title:
                return s
        return None

    @classmethod
    def get_season_config_by_album(cls, album_id: str) -> SeasonConfig:
        for s in cls.Meta.season_configs:
            if s.album_id == album_id:
                return s
        return None

    def search_section_add_episodes(
        self, section_id: int, keyword: str
    ) -> List[mod.SectionEpisodeModel]:
        episodes = []
        req = dto.ArchiveListReqDTO.default()
        req.keyword = keyword
        res = self.member_api.get_add_section_archives(req)
        if not res.arc_audits:
            return episodes

        for arc in res.arc_audits:
            if keyword not in arc.archive.title:
                continue
            res = self.member_api.get_archive_videos(arc.archive.aid)
            video = res.videos[0]
            ep = mod.SectionEpisodeModel(
                aid=arc.archive.aid, cid=video.cid,
                title=video.title)
            episodes.append(ep)
        return episodes

    def get_all_seasons(self):
        ps = 30
        req = dto.SeasonListReqDTO(ps=ps)
        import math
        for page in range(1, 10):
            req.pn = page
            res = self.member_api.get_seasons(req)
            if not res.seasons:
                break
            for sea in res.seasons:
                season = sea.season
                sections = sea.sections.sections
                for sec in sections:
                    sec_res = self.member_api.get_section(sec.id)
                    sec.episodes = sec_res.episodes
                season.sections = sections
                self.save(season)
                season.save()
                yield sea
            total_page = math.ceil(res.total / ps)
            if page >= total_page:
                break

    def del_season(self, id: int) -> dto.BaseResDTO:
        res = self.member_api.season_del(id)
        logger.info(f"{self.log_prefix()} 删除合集: {id} {res.is_success}")
        if res.is_success:
            update_res = self.delete_by_id(id, mod.SeasonModel)
            logger.info(f"{self.log_prefix()} 删除本地合集: {id} {update_res.count}")
        return res

    def search_season(self, name) -> dto.SeasonDetailResDTO:
        for res in self.get_all_seasons():
            if res.season.title == name:
                return res
        return None

    def refresh_season(self):
        seasons = [o.season for o in self.get_all_seasons()]
        logger.info(f"{self.log_prefix()} 现有集合数量: {len(seasons)}")
        season_ids = [o.id for o in seasons]

        # 查询本地合集列表
        query = MongoQuery.build(mod.SeasonModel)
        local_seasons: List[mod.SeasonModel] = list(self.find_items(query))

        del_seasons = [o for o in local_seasons if o.id not in season_ids]
        del_ids = []
        for sea in del_seasons:
            del_ids.append(str(sea.id))
            logger.info(f"{self.log_prefix()} 需要删除集合: {sea.title}")
        query = {"_id": {"$in": del_ids}}
        update_data = {"$set": {"is_delete": 1}}
        logger.info(f"{self.log_prefix()} update db: {self.Meta.DB} query: {query} update: {update_data}")
        res = self.get_db(mod.SeasonModel.Meta.TABLE).update_many(query, update_data)
        logger.info(f"{self.log_prefix()} 删除合集条数: {res.modified_count} 匹配条数 {res.matched_count}")
        res = mod.SeasonModel.get_db().update_many(query, update_data)
        logger.info(f"{self.log_prefix()} 删除合集条数: {res.modified_count} 匹配条数 {res.matched_count}")

    def search_or_create_season(self, name) -> dto.SeasonDetailResDTO:
        sea = self.search_season(name)
        if not sea:
            req = self.build_season_add_req(name)
            if not req:
                raise ValueError("season_add_req can not be None")
            res = self.member_api.season_add(req)
            sea = self.get_season(res.data)
        return sea

    def get_season(self, id: int) -> dto.SeasonDetailResDTO:
        sea = self.member_api.get_season(id)
        sections = sea.sections.sections
        for sec in sections:
            sec_res = self.member_api.get_section(sec.id)
            sec.episodes = sec_res.episodes
        sea.season.sections = sections
        self.save(sea.season)
        sea.season.save()
        return sea

    def build_season_add_req(self, title) -> dto.SeasonAddReqDTO:
        season = self.Meta.get_season_config(title)
        if not season:
            return dto.SeasonAddReqDTO(title=title)
        return season.to_season_add_req()

    def season_switch(self, season: mod.SeasonModel):
        #  根据配置自动修改开关
        s_d = self.Meta.get_season_config(season.title)
        s_forbid = s_d.forbid
        s_no_section = s_d.no_section
        return self.update_season(season.id, forbid=s_forbid, no_section=s_no_section)

    def update_season_by_config(self, sid: int):
        sea = mod.SeasonModel.find_by_id(sid)
        sea_conf = self.Meta.get_season_config(sea.title)
        return self.update_season(
            sid,
            forbid=sea_conf.forbid,
            no_section=sea_conf.no_section,
            desc=sea_conf.desc,
            cover=sea_conf.cover,
        )

    def update_season(
        self,
        sid: int,
        *,
        title: Optional[str] = None,
        desc: Optional[str] = None,
        cover: Optional[str] = None,
        forbid: Optional[int] = None,
        no_section: Optional[int] = None,
    ):
        if forbid is not None:
            res = self.member_api.season_switch_forbid(sid, forbid)
            logger.info(f"update season: {sid} forbid: {forbid} code: {res.code}")
            if not res.is_success:
                return False
        if no_section is not None:
            res = self.member_api.season_section_switch(sid, no_section)
            logger.info(f"update season: {sid} no_section: {no_section} code: {res.code}")
            if not res.is_success:
                return False
        edit_data = {}
        if title or desc or cover:
            q_sea = self.find_season(sid)
            edit_data['title'] = title or q_sea.title
            edit_data['desc'] = desc or q_sea.desc
            edit_data['cover'] = cover or q_sea.cover
            req = dto.SeasonEditReqDTO.build(sid, **edit_data)
            res = self.member_api.season_edit(req)
            logger.info(f"update season: {sid} {edit_data} code: {res.code}")
            if not res.is_success:
                return False
        return True

    def init_section(self, sea_d: dto.SeasonDetailResDTO):
        sec_title_set = set([o.title for o in sea_d.sections.sections])
        sec_configs = self.Meta.get_season_config(
            sea_d.season.title).init_sections().sections
        #  if len(sec_configs) == 1:
        #  return
        for sec_conf in sec_configs:
            sec_title = sec_conf.title
            print(sec_title, sec_title_set)
            if sec_title not in sec_title_set:
                self.member_api.section_add(sea_d.season.id, sec_title)

        #  raise Exception()
        # 删除默认小节
        for sec in sea_d.sections.sections:
            if sec.title == '正片':
                self.member_api.section_del(sec.id)

    def section_move_ep_auto(
            self, section_id: int, season: dto.SeasonDetailResDTO = None):
        sec_res = self.member_api.get_section(section_id)
        if not season:
            season = self.member_api.get_season(sec_res.section.season_id)
        if not sec_res.episodes:
            return
        sea_conf = self.Meta.get_season_config(
            season.season.title).init_sections()
        sec_conf = sea_conf.get_section(sec_res.section.title)

        def is_the_section(ep, prefixs):
            for prefix in prefixs:
                if ep.title.startswith(prefix):
                    return True
            return False

        error_eps = []
        for ep in sec_res.episodes:
            is_right = sec_conf.has_episode(ep)
            if not is_right:
                error_eps.append(ep)

        for ep in error_eps:
            for sec in season.sections.sections:
                if sec.id == section_id:
                    continue
                sec_conf = sea_conf.get_section(sec.title)
                if sec_conf.has_episode(ep):
                    print(f"{ep.title} move to {sec.title}")
                    self.member_api.section_episode_move(sec.id, ep.id)
                    break

    def season_remove_error_state_ep(self, id: int):
        """删除合集异常稿件"""
        sea = self.member_api.get_season(id)
        items = []
        for sec in sea.sections.sections:
            sec_res = self.section_remove_error_state_ep(sec.id)
            item = {
                "title": sec.title,
                "data": sec_res
            }
            items.append(item)
        return items

    def section_remove_error_state_ep(self, section_id: int):
        """删除小节异常稿件"""
        sec_res = self.member_api.get_section(section_id)
        items = []
        for ep in sec_res.episodes:
            if ep.is_error_state:
                print(ep.archive_state, ep.title)
                arch: mod.ArcAuditModel = self.find_archive(ep.bvid)
                res = self.member_api.section_episode_del(ep.id)
                item = {
                    "bvid": arch.bvid,
                    "title": arch.title,
                    "result": res,
                }
                items.append(item)

        return items

    def season_format_auto(self, season_id: int = 0, title: str = ""):
        if title:
            sea_res = self.search_season(title)
        #  for sec in sea_res.sections.sections:
            #  self.section_remove_error_state_ep(sec.id)
        self.init_section(sea_res)
        sea_res = self.member_api.get_season(sea_res.season.id)
        for sec in sea_res.sections.sections:
            self.section_move_ep_auto(sec.id, sea_res)
        for sec in sea_res.sections.sections:
            self.section_ep_sort_edit_auto(sec.id)

    def get_daliy_income(self, days=7) -> List[mod.DaliyIncomModel]:
        res = self.api.get_daliy_income(days)
        for item in res.data:
            self.save(item)
        return res.data

    def add_section_videos(self, section_id: int, keywords: list):
        add_req = dto.SectionEpisodeAddReqDTO.default()
        add_req.section_id = section_id
        for kw in keywords:
            add_req.episodes = self.search_section_add_episodes(
                section_id, kw)
            if not add_req.episodes:
                continue
            self.member_api.section_add_episodes(add_req)

    def add_section_archive(self, section_id: int, keywords: list):
        '''将稿件添加到合集中'''
        add_req = dto.SectionEpisodeAddReqDTO.default()
        add_req.section_id = section_id
        for kw in keywords:
            add_req.episodes = self.search_section_add_episodes(
                section_id, kw)
            if not add_req.episodes:
                continue
            self.member_api.section_add_episodes(add_req)

    def auto_create_season(self, title) -> dto.SeasonDetailResDTO:
        sea_d = self.search_or_create_season(title)
        self.season_switch(sea_d.season)
        self.init_section(sea_d)
        sec_configs = self.Meta.get_season_config(
            sea_d.season.title).init_sections().sections

        sec_conf_map = {o.title: o for o in sec_configs}
        sea_d = self.member_api.get_season(sea_d.season.id)
        sections = sea_d.sections.sections
        sections.sort(key=lambda o: o.order, reverse=True)
        for sec in sections:
            sec_conf = sec_conf_map[sec.title]
            keywords = sec_conf.ep_prefixs
            keywords.sort(reverse=True)
            self.add_section_videos(sec.id, keywords)
            self.section_ep_sort_edit_auto(sec.id)

        sea_d = self.member_api.get_season(sea_d.season.id)
        print(sea_d.sections.sections)
        return sea_d

    def create_season_by_config(self, title: str) -> dto.SeasonDetailResDTO:
        sea_d = self.search_or_create_season(title)
        # 修改开关
        self.season_switch(sea_d.season)
        config = self.get_season_config(title)
        # 封装需要新建的小节
        need_create_sections = self.build_create_sections_by_config(config)

        # 添加不存在的小节
        for sec in need_create_sections:
            exist_sec = sea_d.get_section_by_title(sec.title)
            if not exist_sec:
                res = self.member_api.section_add(
                    sea_d.season.id, sec.title)
                if res.is_success:
                    sec.id = res.data
                time.sleep(1)

        # 删除没必要的小节
        sea_d = self.member_api.get_season(sea_d.season.id)
        for sec in sea_d.sections.sections:
            if not config.get_section(sec.title):
                time.sleep(1)
                print(f"delete sec {sec.title}")
                self.member_api.section_del(sec.id)

        # 删除小节没必要的视频
        sea_d = self.member_api.get_season(sea_d.season.id)
        for sec in sea_d.sections.sections:
            time.sleep(1)
            self.remove_section_episodes_by_config(config, sec.id)

        # 添加小节内的视频
        #  sea_d = self.member_api.get_season(sea_d.season.id)
        for sec in sea_d.sections.sections:
            time.sleep(1)
            self.add_section_episodes_by_config(config, sec.id)

        # 排序
        for sec in sea_d.sections.sections:
            time.sleep(1)
            self.auto_sort_section_ep(sec.id)
        return self.get_season(sea_d.season.id)

    def build_create_sections_by_config(
            self, config: str | SeasonConfig) -> List[SectionConfig]:
        """构建需要添加小节"""
        if isinstance(config, str):
            config = self.get_season_config(config)

        if config.type == SeasonType.EPISODE:
            config.init_sections()

        ep_arch_map = self.find_episode_archive_map_by_season_title(
            config.title)
        # 封装需要新建的小节
        need_create_sections = []
        for sec in config.sections:
            logger.info(f"{self.log_prefix()} need add section: {sec.title} arch count: {len(ep_arch_map)}")
            if not ep_arch_map:
                continue
            for ep_id in sec.episode_ids:
                arcs = ep_arch_map.pop(ep_id, [])
                if not arcs:
                    continue
                sec.archives.extend(arcs)
            if sec.archives:
                need_create_sections.append(sec)
        return need_create_sections

    def remove_section_episodes_by_config(self, sea_conf: SeasonConfig, sec_id):
        """删除不属于这个节点的视频"""
        sec_d = self.member_api.get_section(sec_id)
        sec_conf = sea_conf.get_section(sec_d.section.title)
        if not sec_conf:
            return
        if not sec_d.episodes:
            return
        epids = set(sec_conf.episode_ids)
        for ep in sec_d.episodes:
            part = sea_conf.match_archive_title(ep.title)
            #  part = utils.match_part(ep.title)
            if not part or part.episode_id not in epids:
                print(f"delete ep {sec_d.section.title} {ep.title}")
                self.member_api.section_episode_del(ep.id)

    def add_section_episodes_by_config(self, sea_conf: SeasonConfig, sec_id):
        sec_d = self.member_api.get_section(sec_id)
        sec_conf = sea_conf.get_section(sec_d.section.title)
        if not sec_conf:
            return
        epids = set([o.cid for o in sec_d.episodes]
                    ) if sec_d.episodes else set()
        add_req = dto.SectionEpisodeAddReqDTO.default()
        add_req.section_id = sec_id
        episodes = []
        for arc in sec_conf.archives:
            print(sec_conf.title,  '-' * 20)
            # 过滤已经存在的视频
            if arc.cid in epids:
                continue
            print(arc.title)
            episodes.append(arc.to_section_episode())
        add_req.episodes = episodes
        if not add_req.episodes:
            return
        print(f"add ep {sec_d.section.title} {episodes}")
        self.member_api.section_add_episodes(add_req)

    def section_ep_to_sort(
            self, sec: mod.SectionModel, ep: mod.SectionEpisodeModel
    ) -> dto.SectionEpisodeSortDTO:
        """排序episode的单个实例，可以重写"""
        order = 0
        season: mod.SeasonModel = self.find_by_id(
            sec.season_id, mod.SeasonModel)
        sea_conf = self.get_season_config(season.title)
        sec_conf = sea_conf.get_section(sec.title)
        if sec_conf.sort_type == SectionSortType.EPISODE_PART:
            part: mod.MatchPart = sea_conf.match_archive_title(ep.title)
            order = part.get_order()
        elif sec_conf.sort_type == SectionSortType.VIEW_COUNT:
            arch: mod.ArcAuditModel = self.find_archive(ep.bvid)
            order = 500 * 10000 - arch.view
        #  print(sea_conf.title, ep.title, sea_conf.archive_title_rexs)
        return dto.SectionEpisodeSortDTO(id=ep.id, sort=order)

    def get_archives(self, page: int = 1, pagesize: int = 10,
                     status=const.ARCHIVE_STATUS_ALL):
        req = dto.ArchiveListReqDTO.default()
        req.ps = pagesize
        req.pn = page
        req.status = status
        res = self.member_api.get_archives(req)
        if not res.arc_audits:
            return []
        items = []
        for arc in res.arc_audits:
            arc = self.resave_archive(arc)
            items.append(arc)
        logger.info(f"{self.log_prefix()} get_archives page: {page} status: {status} count: {len(items)}")
        return items

    def get_archive(
        self,
        url_or_bvid: str,
        is_save: bool = True,
    ) -> dto.ArchiveViewResDTO:
        bvid = url_or_bvid
        if url_or_bvid.startswith('https'):
            bvid = url_or_bvid.split('?')[0].split('/')[-1]
        logger.debug(f"get_archive by bvid: {bvid}")

        res: dto.ArchiveViewResDTO = self.member_api.get_archive_view(bvid)
        if res.is_success and is_save:
            self.resave_archive(res.arc_audit)
        return res

    def get_archive_info(
        self,
        url_or_bvid: str,
    ) -> dto.ArchiveInfoResDTO:
        bvid = url_or_bvid
        if url_or_bvid.startswith('https'):
            bvid = get_bvid_from_url(url_or_bvid)
        if not bvid:
            raise ValueError("bvid can not be None")
        logger.debug(f"get_archive by bvid: {bvid}")

        return self.api.get_archive_info(bvid=bvid)

    def get_player_url(
        self,
        bvid: str,
        cid: int,
        *,
        resolution: str = '1080p',
    ) -> dto.PlayerUrlResDTO:
        req = dto.PlayerUrlReqDTO(bvid=bvid, cid=cid)
        if resolution == '1080p':
            req.fnval = 4048
        return self.api.get_player_url(req)

    def resave_archive(self, arc: mod.ArcAuditModel) -> mod.ArcAuditModel:
        local_arc: mod.ArcAuditModel = self.find_by_id(
            arc.bvid, mod.ArcAuditModel)
        if local_arc:
            arc.ext = local_arc.ext
            if arc.stat.view == 0:
                arc.stat = local_arc.stat
            if not arc.videos:
                arc.videos = local_arc.videos
        self.save(arc)
        return arc

    def update_archive(self, r: dto.ArchiveEditDTO):
        view_res = self.get_archive(r.bvid)
        if not view_res.is_success:
            return view_res

        if not r.is_need_update():
            return dto.BaseResDTO.default_error("没有修改项")
        #  import json
        #  print(json.dumps(view_res.arc_audit.dict(), indent=4, ensure_ascii=False))
        req = dto.ArchiveEditReqDTO.from_archive(view_res.arc_audit)
        if r.title:
            req.title = r.title
            req.videos[0].title = r.title
        res = self.member_api.archive_edit(req)
        if res.is_success:
            return self.get_archive(r.bvid)
        #  print(json.dumps(req.dict(), indent=4, ensure_ascii=False))
        #  print(view_res.arc_audit.videos)
        return res

    def get_all_archives(self, status=const.ARCHIVE_STATUS_ALL,
                         total_page: int = -1):
        if total_page == -1:
            total_page = const.MAX_PAGE
        ps = 50
        for i in range(total_page):
            pn = i+1
            items = self.get_archives(page=pn, pagesize=ps, status=status)
            if not items:
                break
            yield from items

    def get_all_archives_gevent(self, status=const.ARCHIVE_STATUS_ALL,
                                total_page: int = -1):
        '''异步获取全部稿件（未完成）'''
        ps = 50

        def _get(page: int, status: str):
            items = self.get_archives(page=page, pagesize=ps, status=status)
            return {"page": page, "items": items}

        req = dto.ArchiveListReqDTO.default()
        req.status = status
        first_res = self.member_api.get_archives(req)
        if total_page == -1:
            total_page = first_res.page.count / ps
            total_page = total_page + 1 if total_page > int(total_page) else total_page
            total_page = int(total_page)
        print(total_page)

        jobs = []
        for i in range(total_page):
            pn = i + 1
            job = gevent.spawn(_get, page=pn, status=status)
            jobs.append(job)
        results = gevent.joinall(jobs)
        total_res = [o.value for o in results]
        total_res.sort(key=lambda o: o.get('page'))
        total_items = []
        for data in total_res:
            print(data.get('page'))
            items = data.get("items")
            total_items.extend(items)
        return total_items

    def refresh_archives(self, status=const.ARCHIVE_STATUS_ALL,
                         total_page: int = -1):
        try:
            exist_archive_ids = set()
            archives = list(self.get_all_archives(status=status, total_page=total_page))
            logger.debug(f"{self.log_prefix()} save archives {len(archives)}")
            if total_page == -1:
                # 删除已经删掉的视频
                exist_archive_ids = set([o.get_id() for o in archives])
                local_archives = self.find_items(MongoQuery.build(mod.ArcAuditModel))
                for item in local_archives:
                    if item.get_id() not in exist_archive_ids:
                        logger.info(f"{self.log_prefix()} delete_by_id {item.get_id()} {item.title}")
                        self.delete_by_id(item.get_id(), mod.ArcAuditModel)
            return len(archives)
        except Exception:
            logger.error(f"{self.log_prefix()} refresh_archives {traceback.format_exc()}")
            logger.error(f"{self.log_prefix()} refresh_archives {traceback.format_stack()}")
            return 0

    def get_replys(self, page: int = 0, pagesize: int = 10) -> dto.ReplyListResDTO:
        req = dto.ReplyListReqDTO.default()
        req.ps = pagesize
        req.pn = page
        res = self.api.get_replys(req)
        #  items = []
        for reply in res.list:
            self.save(reply)
        return res

    def reply_top(self, rpid: int, action: int) -> dto.BaseResDTO:
        item: mod.ReplyModel = self.find_by_id(str(rpid), mod.ReplyModel)
        req = dto.ReplyLikeReqDTO.default()
        req.rpid = item.rpid
        req.oid = item.oid
        req.type = item.type
        req.action = action
        res = self.api.reply_top(req)
        if res.is_success:
            item.reply_control.is_top = True if action else False
            self.save(item)
        return res

    def reply_like(self, rpid: int, action: int) -> dto.BaseResDTO:
        item: mod.ReplyModel = self.find_by_id(str(rpid), mod.ReplyModel)
        req = dto.ReplyLikeReqDTO.default()
        req.rpid = item.rpid
        req.oid = item.oid
        req.type = item.type
        req.action = action
        res = self.api.reply_like(req)
        if res.is_success:
            item.action = action
            item.reply_control.up_like = True if action else False
            item.up_action.like = item.reply_control.up_like
            self.save(item)
        return res

    def reply_add(self, oid: int, message: str, rpid: int = 0) -> dto.ReplyAddResDTO:
        req = dto.ReplyAddReqDTO.default()
        req.oid = oid
        item: mod.ReplyModel = None
        if rpid:
            item: mod.ReplyModel = self.find_by_id(rpid, mod.ReplyModel)
            req.type = item.type
            req.parent = item.rpid
            req.root = item.root if item.root else item.rpid
        req.message = message
        if req.parent != req.root:
            req.message = f"回复 @{item.member.uname} :{message}"
        res = self.api.reply_add(req)
        if res.is_success:
            self.save(res.reply)
            if item:
                item.up_action.reply = True
                self.save(item)
        else:
            if res.code == 12022:
                self.delete_by_id(rpid, mod.ReplyModel)
        return res

    def reply_del(self, rpid: int) -> dto.ReplyAddResDTO:
        item: mod.ReplyModel = self.find_by_id(str(rpid), mod.ReplyModel)
        req = dto.ReplyDelReqDTO.default()
        req.rpid = item.rpid
        req.oid = item.oid
        req.type = item.type
        res = self.api.reply_del(req)
        if res.is_success:
            self.delete_by_id(rpid, mod.ReplyModel)
        return res

    def send_archive_downline_message(self, arc: mod.ArcAuditModel
                                      ) -> dto.BaseResDTO:
        #  text = f"视频下线通知\n用户：{self.Meta.NAME}\n"
        text = f"""
        视频下线通知
        > 用户：<font color=\"comment\">{self.Meta.NAME}</font>\n
        > 视频：<font color=\"comment\">{arc.title}</font>\n
        """
        res = self.qy_api.send_webhook(
            dto.QYWebhookSendReqDTO.build_markdown(text))
        if res.is_success:
            arc.ext.is_send_downline = True
            self.save(arc)
        return res

    def batch_send_archive_downline_message(self):
        res = self.find_page_items(
            MongoQuery.build(mod.ArcAuditModel).eq('state', -4))
        arc: mod.ArcAuditModel
        count = 0
        for arc in res.data:
            if arc.ext.is_send_downline:
                continue
            res = self.send_archive_downline_message(arc)
            print(res)
            if res.is_success:
                count += 1
        print(f"{self.Meta.NAME} count: {count}")
        return count
        #  break

    def refresh_archives_by_season_title(self, season_title):
        import time
        query_res = self.find_archives(season_title_eq=season_title)
        arc: mod.ArcAuditModel
        count = 0
        for arc in query_res.data:
            if arc.is_update:
                count += 1
                res = self.get_archive(arc.bvid)
                arc = res.arc_audit
                print(arc.get_id(), arc.archive.state, arc.title)
                time.sleep(1)
        print(count)

    def submit_archive_card(
        self, arc: Union[str, mod.ArcAuditModel], history_id: str = ""
    ) -> dto.BaseResDTO:
        if isinstance(arc, str):
            arc = self.find_archive(arc)
        req = dto.CardSubmitReqDTO.default()
        req.aid = arc.aid
        req.cid = arc.cid
        if not history_id:
            history_id = arc.ext.history_id
        if not history_id:
            raise Exception("history_id can not be None")
        history: mod.HistoryModel = mod.HistoryModel.find_by_id(history_id)
        req.cards = history.cards
        return self.member_api.card_submit(req)

    def get_allcards(self, arch: Union[str, mod.ArcAuditModel]
                     ) -> dto.AllCardsResDTO:
        if isinstance(arch, str):
            arch: mod.ArcAuditModel = self.find_archive(arch)

        return self.member_api.allcards(arch.aid, arch.cid)

    def login_by_qrcode(self):
        qrcode_res = self.passport_api.qrcode_generate()
        create_qrcode(qrcode_res.url)
        is_success = False
        poll_res: dto.QRCodePollResDTO = None
        while not is_success:
            poll_res = self.passport_api.qrcode_poll(qrcode_res.qrcode_key)
            logger.info(f"等待扫描结果 code: {poll_res.code} message: {poll_res.message}")
            if poll_res.code == 0:
                is_success = True
            time.sleep(2)

        if poll_res.code != 0:
            return

        cookies = dict(poll_res.response.cookies)
        cookie = mod.AuthCooke(**cookies)
        return self.login_by_cookie(cookie, poll_res.refresh_token, poll_res.timestamp / 1000)

    def login_by_cookie(self, cookie: AuthUser, refresh_token: str, login_timestamp: float):
        auth = mod.AuthUser(cookies=cookie)
        auth.mid = int(cookie.dede_user_id)
        auth.refresh_token = refresh_token
        auth.login_time = datetime.fromtimestamp(login_timestamp)
        auth.save()
        self.auth = auth
        self.load_api(auth)
        self.refresh_auth()
        logger.info(f"登录成功: {self.auth.name}({self.auth.mid})")
        return self.auth

    def login_by_biliup(self):
        '''使用 biliup 命令登录'''
        temp_cookies_file = os.path.join(const.CONFIG_DIR, f"cookies-{time.time()}.json")
        cmds = [
            const.BILIUP_PATH,
            "-u", temp_cookies_file,
            "login"
        ]
        logger.debug(f"登录命令: {' '.join(cmds)}")
        subprocess.run(cmds)

        # 解析 cookie 地址
        with open(temp_cookies_file, 'r') as f:
            lines = f.readlines()
            data = json.loads(''.join(lines))

        biliup_auth = mod.BiliUPAuth(**data)
        cookie = mod.AuthCooke(**biliup_auth.cookie_map)
        auth = self.login_by_cookie(
                cookie,
                refresh_token=biliup_auth.token_info.refresh_token,
                login_timestamp=datetime.now().timestamp()
            )

        # 迁移配置文件
        shutil.move(temp_cookies_file, os.path.join(const.CONFIG_DIR, f"{auth.bili_name}-cookies.json"))
        return auth

    def refresh_auth(self):
        mid = self.auth.mid
        auth = AuthUser.find_by_id(mid)

        nav_res = self.api.get_web_inferface_nav()
        auth.name = nav_res.name
        auth.face = nav_res.face
        auth.money = nav_res.money
        auth.wbi = nav_res.wbi
        auth.refresh_time = datetime.now()
        auth.save()
        self.auth = auth
        self.load_api(auth)
        self.get_user_info(mid)

    def get_user_info(self, mid: int) -> mod.User:
        res = self.api.get_acc_info(mid)
        user = mod.User(**res.data)
        user.ext.is_followed[self.auth.get_id()] = res.is_followed
        user.save()
        return user

    def add_archive_to_season(
            self, arch: Union[str, mod.ArcAuditModel],
            season_id: int, *, section_id: int = 0):
        '''将稿件添加到合集中'''
        if isinstance(arch, str):
            arch = self.find_by_id(arch, mod.ArcAuditModel)
        if not section_id:
            season = self.find_by_id(season_id, mod.SeasonModel)
            section_id = season.sections[-1].id
        logger.debug(f"add_archive_to_season {arch.bvid} => season: {season_id} / section: {section_id}")
        req = dto.SectionEpisodeAddReqDTO()
        req.section_id = section_id
        ep = arch.to_section_episode()
        req.episodes.append(ep)
        #  logger.info(f"{self.log_prefix()} section add episodes req: {req}")
        return self.member_api.section_add_episodes(req)

    def pre_upload(self, req: dto.ArchiveUploadReqDTO, *, bash_path: str = None, with_to_season: bool = True):
        '''
        https://github.com/biliup/biliup-rs
        上传视频

Usage: biliup upload [OPTIONS] [VIDEO_PATH]...

Arguments:
  [VIDEO_PATH]...  需要上传的视频路径,若指定配置文件投稿不需要此参数

Options:
      --submit <SUBMIT>            提交接口 [default: client] [possible values: client, app, web]
  -c, --config <FILE>              Sets a custom config file
  -l, --line <LINE>                选择上传线路 [possible values: bda2, ws, qn, bldsa, tx, txa, bda]
      --limit <LIMIT>              单视频文件最大并发数 [default: 3]
      --copyright <COPYRIGHT>      是否转载, 1-自制 2-转载 [default: 1]
      --source <SOURCE>            转载来源 [default: ]
      --tid <TID>                  投稿分区 [default: 171]
      --cover <COVER>              视频封面 [default: ]
      --title <TITLE>              视频标题 [default: ]
      --desc <DESC>                视频简介 [default: ]
      --dynamic <DYNAMIC>          空间动态 [default: ]
      --tag <TAG>                  视频标签，逗号分隔多个tag [default: ]
      --dtime <DTIME>              延时发布时间，距离提交大于4小时，格式为10位时间戳
      --interactive <INTERACTIVE>  [default: 0]
      --mission-id <MISSION_ID>
      --dolby <DOLBY>              是否开启杜比音效, 0-关闭 1-开启 [default: 0]
      --hires <LOSSLESS_MUSIC>     是否开启 Hi-Res, 0-关闭 1-开启 [default: 0]
      --no-reprint <NO_REPRINT>    0-允许转载，1-禁止转载 [default: 0]
      --open-elec <OPEN_ELEC>      是否开启充电, 0-关闭 1-开启 [default: 0]
      --up-selection-reply         是否开启精选评论，仅提交接口为app时可用
      --up-close-reply             是否关闭评论，仅提交接口为app时可用
      --up-close-danmu             是否关闭弹幕，仅提交接口为app时可用
  -h, --help                       Print help
        '''

        bili_name = self.auth.bili_name
        mid = self.auth.mid
        cmds = [os.path.join(const.BIN_DIR, 'biliup'),
                '-u', os.path.join(const.CONFIG_DIR, f'{bili_name}-cookies.json'),
                'upload',
                ]
        cmds.extend(req.to_command_params())
        cmd = ' '.join(cmds)
        logger.info(f"upload cmd: {cmd}")
        bash_dir = os.path.join(const.CACHE_DIR, 'bin')
        try:
            os.makedirs(bash_dir)
        except Exception:
            pass
        now = datetime.today().timestamp()
        if not bash_path:
            bash_path = os.path.join(bash_dir, f"upload_{bili_name}_{req.title}_{now}.sh")
        season_refresh_cmd = const.SEASON_REFRESH_CMD.format(mid=mid)
        archive_refresh_cmd = const.ACHIVE_REFRESH_ONE_CMD.format(title=req.title, mid=mid)
        refresh_ext_cmd = const.ARCHIVE_REFRESH_EXT_CMD.format(title=req.title, mid=mid)
        to_season_cmd = const.ARCHIVE_TO_SEASON_CMD.format(title=req.title, mid=mid)
        sleep_s = 10
        to_season_all_cmd = f'''echo '等待 {sleep_s} 秒钟添加到合集'
sleep {sleep_s}
{season_refresh_cmd}
{archive_refresh_cmd}
{refresh_ext_cmd}
{to_season_cmd}

        '''
        with open(bash_path, 'a') as f:
            f.write(f"{cmd}\n\n")
            if with_to_season:
                f.write(to_season_all_cmd)
        os.chmod(bash_path, 0o755)
        logger.debug(f"cmd write to {bash_path}")
        if with_to_season:
            print("")
            print("查看生成脚本:")
            subprocess.run(['cat', bash_path])
            print("脚本地址如下:")
            print("")
            print(bash_path)
            print("")
