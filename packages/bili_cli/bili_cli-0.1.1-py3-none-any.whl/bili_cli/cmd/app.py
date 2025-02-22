#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
import plotext as plt
import os
from typer import (
    Typer,
    Argument,
    Option,
)
from . import (
    season,
    auth,
    archive,
    episode,
    history,
    reply,
    part,
    config,
)
from .download import download
from rich import print
from bili_cli.bili import DEFAULT_BILI, get_bilis
from bili_cli.manage import init_db, move_screenshot
from bili_cli.config.user_album import get_user_albums
from bili_cli.tools.loggers import set_logger_level
from .base import OPT_MID, command, exit
from bili_cli.const import BILIUP_PATH

app = Typer()
app.add_typer(season.app)
app.add_typer(auth.app, name='auth')
app.add_typer(archive.app, name='archive')
app.add_typer(episode.app, name='episode')
app.add_typer(history.app, name='history')
app.add_typer(reply.app, name='reply')
app.add_typer(part.app)
app.add_typer(config.app)
command(app, name='download', help='下载视频')(download)


@app.callback()
def verbose_callback(
    verbose: bool = Option(False, '--verbose', '-v', help='是否展示更详细信息 ')
):
    if verbose:
        print("显示详细信息")
        set_logger_level("DEBUG")


@command(app, name='login', help='登录')
def login():
    if not os.path.exists(BILIUP_PATH):
        exit(f"{BILIUP_PATH} 脚本不存在")
    DEFAULT_BILI.login_by_biliup()


@command(app, name='init', help='初始化 ')
def init(
    action: str = Argument('', help='刷新动作 ua vc album season'),
    mid: int = OPT_MID,
):
    init_db(action=action, auth_user_id=mid)


def complete_income():
    return ['stacked', 'multiple']


@command(app, name='income', help='收入')
def income(
    bar: str = Option('stacked', help='展示类型', show_choices=True, autocompletion=complete_income),
    pagesize: int = Option(10),
    is_update: bool = Option(False, '--update', '-u', help='是否更新')
):
    '''收入展示
    plotext bar api
    https://github.com/piccolomo/plotext/blob/master/readme/bar.md
    '''
    data = []
    dates = []
    labels = []
    for bili in get_bilis():
        if is_update:
            bili.get_daliy_income(days=30)
        incomes = bili.find_incomes(pagesize=pagesize).data
        incomes.sort(key=lambda o: o.date)
        data.append([float(o.income) for o in incomes])
        dates = [o.date_fmt[5:] for o in incomes]
        labels.append(bili.auth.bili_name)

    func = getattr(plt, f"{bar}_bar")
    func(
        dates,
        data,
        color=['red', 'gray', 'green', 'orange', 'cyan', 'blue'],
        label=labels,
    )
    plt.title("账号收益明细")
    plt.show()


@command(app, name='check-title', help='检查标题 ')
def check_title(
    title: str = Argument()
):
    print("匹配合集:")
    for bili in get_bilis():
        sea_conf = bili.match_title_to_season_config(title)
        if not sea_conf:
            continue
        print(f"[cyan]Match:[/cyan] {bili.Meta.NAME} {sea_conf.title}")

    print("")
    print("匹配剧集:")
    for ua in get_user_albums():
        part = ua.match_title_to_part(title)
        if not part:
            continue
        print(f"[cyan]Match:[/cyan] {ua.user_id}-{ua.album_id} {part.episode_id}.{part.part}")


@command(app, name='move-screenshot', help='移动截图 ')
def move_screenshot_():
    move_screenshot()
