#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from typer import Typer, Option
from bili_cli.mod import ConfigModel
from bili_cli.tools.pretty_print import print_pretty
from bili_cli.base import MongoQuery
from .base import command
from . import config_video, config_user_album

app = Typer(name='config', help='配置相关')
app.add_typer(config_video.app)
app.add_typer(config_user_album.app)


@command(app, name='list', help='查看列表')
def _list(
    page: int = Option(1,),
    pagesize: int = Option(10),
        ):
    query = (
        MongoQuery.build(ConfigModel).page(page).pagesize(pagesize)
        .sort('update_time', typ='desc')
    )
    query_res = ConfigModel.find_page_items(query)
    print_pretty(query_res.data)
    print(f"Total: {query_res.total}")
