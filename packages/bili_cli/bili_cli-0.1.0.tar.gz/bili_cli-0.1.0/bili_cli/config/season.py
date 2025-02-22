#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
import pydantic
import re
from typing import List, Self
from bili_cli import mod, dtos as dto, const
from bili_cli.base import BaseMongoORM
from bili_cli import utils
from bili_cli.mod import SeasonModel


class SeasonType():
    EPISODE = 'episode'
    CUSTOM = 'custom'
    NONE = ""


class SectionSortType():
    EPISODE_PART = 'episode_part'
    VIEW_COUNT = 'view_count'


class SectionConfig(BaseMongoORM):
    id: int = pydantic.Field(0)
    season_id: int = pydantic.Field(0)
    title: str = pydantic.Field("")
    order: int = pydantic.Field(0)
    season: int = pydantic.Field(0)
    ep_start: int = pydantic.Field(0)
    ep_end: int = pydantic.Field(0)
    ep_prefixs: list = pydantic.Field([])
    ep_ids: list = pydantic.Field([])
    sort_type: str = pydantic.Field(
        SectionSortType.EPISODE_PART, title='排序方式')
    archive_title_rexs: List[str] = pydantic.Field([], title="视频标题正则")
    archive_title_regs: List[re.Pattern] = pydantic.Field([], title="视频标题正则")

    # 扩展数据
    archives: List[mod.ArcAuditModel] = pydantic.Field([])

    def load(self) -> Self:
        self.archive_title_regs = []
        for rex in self.archive_title_rexs:
            rex = rex.format(**const.EPISODE_TITLE_REX_DICT)
            self.archive_title_regs.append(re.compile(rex))
        return self

    @property
    def episode_ids(self):
        if self.ep_ids:
            return self.ep_ids
        """The episode_ids property."""
        return [f"S{self.season:0>2}E{ep:0>2}" for ep in range(
            self.ep_start, self.ep_end+1)]

    def has_episode(self, ep: mod.SectionEpisodeModel):
        for prefix in self.ep_prefixs:
            if ep.title.startswith(prefix):
                return True
        return False

    def set_archive_title_rexs(self, rexs) -> Self:
        self.archive_title_rexs = rexs
        for rex in rexs:
            rex = rex.format(**const.EPISODE_TITLE_REX_DICT)
            self.archive_title_regs.append(re.compile(rex))
        return self

    def is_match_archive_title(self, title) -> bool:
        """匹配稿件名称到片段"""
        for reg in self.archive_title_regs:
            if utils.is_match_str(reg, title):
                return True
        return False


class SeasonConfig(SeasonModel):
    id: str = pydantic.Field("")
    # 功能属性
    type: str = pydantic.Field(SeasonType.NONE, title="合集类型")
    album_id: str = pydantic.Field("")
    season: int = pydantic.Field(0)
    ep_count: int = pydantic.Field(0)
    section_ep_count: int = pydantic.Field(0)
    ep_prefix: str = pydantic.Field("")
    sections: List[SectionConfig] = pydantic.Field([])
    archive_title_rexs: List[str] = pydantic.Field([], title="视频标题正则")
    archive_title_regs: List[re.Pattern] = pydantic.Field([], title="视频标题正则")

    class Meta():
        TABLE = "season_config"

    def get_id(self):
        return self.title

    @classmethod
    def table_headers(cls) -> List[str]:
        return ['id', 'title', 'cover', 'forbid_fmt', 'no_section_fmt']

    def load(self) -> Self:
        self.archive_title_regs = []
        for rex in self.archive_title_rexs:
            rex = rex.format(**const.EPISODE_TITLE_REX_DICT)
            self.archive_title_regs.append(re.compile(rex))

        for sec in self.sections:
            sec.load()
        return self

    def get_save_data(self) -> dict:
        data = super().get_save_data()
        data.pop('archive_title_regs', [])
        for sec in data.get("sections"):
            sec.pop('archive_title_regs', [])
        return data

    def enable_forbid(self) -> 'SeasonConfig':
        """使用防刷屏"""
        self.forbid = 1
        return self

    def enable_section(self) -> 'SeasonConfig':
        """使用小节"""
        self.no_section = 0
        return self

    def set_section_ep_count(self, count) -> 'SeasonConfig':
        self.section_ep_count = count
        return self

    def set_title(self, title) -> 'SeasonConfig':
        self.title = title
        return self

    def set_desc(self, desc) -> 'SeasonConfig':
        self.desc = desc
        return self

    def set_archive_title_rexs(self, rexs) -> 'SeasonConfig':
        self.archive_title_rexs = rexs
        for rex in rexs:
            rex = rex.format(**const.EPISODE_TITLE_REX_DICT)
            self.archive_title_regs.append(re.compile(rex))
        return self

    def set_archive_title_rexs_auto(self, user_id) -> 'SeasonConfig':
        rexs = const.get_season_archive_titles(self.album_id, user_id)
        return self.set_archive_title_rexs(rexs)

    def is_match_archive_title(self, title) -> bool:
        # 先匹配小节
        for sec in self.sections:
            if sec.is_match_archive_title(title):
                return True
        # 最后统一由合集匹配
        if self.match_archive_title(title):
            return True
        return False

    def match_archive_title(self, title) -> mod.MatchPart:
        """匹配稿件名称到片段"""
        for reg in self.archive_title_regs:
            p = utils.match_part(reg, title)
            if not p:
                continue
            if self.season and self.season != p.season:
                continue
            return p
        return None

    def init_sections(self):
        self.sections = []
        ep_count = self.ep_count
        section_ep_count = self.section_ep_count
        for i, ep_s in enumerate(range(0, ep_count, section_ep_count)):
            ep_s += 1
            ep_end = ep_s + section_ep_count - 1
            if ep_end > ep_count:
                ep_end = ep_count
            section = SectionConfig(
                ep_start=ep_s, ep_end=ep_end, title=f"{ep_s}-{ep_end}",
                order=i+1, season=self.season
            )
            for x in range(ep_s, ep_end+1):
                section.ep_prefixs.append(f"{self.ep_prefix}{x:0>2}")
            self.sections.append(section)
        return self

    def get_section(self, title: str) -> SectionConfig:
        for sec in self.sections:
            if sec.title == title:
                return sec
        return None

    def to_season_add_req(self) -> dto.SeasonAddReqDTO:
        return dto.SeasonAddReqDTO(**self.model_dump(by_alias=True))
