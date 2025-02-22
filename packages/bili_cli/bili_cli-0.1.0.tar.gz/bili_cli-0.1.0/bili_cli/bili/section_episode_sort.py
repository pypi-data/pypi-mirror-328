#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import pydantic
from typing import List, Callable
from bili_cli.base import BaseModel
from bili_cli.api import MemberApi, Api
from bili_cli import dtos as dto, mod


class SectionEpisodeSort(BaseModel):

    member_api: MemberApi = pydantic.Field(None)
    api: Api = pydantic.Field(None)

    def section_episode_to_sort_dto_auto(
            self, ep: mod.SectionEpisodeModel) -> dto.SectionEpisodeSortDTO:
        """默认使用时间"""
        return dto.SectionEpisodeSortDTO(id=ep.id, sort=ep.cid)

    def section_episodes_to_sort_dtos_auto(
        self, episodes: List[mod.SectionEpisodeModel]
    ) -> List[dto.SectionEpisodeSortDTO]:
        """合集分段自动排序规则"""
        return self.episodes_sort_first_hot_second_new(episodes)

    def episodes_sort_first_hot_second_new(
        self, episodes: List[mod.SectionEpisodeModel]
    ) -> List[dto.SectionEpisodeSortDTO]:
        sorts = []
        data = []
        is_pubing_eps = []
        for ep in episodes:
            if ep.archive_state == -40:
                print(ep.cid, ep.id, ep.archive_state, ep.title)
                is_pubing_eps.append(ep)
                continue
            #  online = 0
            if ep.archive_state == 0:
                online_res = self.api.get_online(ep.cid, aid=ep.aid)
                ep.online = online_res.online
            print(ep.online, ep.cid, ep.id, ep.archive_state, ep.title)
            data.append(ep)
        # 未发布的放在最前面
        for i, ep in enumerate(is_pubing_eps):
            sorts.append(dto.SectionEpisodeSortDTO(id=ep.id, sort=i))
        # 播放最高的其次
        data.sort(key=lambda o: o.online, reverse=True)
        sorts.append(dto.SectionEpisodeSortDTO(
            id=data[0].id, sort=len(sorts) + 1))
        # 然后是最新发布的
        data = data[1:]
        data.sort(key=lambda o: o.cid, reverse=True)
        sorts.append(dto.SectionEpisodeSortDTO(
            id=data[0].id, sort=len(sorts)+1))
        # 最后按照在线数量排序
        data = data[1:]
        data.sort(key=lambda o: o.online, reverse=True)

        now_sort_count = len(sorts)
        for i, ep in enumerate(data):
            sorts.append(dto.SectionEpisodeSortDTO(
                id=ep.id, sort=i+now_sort_count+1))

        for s in sorts:
            print(s)

        print(len(episodes), len(sorts))
        #  raise Exception()
        return sorts

    def section_ep_sort_edit_auto(self, section_id: int):
        sec_res = self.member_api.get_section(section_id)
        if not sec_res.episodes:
            return

        #  print(sec_res.episodes)
        sorts = self.section_episodes_to_sort_dtos_auto(sec_res.episodes)
        sorts.sort(key=lambda o: o.sort)
        for i, s in enumerate(sorts):
            s.sort = i + 1

        edit_req = dto.SectionEditReqDTO.default()
        edit_req.section = sec_res.section
        edit_req.sorts = sorts

        self.member_api.section_edit(edit_req)

    def season_ep_sort_auto(self, id: int):
        sea_res = self.member_api.get_season(id)
        for sec in sea_res.sections.sections:
            self.auto_sort_section_ep(sec.id)
            #  self.section_ep_sort_edit_auto(sec.id)

    def section_ep_sort_edit(
        self, section_id: int,
        to_sort_func: Callable[[mod.SectionModel, mod.SectionEpisodeModel],
                               dto.SectionEpisodeSortDTO]
    ) -> dto.BaseResDTO:
        sec_res = self.member_api.get_section(section_id)
        if not sec_res.episodes:
            return

        sorts = []
        for ep in sec_res.episodes:
            s = to_sort_func(sec_res.section, ep)
            print(s)
            sorts.append(s)
        sorts.sort(key=lambda o: o.sort)
        for i, s in enumerate(sorts):
            s.sort = i + 1

        edit_req = dto.SectionEditReqDTO.default()
        edit_req.section = sec_res.section
        edit_req.sorts = sorts

        return self.member_api.section_edit(edit_req)

    def section_ep_to_sort(
            self, sec: mod.SectionModel, ep: mod.SectionEpisodeModel
    ) -> dto.SectionEpisodeSortDTO:
        pass

    def auto_sort_section_ep(self, section_id: int):
        return self.section_ep_sort_edit(section_id, self.section_ep_to_sort)
