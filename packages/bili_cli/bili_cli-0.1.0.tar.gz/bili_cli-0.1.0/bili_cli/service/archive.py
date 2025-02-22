#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from typing import List
from wpy import Singleton
from rich import print
from bili_cli import const
from bili_cli.base import (
    QueryResult, MongoQuery
)
from bili_cli.mod import (
    AuthUser,
)
from bili_cli.mod.arc_auait import ArcAuditModel, ArcVideoModel
from bili_cli.common import crud
from bili_cli.common.bilibili import BiliBiliClient
from bilibili_sdk import MemberClient
from bilibili_sdk.dto import GetArchiveListReq
from bilibili_sdk.dto.archive import ArcAudit


class ArchiveService(Singleton):
    def __init__(self):
        self.crud_archive = crud.archive
        self.bilibili_client = BiliBiliClient()

    def get_member_client(self, mid) -> MemberClient:
        cookies = self.get_cookies(mid)
        client = MemberClient.default()
        client.set_cookies(cookies)
        return client

    def get_cookies(self, mid) -> dict:
        user = AuthUser.find_by_id(mid)
        return user.cookies.dict()

    async def refresh_archives(
        self,
        mid: int,
        *,
        refresh_page: int = const.MAX_PAGE,
        page_size: int = 50,
    ):
        '''刷新稿件'''
        async def save(res):
            for arc in res.data.arc_audits:
                data = arc.dict(by_alias=True)
                arc_model = ArcAuditModel(mid=mid, **data)
                await arc_model.save()

        client = self.get_member_client(mid)

        ps = page_size
        req = GetArchiveListReq(ps=ps)
        res = await client.get_archive_list(req)
        print(f"请求数据: {req}")
        await save(res)

        if refresh_page <= 1:
            # 刷新视频列表
            await self.refresh_archive_videos(mid, res.data.arc_audits)
            return

        class_ = res.data.class_
        total = class_.is_pubing + class_.pubed + class_.not_pubed
        total_page = int(total / ps) + 1
        print(f"视频总数: {total} 总页数: {total_page}")

        for pn in range(2, total_page + 1):
            req.pn = pn
            print(f"请求数据: {req}")
            res = await client.get_archive_list(req)
            await save(res)

            if pn >= refresh_page:
                return

    async def refresh_archive_videos(self, mid, audits: List[ArcAudit]):
        '''刷新稿件视频列表'''
        client = self.get_member_client(mid)

        for arc in audits:
            res = await client.get_archive_videos(arc.archive.aid)
            data = res.data.dict(by_alias=True)
            m = ArcVideoModel(mid=mid, **data)
            print(f"Video: {arc.archive.bvid} videos: {len(m.videos)}")
            await m.save()

    async def find_archives(
        self, mid: int, title_eq="", title_like="", season_title_eq="",
        state: int = -1, sort: str = "-ptime", episode_id: str = "",
        state_in: list = [], album_id: str = "",
        page=1, pagesize=const.MAX_PAGESIZE,
    ) -> QueryResult:
        query = MongoQuery.build(ArcAuditModel).page(page).pagesize(pagesize)
        query.eq('mid', mid)
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
        query_res = await ArcAuditModel.find_page_items(query)

        # 获取视频列表
        for audit in query_res.data:
            arc_video = await ArcVideoModel.find_by_id(audit.get_id())
            audit.videos = arc_video.videos

        return query_res

    async def find_archive(
        self, bvid,
    ) -> ArcAuditModel:
        item = await ArcAuditModel.find_by_id(bvid)
        arc_video = await ArcVideoModel.find_by_id(bvid)
        item.videos = arc_video.videos
        return item
