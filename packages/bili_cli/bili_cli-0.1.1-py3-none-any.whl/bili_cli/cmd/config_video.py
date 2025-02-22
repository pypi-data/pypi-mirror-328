#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from typer import Typer, Option, Argument
from bili_cli.tools.pretty_print import print_pretty
from bili_cli.make import VideoConfig
from bili_cli.manage import make_video_by_config
from .base import command, OPT_MID, p_error

app = Typer(name='video', help='视频配置相关')


@command(app, name='list', help='查看列表')
def _list(
    mid: int = OPT_MID,
    album_id: str = Option('', help='专辑'),
    type: str = Option('', help='类型'),
    season: int = Option(1, help='季数'),
    episode_id: str = Option('', help='集数'),
    page: int = Option(1,),
    pagesize: int = Option(10),
):
    query_res = VideoConfig.find_configs(
        user_id=mid,
        album_id=album_id,
        season=season,
        type_=type,
        episode_id=episode_id,
        page=page,
        pagesize=pagesize
    )
    print_pretty(query_res.data)
    print(f"Total: {query_res.total}")


@command(app, name='make', help='构建视频')
def make(
    conf_id: str = Argument(..., help='配置id'),
    mid: int = Option(0, help='用户jd'),
    album_id: str = Option('', help='专辑'),
):
    config = VideoConfig.find_by_id(conf_id)
    if not config:
        p_error(f"找不到配置: {conf_id}")
        return
    if not mid and not album_id:
        mid, album_id, _ = conf_id.split('-')
    make_video_by_config(album_id, int(mid), conf_id)
