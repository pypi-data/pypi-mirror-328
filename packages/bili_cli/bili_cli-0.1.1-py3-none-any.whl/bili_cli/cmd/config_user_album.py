#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from typer import Typer, Option, Argument
from bili_cli.tools.pretty_print import print_pretty
from bili_cli.base import MongoQuery
from bili_cli.config import UserAlbumConfig
from bili_cli.bili import get_bili
from .base import command, OPT_MID

app = Typer(name='user-album', help='用户视频配置相关')


@command(app, name='list', help='查看列表')
def _list(
    mid: int = OPT_MID,
    album_id: str = Option('', help='专辑'),
    page: int = Option(1,),
    pagesize: int = Option(10),
):
    q = (
        MongoQuery.default()
        .page(page).pagesize(pagesize)
    )
    if album_id:
        q.eq('album_id', album_id)
    bili = get_bili(mid)
    q.eq('user_id', bili.auth.bili_name)
    query_res = UserAlbumConfig.find_page_items(q)
    print_pretty(query_res.data)
    print(f"Total: {query_res.total}")


@command(app, name='info', help='查看 详情 ')
def info(
    id_: str = Argument(help='配置 id')
):
    item = UserAlbumConfig.find_by_id(id_)
    item.pprint()
