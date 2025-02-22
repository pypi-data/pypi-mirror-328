#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from typer import Typer, Argument, Option
from bili_cli.tools.pretty_print import print_pretty
from bili_cli.bili import get_bili, get_bilis
from bili_cli.config import settings
from .base import command

app = Typer()


@command(app, name='refresh', help='刷新回复')
def refresh_replys(
    mid: int = Option(0, help='用户id'),
    total_page: int = Option(5, help='刷新的页数，默认使用最大'),
    print_data: bool = Option(True, help='打印结果'),
):
    for bili in get_bilis(mid):
        for i in range(total_page):
            bili.get_replys(page=i+1, pagesize=50)

    if mid and print_data:
        list_reply(mid=mid)


@command(app, name='list', help='查看回复列表')
def list_reply(
    mid: int = Argument(settings.default_auth_user_id, help='用户id'),
    page: int = Option(1, help='页码'),
    pagesize: int = Option(10, help='每页条数'),
):
    bili = get_bili(mid)
    res = bili.find_replys(page=page, pagesize=pagesize)
    items = res.data
    print_pretty(items, maxcolwidths=[None, None, 40, 90])
    print(f"Total: {res.total}")
