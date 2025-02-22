#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
import os
import subprocess
from typer import Typer, Option, Argument
from bili_cli import manage as bm
from bili_cli.part import manage as pm
from bili_cli.config import settings
from bili_cli.tools import logger, show_in_finder as _show_in_finder
from .base import command, OPT_MID, OPT_PAGE, OPT_ALBUM_ID
from bili_cli.tools.pretty_print import print_pretty

app = Typer()


@command(app, help='分割剧集')
def split(
    episode_id: str = Argument(help='剧集id'),
    mid: int = Option(settings.default_auth_user_id),
    album_id: str = Option(settings.default_album_id),
):
    bm.split_episode(album_id, mid, episode_id)


@command(app, help='展示目录')
def show_in_finder(
    album_id: str = Argument(help='专辑'),
    action: str = Option('episode', help='动作'),
    episode_id: str = Option('S01E01', help='剧集id'),
):
    m = pm.get_manage(album_id, settings.default_auth_user_id)
    if action == 'split':
        dirname = os.path.join(m.part_root, 'split', m.album.id)
        logger.info(f"{album_id} split dir: {dirname}")
        subprocess.run(['open', dirname])
    elif action == 'episode':
        episode = m.get_episode_by_id(episode_id)
        _show_in_finder(episode.path)
    elif action == 'part':
        episode = m.get_episode_by_id(episode_id)
        subprocess.run(['open', episode.part_source_dir])


@command(app, name='list', help='展示剧集列表')
def list_episodes(
    album_id: str = Argument(help='专辑'),
    mid: int = OPT_MID,
    season: int = Option(1, help='季数'),
    page: int = OPT_PAGE,
    pagesize: int = Option(30, help='每页条数'),
):
    res = bm.find_episodes(album_id, mid, season=season, page=page, pagesize=pagesize)
    items = res.data
    print_pretty(items)
    print(f"Total: {res.total}")


@command(app, help='制作片段视频')
def make_part(
    episode_id: str = Argument(help='剧集id'),
    mid: int = OPT_MID,
    album_id: str = OPT_ALBUM_ID,
):
    bm.make_episode_part_video(album_id, mid, episode_id)
