#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from typer import Typer, Argument, Option
from typing import Optional
from bili_cli.tools import logger
from bili_cli.tools.pretty_print import print_pretty
from bili_cli.bili import get_bili, get_bilis
from bili_cli.base import MongoQuery
from bili_cli.mod import SeasonModel
from bili_cli.config import settings
from .base import OPT_MID, OPT_MID_NONE, command, exit

app = Typer(name='season', help='合集相关')


@command(app)
def refresh(mid: int = Option(0, help='用户id'),
            print_data: bool = Option(True, help='打印结果')):
    for bili in get_bilis(mid):
        bili.refresh_season()

    if mid and print_data:
        list_season(mid=mid)


@command(app)
def create(
    title: str = Argument(help='合集标题'),
    mid: int = OPT_MID,
):
    bili = get_bili(mid)
    logger.info(f"{bili.log_prefix()} 创建合集: {title}")
    if bili.Meta.get_season_config(title):
        sea_d = bili.create_season_by_config(title)
    else:
        sea_d = bili.search_or_create_season(title)
    logger.info(f"{bili.log_prefix()} 创建合集: {title} 成功 id: {sea_d.season.id}")

    # 查看列表
    list_season(mid=mid)


@command(app, name='list', help='合集列表')
def list_season(
    mid: int = OPT_MID,
):
    items = SeasonModel.find(MongoQuery.default().eq('mid', mid))
    items = [o for o in items]
    print("配置列表:")
    bili = get_bili(mid)
    _items = bili.get_season_configs()
    print_pretty(_items)
    print(f"Total: {len(_items)}")
    print("")
    print("远程合集列表:")
    print_pretty(items)
    print(f"Total: {len(items)}")


@command(app, name='del')
def del_(
    sid: str = Argument(help='合集id'),
    mid: int = OPT_MID,
):
    bili = get_bili(mid)
    bili.del_season(sid)


@command(app, name='info')
def info(
    sid: str = Argument(help='合集id'),
    #  mid: int = OPT_MID,
    with_browser: bool = Option(False, help='使用浏览器打开')
):
    if with_browser:
        import subprocess
        subprocess.run(['open', f'{settings.full_host}/api/season/{sid}.json'])
        return
    item = SeasonModel.find_by_id(sid)
    if not item:
        print(f"[red]ERROR[/red] 找不到合集: {sid}")
        return
    item.pprint()


@command(app, name='update')
def update(
    sid: int = Argument(help='合集id'),
    title: str = Option('', help='标题 '),
    forbid: Optional[int] = Option(None, '--forbid', '-f', help='防止刷屏。1、使用；0、不使用'),
    no_section: Optional[int] = Option(None, '--no-section', '-s', help='使用小节。1、使用；0、不使用'),
    with_config: bool = Option(False, help='使用配置修改')
):
    sea = SeasonModel.find_by_id(sid)
    if not sea:
        exit(f"合集: {sid} 找不到 ")

    bili = get_bili(sea.mid)
    flag = False
    if with_config:
        flag = bili.update_season_by_config(sid)
    else:
        flag = bili.update_season(sid, title=title, forbid=forbid, no_section=no_section)
    if flag:
        item = bili.get_season(sid).season
        item.pprint()
        print("修改成功")
    else:
        exit("修改失败")
