#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from rich import print
from typer import Typer, Option
from bili_cli.tools.pretty_print import print_pretty
from .base import command, OPT_ALBUM_ID, ARG_ALBUM_ID
from bili_cli.config import settings
from bili_cli.part import manage as pm
from bili_cli.manage import init_part

app = Typer(name='part', help='视频片段')


@command(app, name='list', help='查看稿件列表')
def _list(
    album_id: str = OPT_ALBUM_ID,
    page: int = Option(1),
    pagesize: int = Option(10),
):
    m = pm.get_manage(album_id, settings.default_auth_user_id)
    query_res = m.find_parts(page=page, pagesize=pagesize)
    print_pretty(query_res.data,
                 #  maxcolwidths=[None, None, 50, None, None, None, None, None],
                 )
    print(f"Total: {query_res.total}")


@app.command()
def init(
    album_id: str = ARG_ALBUM_ID,
    recreate: bool = Option(False, help='是否重新创建'),
):
    init_part(album_id, recreate=recreate)
