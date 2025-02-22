#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import pydantic
from typing import List
from datetime import datetime
from pydantic import model_validator
from bili_cli.base import BaseORM, BaseModel, BaseMongoORM
from bili_cli import tools


class Card(BaseModel):
    from_: int = pydantic.Field(0, title="开始时间", alias="from")
    from_dur: str = pydantic.Field("", title="时间格式化")
    to: int = pydantic.Field(0, title="截止时间")
    to_dur: str = pydantic.Field("", title="时间格式化")
    content: str = pydantic.Field("", title="内容")

    @classmethod
    def build(cls, from_: int, to: int, content: str) -> 'Card':
        return cls(
            from_=from_, to=to, content=content,
        ).load()

    @model_validator(mode='before')
    def validator_all(cls, values):
        f = values.get('from_')
        if f:
            values['from'] = f
        return values

    def load(self) -> 'Card':
        self.from_dur = tools.format_duration(self.from_)
        self.to_dur = tools.format_duration(self.to)
        return self


class HistoryModel(BaseMongoORM):
    title: str = pydantic.Field("")
    user_id: str = pydantic.Field("", title="用户")
    album_id: str = pydantic.Field("", title="内容")
    part_ids: list = pydantic.Field([], title="片段id列表")
    ts_list: list = pydantic.Field([], title="片段列表")
    ctime: int = pydantic.Field(default_factory=tools.build_timestamp,
                                title="创建时间")
    cards: List[Card] = pydantic.Field([], title="时间节点列表")
    duration: float = pydantic.Field(0, title="长度")

    class Meta(BaseMongoORM.Meta):
        TABLE = 'history'
        DB = 'bili_record'

    def build_card_reply(self) -> str:
        reply = "导航已做\n"
        for card in self.cards:
            card.load()
            reply += f"{card.from_dur}  {card.content}\n"
        return reply
