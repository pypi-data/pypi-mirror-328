#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import pydantic
import os
from pydantic import Field
from collections import defaultdict
from typing import Dict, Self
from bili_cli.base import BaseMongoORM
from bili_cli import const
from bili_cli.models import Video


class Part(BaseMongoORM):
    manage_name: str = Field(title="管理名称")
    id: str = Field("", title="id")
    name: str = Field("", title="名称")
    episode: str = Field("", title="集数")
    episode_name: str = Field("", title="集名称")
    season: int = Field(0, title="")
    ep: int = Field(0, title="集数，数值")
    order: int = Field(0, title="排序")
    path: str = Field("", title="地址")
    source_dir: str = Field("", title="原址的目录")
    used_times: int = Field(0, title="使用次数")
    info: Video = Field(None, title="详情")

    class Meta(BaseMongoORM.Meta):
        TABLE = "part"

    def get_ts_path(self):
        return os.path.join(const.get_part_dir(), self.manage_name, f"{self.id}.ts")

    @classmethod
    def table_headers(cls) -> list:
        return ['id', 'name', 'episode_id', 'dur', 'size_fmt', 'path']

    @property
    def dur(self):
        if not self.info:
            return ''
        return self.info.dur

    @property
    def size_fmt(self):
        if not self.info:
            return ''
        return self.info.size_fmt

    @property
    def ep_str(self):
        """The ep_str property."""
        ep = f"{self.ep:0>2}"
        if self.ep > 1000:
            ep = f"{self.ep:0>5}"
        return ep

    @property
    def season_str(self):
        """The ep_str property."""
        return f"{self.season:0>2}"

    @property
    def episode_id(self) -> str:
        """The ep_str property."""
        return f"S{self.season_str}E{self.ep_str}"


class PartModel(Part):
    pass


class PartUsedModel(BaseMongoORM):
    user_id: str = pydantic.Field("", title="用户id")
    album_id: str = pydantic.Field("", title="album id")
    part_used: Dict[str, int] = pydantic.Field(defaultdict(int), title="用户id")

    class Meta(BaseMongoORM.Meta):
        TABLE = "part_used"

    def get_id(self) -> str:
        return f"{self.user_id}-{self.album_id}"

    def increment(self, part_id) -> Self:
        self.part_used[part_id]+=1
        return self

    def get_part_used_times(self, part_id: str) -> int:
        return self.part_used[part_id]

    @classmethod
    def find_part_used(cls, album_id: str, user_id: str) -> Self:
        item = cls(album_id=album_id, user_id=user_id)
        exists = cls.find_by_id(item.get_id())
        if exists:
            exists.part_used = defaultdict(int, exists.part_used)
            return exists
        return item
