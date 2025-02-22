#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from pydantic import Field
from .base import BaseORM


class Archive(BaseORM):
    class Meta(BaseORM.Meta):
        TABLE = "archive"

    # archive
    aid: int = Field(title="视频id")
    bvid: str = Field(title="视频id")
    cid: int = Field(0, title="p1 id")
    title: str = Field("", title="标题")
    cover: str = Field("", title="封面")
    tag: str = Field("", title="标签")
    desc: str = Field("", title="描述")
    state: int = Field(
        0, title="状态", description="0 开发浏览 -4 已锁定 -30 审核中、-40 审核通过，等待发布")
    state_desc: str = Field("", title="状态描述")
    reject_reason: str = Field("", title="锁定原因")
    duration: int = Field(0, title="时长")
    ctime: int = Field(0, title="")
    ptime: int = Field(0, title="")
    dtime: int = Field(0, title="")
    # state
    view: int = Field(0, title="播放")
    danmaku: int = Field(0, title="弹幕")
    reply: int = Field(0, title="回复")
    favorite: int = Field(0, title="收藏")
    coin: int = Field(0, title="硬币")
    share: int = Field(0, title="分享")
    like: int = Field(0, title="点赞")
    # ext
    online: str = Field("", title="在线播放")
    season_title: str | None = Field("", title="合集标题")
    season_id: int = Field(0, title="合集id")
    part: int = Field(0, title="剧集片段")
    album_id: str = Field("", title="专辑id")
    episode_id: str = Field("", title="剧集id")
    is_send_downline: bool = Field(False, title="是否发送下线消息")
    history_id: str = Field("", title="记录id")
