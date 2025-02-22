#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from datetime import datetime
from rich import print
from typing import List
from pydantic import Field
from bili_cli.base import AsyncCommonORM
from bilibili_sdk.dto.archive import ArcAudit, ArchiveVideoListData, Video
from bilibili_sdk.enums.archive import ArchiveState


class ArcAuditModel(AsyncCommonORM, ArcAudit):
    mid: int = Field(title="用户id")
    online: str = Field("", title="在线播放")
    videos: List[Video] = Field([], title='视频列表')

    class Meta(AsyncCommonORM.Meta):
        TABLE = "arc_audit"

    def get_id(self):
        if self.id:
            return self.id
        return self.archive.bvid

    @classmethod
    def table_headers(cls) -> List[str]:
        return ['bvid', '标题', 'P数', '播放', '在线', '点赞', '合集', '剧集', '状态', '发布时间', '上传时间']

    def table_line(self) -> List[str]:
        like_rate = 0
        if self.view > 0:
            like_rate = self.stat.like / self.view
        ptime = self.archive.ptime
        if self.archive.dtime:
            ptime = self.archive.dtime
        state_desc = self.archive.state_desc
        if self.state == ArchiveState.WAITING:
            state_desc = '预发布'
        elif self.state == ArchiveState.OPEN:
            state_desc = '已发布'
        return [
            self.bvid, self.title,
            f"{len(self.videos)}",
            self.view, self.online,
            f"{self.stat.like} ({like_rate:.2f})",
            "",
            "",
            #  f"{self.season_title}({self.season_id})",
            #  f"{self.ext.album_id}-{self.ext.episode_id}.{self.ext.part}",
            f"{state_desc} {self.state}",
            f"{datetime.fromtimestamp(ptime or 0)}",
            f"{datetime.fromtimestamp(self.archive.ctime)}"
        ]

    def pprint(self):
        print(f"title: {self.archive.title}")
        print(f"state: {self.archive.state_desc} {self.state}")

        for video in self.videos:
            print(video)

    @property
    def aid(self) -> int:
        return self.archive.aid if self.archive else 0

    @property
    def bvid(self) -> str:
        return self.archive.bvid

    @property
    def title(self) -> str:
        return self.archive.title

    @property
    def state(self) -> str:
        return self.archive.state

    @property
    def view(self) -> int:
        return self.stat.view

    @property
    def ptime(self) -> int:
        if self.archive:
            return self.archive.ptime
        return 0


class ArcVideoModel(AsyncCommonORM, ArchiveVideoListData):
    mid: int = Field(title="用户id")

    class Meta(AsyncCommonORM.Meta):
        TABLE = "arc_video"

    def get_id(self):
        if self.id:
            return self.id
        return self.archive.bvid
