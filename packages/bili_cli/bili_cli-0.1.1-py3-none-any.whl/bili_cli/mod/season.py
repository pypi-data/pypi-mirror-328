#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from pydantic import Field
from typing import List, Optional
from bili_cli.base import BaseMongoORM
from .archive import SectionEpisodeModel


class SectionModel(BaseMongoORM):
    id: int = Field(0)
    title: str = Field("")
    cover: str = Field("", title='封面')
    season_id: int = Field(0, alias='seasonId')
    ep_count: int = Field(0, alias="epCount")
    order: int = Field(0)
    type: int = Field(0)
    episodes: Optional[List[SectionEpisodeModel]] = Field([], title='小节稿件')
    ctime: int = Field(0, title="")
    mtime: int = Field(0, title="")

    class Meta():
        TABLE = "section"

    def get_id(self):
        return str(self.id)


class SeasonModel(BaseMongoORM):
    id: int = Field(0)
    title: str = Field("")
    cover: str = Field("", title='封面')
    desc: str = Field("")
    mid: int = Field(0, title='用户id')
    forbid: int = Field(0, title="放刷屏",
                                 description='1 使用 0 不使用')
    no_section: int = Field(1, title="是否没有小节",
                                     description='1 没有 0 有小节')
    ctime: int = Field(0, title="")
    mtime: int = Field(0, title="")
    is_opened: int = Field(0, title="是否打开")
    sections: List[SectionModel] = Field([], title='小节列表')

    class Meta(BaseMongoORM.Meta):
        TABLE = "season"

    def get_id(self):
        return str(self.id)

    @property
    def forbid_fmt(self):
        """The forbid_fmt property."""
        return '防刷屏' if self.forbid else '刷屏'

    @property
    def no_section_fmt(self):
        """The forbid_fmt property."""
        return '无小节' if self.no_section else '有小节'

    @property
    def section(self):
        return '\n'.join([f"{o.title} {o.id} {o.ep_count}" for o in self.sections])

    @classmethod
    def table_headers(cls) -> List[str]:
        return ['id', 'title', 'section', 'forbid_fmt', 'no_section_fmt', 'ctime', 'mtime', 'is_delete']

    def pprint(self):
        from rich.tree import Tree
        from rich.console import Console, Group
        from rich.table import Table
        f_fmt = '防刷屏' if self.forbid else '刷屏'
        s_fmt = '无小节' if self.no_section else '有小节'
        root = Tree(f"合集: {self.title} {f_fmt} {s_fmt} {self.desc} {self.cover}")
        for sec in self.sections:
            node = root.add(f"小节: {sec.title}")
            if not sec.episodes:
                continue
            table = Table()
            headers = sec.episodes[0].table_headers()
            for header in headers:
                table.add_column(header)
            for ep in sec.episodes:
                line = []
                for field in headers:
                    line.append(str(getattr(ep, field, '')))
                table.add_row(*line)
            node.add(Group("稿件列表", table))

        console = Console()
        console.print(root)
