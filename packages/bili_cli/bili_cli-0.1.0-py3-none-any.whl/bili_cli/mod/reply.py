#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from datetime import datetime
from pydantic import Field
from typing import Union, List
from bili_cli.base import BaseMongoORM, BaseModel


class LevelInfo(BaseModel):
    current_level: int = Field(0, title="当前等级")


class ReplyModel(BaseMongoORM):
    mid: int = Field(0, title="评论人id")
    oid: int = Field(0, title="视频aid")
    rpid: int = Field(0, title="评论id")
    type: int = Field(0, title="")
    bvid: str = Field("", title="视频id")
    title: str = Field("", title="视频标题")
    cover_url: str = Field("", title="封面")
    like: int = Field(0, title="点赞数")
    action: int = Field(0, title="是否点赞")
    parent: int = Field(0, title="回复人id")
    root: int = Field(0, title="根评论id")
    ctime: int = Field(0, title="")
    content: 'Content' = Field(None, title="回复内容")
    member: 'Member' = Field(None, title="评论人")
    reply_control: 'Control' = Field(None, title="评论控件")
    up_action: 'UpAction' = Field(None, title="UP操作详情")
    parent_info: Union['ReplyModel', None] = Field(
        None, title="回复上级内容")
    root_info: Union['ReplyModel', None] = Field(None, title="根评论")

    class Meta():
        TABLE = "reply"

    def get_id(self):
        return str(self.rpid)

    @classmethod
    def table_headers(cls) -> List[str]:
        return ['rpid', 'title', 'message', 'up_like', 'create_at']

    class Content(BaseModel):
        message: str = Field("", title="回复内容")

    class Member(BaseModel):
        mid: int = Field(0, title="评论人id")
        uname: str = Field("", title="评论人")
        level_info: LevelInfo = Field(LevelInfo(), title="评论人")

    class Control(BaseModel):
        up_like: bool = Field(False, title="up是否点赞")
        followed: bool = Field(False, title="是否关注UP")
        is_top: bool = Field(False, title="是否置顶")
        is_charge_plus: bool = Field(False, title="是否为充电评论")

    class UpAction(BaseModel):
        like: bool = Field(False, title="up是否点赞")
        reply: bool = Field(False, title="up是否回复")

    @property
    def message(self):
        return self.content.message

    @property
    def up_like(self):
        return self.reply_control.up_like if self.reply_control else False

    @property
    def create_at(self):
        return datetime.fromtimestamp(self.ctime)
