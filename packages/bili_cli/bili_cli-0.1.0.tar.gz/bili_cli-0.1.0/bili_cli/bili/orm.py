#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from pydantic import Field
from collections import defaultdict
from typing import Dict, List, Union, Optional
from bili_cli.base import (
    Query, QueryResult, BaseMongoDB, MongoQuery
)
from bili_cli import mod, const


class BiliORM(BaseMongoDB):
    auth: mod.AuthUser = Field(None)

    class Meta(BaseMongoDB.Meta):
        NAME: str
        DB: str

    def find_episode_archive_map_by_season_title(
            self, title) -> Dict[str, List[mod.ArcAuditModel]]:
        arc: mod.ArcAuditModel
        queryRes = self.find(
            Query.build(mod.ArcAuditModel).eq('season_title', title))
        res = defaultdict(list)
        for arc in queryRes.data:
            if not arc.is_open:
                continue
            res[arc.ext.episode_id].append(arc)
        return res

    def find_season(self, id_or_title: Union[int, str]) -> mod.SeasonModel:
        item = mod.SeasonModel.find_by_id(id_or_title)
        if item:
            return item

        q = (
            MongoQuery.build(mod.SeasonModel)
            .pagesize(10)
            .eq('mid', self.auth.mid)
            .eq('title', id_or_title)
        )
        items = self.find_page_items(q).data
        if items:
            return items[0]
        return None

    def find_archive(self, id_or_title: str) -> mod.ArcAuditModel:
        item = self.find_by_id(id_or_title, mod.ArcAuditModel)
        if not item:
            items = self.find_archives(title_eq=id_or_title, pagesize=1).data
            if items:
                item = items[0]
        return item

    def find_archives_old(
        self, title_eq="", title_like="", season_title_eq="",
        state: int = -1, sort: str = "-ptime", episode_id: str = "",
        state_in: list = [], album_id: str = "",
        page=1, pagesize=const.MAX_PAGESIZE,
    ) -> QueryResult:
        q = Query.build(mod.ArcAuditModel).pagesize(pagesize).page(page)
        if title_eq:
            q.eq('title', title_eq)
        if title_like:
            q.like('title', title_like)
        if season_title_eq:
            q.eq('season_title', season_title_eq)
        if episode_id:
            q.eq('episode_id', episode_id)
        if album_id:
            q.eq('album_id', album_id)
        if state != -1:
            q.eq('state', state)
        if state_in:
            q.in_('state', state_in)
        if sort:
            sort_type = sort[0:1]
            if sort_type == '+':
                sort_type = 'asc'
            else:
                sort_type = 'desc'
            q.sort(sort[1:], sort_type)
        res = self.find(q)
        return res

    def find_archives(
        self, title_eq="", title_like="", season_title_eq="",
        state: int = -1, sort: str = "-ptime", episode_id: str = "",
        state_in: list = [], album_id: str = "",
        page=1, pagesize=const.MAX_PAGESIZE,
    ) -> QueryResult:
        query = MongoQuery.build(mod.ArcAuditModel).page(page).pagesize(pagesize)
        if title_eq:
            query.eq('Archive.title', title_eq)
        if title_like:
            query.like('Archive.title', title_like)
        if season_title_eq:
            query.eq('ext.season_title', season_title_eq)
        if episode_id:
            query.eq('ext.episode_id', episode_id)
        if album_id:
            query.eq('ext.album_id', album_id)
        if state != -1:
            query.eq('Archive.state', state)
        if state_in:
            query.in_('Archive.state', state_in)
        if sort:
            if sort.endswith('ptime'):
                sort = sort.replace('ptime', 'Archive.ptime')
            if sort.endswith('view'):
                sort = sort.replace('view', 'stat.view')
            query.sort(sort)
        return self.find_page_items(query)

    def find_normal_archives(self) -> QueryResult:
        return self.find_archives(state_in=[0, -40])

    def find_replys(self, message_like: str = "", is_up_like: Optional[int] = None,
                    sort: str = "-ctime", page: int = 1, pagesize=const.MAX_PAGESIZE):
        q = MongoQuery.build(mod.ReplyModel).pagesize(pagesize).page(page)
        if message_like:
            q.like('Content.message', message_like)
        if is_up_like is not None:
            q.eq('action', int(is_up_like))

        if sort:
            q.sort(sort)
        return self.find_page_items(q)

    def find_incomes(
        self,
        *,
        sort: str = "-date",
        page: int = 1,
        pagesize=10,
    ):
        q = (
            MongoQuery
            .build(mod.DaliyIncomModel)
            .sort(sort)
            .pagesize(pagesize)
            .page(page)
        )
        return self.find_page_items(q)

    def find_split_episode_last_archives(
            self, album_id, episode_id) -> Dict[int, mod.ArcAuditModel]:
        query = MongoQuery.build(mod.ArcAuditModel)
        query.eq('ext.episode_id', episode_id)
        query.eq('ext.album_id', album_id)
        query.sort('Archive.ptime', 'desc')

        arc: mod.ArcAuditModel
        data = {}
        for arc in self.find_items(query):
            p = arc.ext.part
            if p in data:
                continue
            data[p] = arc
        return data
