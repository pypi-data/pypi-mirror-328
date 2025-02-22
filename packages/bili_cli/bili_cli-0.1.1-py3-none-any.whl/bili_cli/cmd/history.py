#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from datetime import datetime, timedelta
from rich import print
from typer import Typer, Option, Argument
from bili_cli.mod import RequestHistory
from bili_cli.tools.pretty_print import print_pretty
from bili_cli.base import MongoQuery
from .base import command

app = Typer()


@command(app, name='list', help='查看列表')
def _list(
    type_: str = Argument('history', help='类别', ),
    keyword: str = Option(None, help='搜索关键字'),
    order: str = Option('-create_time', help='排序 '),
    page: int = Option(1, ),
    pagesize: int = Option(10),
):
    query = (
        MongoQuery.build(RequestHistory).page(page).pagesize(pagesize)
        .sort(order)
    )
    if keyword:
        query.like('url', keyword)
    query.include(
        'response.headers.X-Bili-Trace-Id',
        'method',
        'status_code',
        'create_time',
        'request.path',
        'request.params'
    )
    query_res = RequestHistory.find_page_items(query)
    print_pretty(query_res.data)
    print(f"Total: {query_res.total}")


@command(app, help='查看详情')
def info(
    hid: str = Argument(help='history id'),
    with_browser: bool = Option(False, help='使用浏览器打开'),
):
    if with_browser:
        import subprocess
        subprocess.run(['open', f'http://localhost:8006/api/history/request/{hid}'])

    h = RequestHistory.find_by_id(hid)
    h.pprint()


@command(app, name='clear', help='清理历史数据 ')
def clear(
    days: int = Option(10, '--before-days', '-d', help='清理多少天之前')
):
    before_datetime = datetime.now() - timedelta(days=days)
    q = (
        MongoQuery.default()
        .lte('create_time', before_datetime)
    )
    ids = []
    for item in RequestHistory.find(q):
        id_ = item.get_id()
        ids.append(id_)
    res = RequestHistory.get_db().delete_many({"_id": {"$in": ids}})
    print(f"删除截止日期: {before_datetime} 条数: [cyan]{res.deleted_count}[/cyan]")
