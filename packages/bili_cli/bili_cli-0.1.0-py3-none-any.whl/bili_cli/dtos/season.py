#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from typing import List, Self
from pydantic import Field
from .base import BaseActionDTO, BaseReqDTO
from bili_cli.const import IMAGE_SEASON_DEFAULT
from bili_cli.mod import SectionEpisodeModel, SeasonModel, SectionModel


class SeasonAddReqDTO(BaseActionDTO):
    cover: str = Field(IMAGE_SEASON_DEFAULT)
    title: str = Field()
    desc: str = Field("")
    season_price: int = Field(0)


class SectionEpisodeAddReqDTO(BaseActionDTO):
    section_id: int = Field(0, alias="sectionId")
    episodes: List[SectionEpisodeModel] = Field([], title='视频列表')


class SectionEpisodeSortDTO(BaseReqDTO):
    id: int = Field(0, title="")
    sort: int = Field(0, title="")


class SectionSortDTO(SectionEpisodeSortDTO):
    ...


class SectionEditReqDTO(BaseActionDTO):
    section: SectionModel = Field(None)
    sorts: List[SectionEpisodeSortDTO] = Field([])


class SeasonEditDTO(BaseActionDTO, SeasonModel):

    @property
    def model_dump_include(self):
        return ['id', 'title', 'cover', 'desc']


class SeasonEditReqDTO(BaseActionDTO):
    season: SeasonEditDTO = Field(title='合集信息')
    sorts: List[SectionSortDTO] = Field([], title='小节排序')

    @classmethod
    def build(
        cls,
        sid: int,
        *,
        title: str = None,
        cover: str = None,
        desc: str = None
    ) -> Self:
        season = SeasonEditDTO(
            id=sid,
            title=title,
            cover=cover,
            desc=desc,
        )
        item = cls(season=season)
        return item

    def to_req_data(self) -> dict:
        data = {}
        data['season'] = self.season.to_req_data()
        return data
