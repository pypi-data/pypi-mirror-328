#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from pydantic import Field, model_validator
from datetime import datetime
from typing import List
from bili_cli.base import BaseMongoORM, BaseModel

STATE_OPEN = 0
STATE_LOCK = -4
STATE_UPDATE = -6
STATE_AUDIT = -30
STATE_WAITING = -40  # 预发布

STATE_OPEN_SET = set([
    STATE_OPEN, STATE_UPDATE, STATE_AUDIT, STATE_WAITING
])

STATE_LOCK_SET = set([
    STATE_LOCK
])


class SectionEpisodeModel(BaseModel):
    id: int = Field(0)
    title: str = Field(title='在合集中的标题')
    aid: int = Field()
    cid: int = Field()
    bvid: str = Field("")
    season_id: int = Field(0, title='合集id', alias='seasonId')
    section_id: int = Field(0, title='小节id', alias='sectionId')
    order: int = Field(0)
    online: int = Field(0)
    archive_state: int = Field(
        0, alias='archiveState',
        description='-4 p1-版权原因 -2 P1 增加时间段信息 -30 审核中')

    @property
    def is_error_state(self) -> bool:
        """The is_error_state property."""
        return self.archive_state == STATE_LOCK

    @classmethod
    def table_headers(cls) -> List[str]:
        return ['bvid', 'title', 'cid', 'archive_state']


class VideoModel(BaseModel):
    cid: int = Field(0, title="p1 id")
    title: str = Field("", title="标题")
    filename: str = Field("", title="猜测是md5")
    desc: str = Field("", title="描述")
    index: int = Field(0, title="")
    duraction: int = Field(0, title="时长")


class ArchiveExt(BaseModel):
    season_title: str | None = Field("", title="合集标题")
    season_id: int = Field(0, title="合集id")
    cid: int = Field(0, title="p1 id")
    part: int = Field(0, title="剧集片段")
    album_id: str = Field("", title="专辑id")
    episode_id: str = Field("", title="剧集id")
    is_send_downline: bool = Field(False, title="是否发送下线消息")
    history_id: str = Field("", title="记录id")
    #  has_card: bool = Field(False, title="是否有导航")


class AuditStat(BaseModel):
    view: int = Field(0, title="播放")
    danmaku: int = Field(0, title="弹幕")
    reply: int = Field(0, title="回复")
    favorite: int = Field(0, title="收藏")
    coin: int = Field(0, title="硬币")
    share: int = Field(0, title="分享")
    like: int = Field(0, title="点赞")


class AuditSubtitle(BaseModel):
    allow: bool = Field(False, title="")
    lan: str = Field("", title="")
    lan_doc: str = Field("", title="")
    #  draft_list: list = Field(None, title="")


class ArchiveRecreate(BaseModel):
    auth: int = Field(0, title="")
    editable: int = Field(0, title="")
    switch: int = Field(0, title="")


class ArchiveModel(BaseModel):
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
    copyright: int = Field(0, title="版权保护")
    tid: int = Field(0, title="分区id")
    topic_id: int = Field(0, title="话题id")
    mission_id: int = Field(0, title="活动id")
    receate: ArchiveRecreate = Field(ArchiveRecreate(), title="修改权限")
    dynamic: str = Field("", title="")
    interactive: int = Field(0, title="")
    no_reprint: int = Field(0, title="")
    is_360: int = Field(0, title="是否为360")
    ctime: int = Field(0, title="")
    ptime: int = Field(0, title="")
    dtime: int = Field(0, title="")
    #  online: int = Field(0, title="在线总数", description="大概数")
    #  total_income: int = Field(0, title="总收入")
    #  income_upload_time: datetime = Field(None, title="收入更新时间")
    publish_time: datetime = Field(None, title="发布时间")
    subscribe_time: datetime = Field(None, title="预约发布时间")
    #  publish_days: int = Field(0, title="发布天数")

    @model_validator(mode='before')
    def validator_all(cls, values):
        values['publish_time'] = datetime.fromtimestamp(
            values.get("ptime") or 0)
        values['subscribe_time'] = datetime.fromtimestamp(
            values.get("dtime") or 0)
        return values

    @property
    def create_time(self) -> datetime:
        return datetime.fromtimestamp(self.ctime)


class ArcAuditModel(BaseMongoORM):
    archive: ArchiveModel = Field(None, title="文档信息", alias="Archive")
    videos: List[VideoModel] = Field([], title="视频列表")
    act_reserve_create: bool = Field(False, title="")
    stat: AuditStat = Field(AuditStat())
    online: str = Field("", title="在线播放")
    ext: ArchiveExt = Field(ArchiveExt(), title="扩展数据")
    subtitle: AuditSubtitle = Field(AuditSubtitle(), title="")

    class Meta():
        TABLE = "arc_audit"

    def get_id(self):
        if self.id:
            return self.id
        return self.archive.bvid

    @classmethod
    def table_headers(cls) -> List[str]:
        return ['bvid', '标题', '播放', '在线', '点赞', '合集', '剧集', '状态', '发布时间', '上传时间']

    def table_line(self) -> List[str]:
        like_rate = 0
        if self.view > 0:
            like_rate = self.stat.like / self.view
        ptime = self.archive.publish_time
        if self.archive.dtime:
            ptime = self.archive.subscribe_time
        #  view = f"{self.view} ({self.online})"
        state_desc = self.archive.state_desc
        if self.is_pre_release:
            state_desc = '预发布'
        return [
            self.bvid, self.title, self.view, self.online,
            f"{self.stat.like} ({like_rate:.2f})",
            f"{self.season_title}({self.season_id})",
            f"{self.ext.album_id}-{self.ext.episode_id}.{self.ext.part}",
            f"{self.state} {state_desc}",
            f"{ptime}",
            f"{self.archive.create_time}"
        ]

    @property
    def cid(self) -> int:
        return self.ext.cid if self.ext else 0

    @property
    def episode_id(self) -> str:
        return self.ext.episode_id

    @property
    def album_id(self) -> str:
        return self.ext.album_id

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

    @property
    def is_open(self):
        """The foo property."""
        return self.archive.state in STATE_OPEN_SET

    @property
    def is_publish(self):
        """The foo property."""
        return self.archive.state == STATE_OPEN

    @property
    def is_pre_release(self):
        """The foo property."""
        return self.archive.state == STATE_WAITING

    @property
    def is_lock(self):
        """The foo property."""
        return self.archive.state in STATE_LOCK_SET

    @property
    def is_update(self):
        """The foo property."""
        return self.archive.state == STATE_UPDATE

    @property
    def season_title(self) -> str:
        if self.ext:
            return self.ext.season_title
        return ""

    @property
    def season_id(self) -> int:
        if self.ext:
            return self.ext.season_id
        return 0

    def set_ext_season_title(self, value) -> 'ArcAuditModel':
        return self.set_ext_field('season_title', value)

    def set_ext_cid(self, value) -> 'ArcAuditModel':
        return self.set_ext_field('cid', value)

    def set_ext_album_id(self, value) -> 'ArcAuditModel':
        return self.set_ext_field('album_id', value)

    def set_ext_episode_id(self, value) -> 'ArcAuditModel':
        return self.set_ext_field('episode_id', value)

    def set_ext_field(self, key, value) -> 'ArcAuditModel':
        ext: ArchiveExt = self.ext or ArchiveExt()
        setattr(ext, key, value)
        self.ext = ext
        return self

    def to_section_episode(self) -> 'SectionEpisodeModel':
        return SectionEpisodeModel(
            aid=self.aid, cid=self.cid, title=self.title)
