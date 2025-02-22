#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
import pydantic
from typing import List
from datetime import datetime
from pydantic import model_validator
from bili_cli.base import BaseModel, BaseORM, BaseMongoORM
from bili_cli import tools
from bili_cli.mod.archive import ArcAuditModel


class EpisodeModel(BaseMongoORM):
    id: str = pydantic.Field("", title="id")
    manage_name: str = pydantic.Field("", title="id")
    title: str = pydantic.Field("", title="名称")
    episode: str = pydantic.Field("", title="")
    subtitles: List[str] = pydantic.Field([], title="副标题合集")
    album_id: str = pydantic.Field("", title="专辑")
    album: str = pydantic.Field("", title="专辑")
    path: str = pydantic.Field("", title="地址")
    ts: str = pydantic.Field("", title="ts地址")
    part_source_dir: str = pydantic.Field("", title="切片源目录")
    season: int = pydantic.Field(1, title="")
    season_title: int = pydantic.Field("", title="季名称")
    ep: int = pydantic.Field(0, title="集数，数值")
    order: int = pydantic.Field(0, title="排序")
    bed: List[tuple] = pydantic.Field([], title="")
    story: List[str] = pydantic.Field([], title="故事")

    archives: List[ArcAuditModel] = pydantic.Field([], title="关联稿件")

    @model_validator(mode='before')
    def validator_all(cls, values):
        id = values.get("id")
        if id:
            season, ep = id.split("E")
            ep = int(ep)
            values['ep'] = ep
            season = int(season[1:])
            values['season'] = season
            values['order'] = season * 1000000 + ep
        title = values.get("title")
        if title:
            values['episode'] = title
        return values

    def get_title(self):
        return self.title or self.ep_str

    @classmethod
    def table_headers(cls) -> List[str]:
        return ['id', 'title', 'archive', 'bed']

    @property
    def archive(self):
        lines = []
        for i, arch in enumerate(self.archives):
            lines.append(f"{i} {arch.title}")
        if lines:
            return '\n'.join(lines)
        return ""

    @property
    def ep_str(self):
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

    def get_order(self) -> int:
        return self.season * 1000000 + self.ep * 1000

    def get_format_kwargs(self):
        return dict(
            album=self.album,
            season=self.season,
            ep=self.ep,
            episode=self.get_title()
        )


class MatchPart(EpisodeModel):
    part: int = pydantic.Field(0, title="片段")
    ab: str = pydantic.Field("", title="专辑简称")

    def get_order(self) -> int:
        return super().get_order() + self.part

    @property
    def part_id(self) -> str:
        """The part_id property."""
        return f"{self.ab}{self.season}.{self.ep}.{self.part}"

    def get_format_kwargs(self):
        kw = self.get_format_kwargs()
        kw['part'] = self.part
        return kw


class EpisodeArchiveModel(BaseORM):
    episode_id: str = pydantic.Field("", title="id")
    album_id: str = pydantic.Field("", title="id")
    #  manage_name: str = pydantic.Field("", title="id")
    archive_ids: list = pydantic.Field([], title="id")

    class Meta(BaseORM.Meta):
        TABLE = 'episode_archive'

    def get_id(self) -> str:
        if self.id:
            return self.id
        return f"{self.album_id}-{self.episode_id}"

    @classmethod
    def build(cls, manage_name: str, episode_id: str) -> 'EpisodeArchiveModel':
        return cls(album_id=manage_name, episode_id=episode_id)


class AuthModel(BaseModel):
    id: str = pydantic.Field("", title="id")
    cookie: str = pydantic.Field("", title="网络请求cookie")
    bili_jct: str = pydantic.Field("", title="post请求认证")


class DaliyIncomModel(BaseMongoORM):
    date_key: int = pydantic.Field(0, title="日期")
    date: datetime = pydantic.Field(None, title="日期")
    amt: int = pydantic.Field(0, title="收入")

    class Meta(BaseMongoORM.Meta):
        TABLE = 'daliy_inome'

    def get_id(self) -> str:
        return str(self.date_key)

    @property
    def date_fmt(self):
        return self.date.strftime("%Y-%m-%d")

    @property
    def income(self):
        f = float(self.amt) / 100
        return f"{f:2}"

    @model_validator(mode='before')
    def validator_all(cls, values):
        #  print(values)
        date = values.get("date") or 0
        if isinstance(date, int):
            values['date'] = datetime.fromtimestamp(date)
            values['date_key'] = date

        return values


class Video(BaseMongoORM):
    width: int = pydantic.Field(title="宽")
    height: int = pydantic.Field(title="高")
    duration: float = pydantic.Field(title="长度")
    dur: str = pydantic.Field(None, title="长度")
    size: int = pydantic.Field(title="大小")

    class Meta(BaseMongoORM.Meta):
        TABLE = "video_info"

    @model_validator(mode='before')
    def validator_all(cls, values):
        values['dur'] = tools.format_duration(values['duration'])
        return values

    @property
    def size_fmt(self):
        s = self.size / 1024.0 / 1024.0
        return f"{s:.2f} MB"
