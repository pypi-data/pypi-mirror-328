#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
import os
import time
import subprocess
from rich import print
from datetime import datetime
from typer import Typer, Option, Argument, echo
from bili_cli.tools import logger
from bili_cli.tools.pretty_print import print_pretty
from bili_cli.bili import get_bilis, get_bili
from bili_cli import const
from bili_cli.manage import get_manage, refresh_archive_ext, refresh_episode_archive
from bili_cli.config import settings, get_album
from bili_cli.tools import tools
from bili_cli.dtos import ArchiveUploadReqDTO
from bili_cli.mod import ArcAuditModel, AuthUser
from bili_cli.service import ArchiveService
from bilibili_sdk import member_client, api_client
from bilibili_sdk.enums.archive import ArchiveState
from .base import command, OPT_MID, p_error, exit, ARG_MID

app = Typer()

archive_srv = ArchiveService()


@command(app, name='list', help='查看稿件列表')
async def _list(
    mid: int = ARG_MID,
    state: int = Option(-1, help='状态,0 开发浏览 -4 已锁定 -30 审核中、-40 审核通过，等待发布'),
    title: str = Option('', help='标题'),
    sort: str = Option('-ptime', help='排序'),
    season_title: str = Option('', help='合集名称'),
    page: int = Option(1),
    pagesize: int = Option(10),
    with_online: bool = Option(False, help='是否展示在线人数')
):
    bili = get_bili(mid)
    #  query_res = bili.find_archives(
        #  state=state, title_like=title, page=page, pagesize=pagesize,
        #  season_title_eq=season_title, sort=sort,
    #  )
    query_res = await archive_srv.find_archives(
        mid,
        state=state, title_like=title, page=page, pagesize=pagesize,
        season_title_eq=season_title, sort=sort,
    )
    audits = query_res.data
    if with_online:
        item: ArcAuditModel
        for item in audits:
            if item.state != ArchiveState.OPEN:
                continue
            if not item.videos:
                continue
            for video in item.videos:
                res = await api_client.get_online(cid=video.cid, bvid=item.bvid)
                item.online += res.data.total + " "

    print_pretty(audits,
                 maxcolwidths=[None, None, 50, None, None, None, None, None],
                 )
    print(f"Total: {query_res.total}")


@command(app, name='refresh-one', help='刷新单个稿件')
def refresh_one_archive(
    bvid_or_title: str = Argument(None, help='视频bvid或者标题'),
    mid: int = OPT_MID,
    total_page: int = Option(1, '--total-page', '-p', help='刷新的页数，默认刷新第一页'),
    loop_count: int = Option(10, '--loop', '-l', help='刷新的页数，默认刷新第一页'),
):
    bili = get_bili(mid)
    arch = None
    print(f"开始刷新指定稿件: {bvid_or_title}")
    for _ in range(loop_count):
        bili.refresh_archives(total_page=total_page)
        arch = bili.find_archive(bvid_or_title)
        if arch:
            break
        sleep_s = 5
        print(f"没有刷新到指定稿件，等待 {sleep_s} 秒钟 ")
        time.sleep(sleep_s)
    if arch:
        print(f"刷新到指定稿件: {arch.bvid} {arch.title}")
        print(arch.pprint())
    else:
        exit(f"找不到稿件: {bvid_or_title}")


@command(app, name='refresh', help='刷新稿件')
async def refresh_archive(
    mid: int = ARG_MID,
    status: str = Option(const.ARCHIVE_STATUS_ALL, help='需要刷新稿件的状态'),
    refresh_page: int = Option(const.MAX_PAGE, help='刷新的页数，默认使用最大'),
    print_data: bool = Option(True, help='打印数据'),
    page_size: int = Option(50, help='每页条数'),
):

    await archive_srv.refresh_archives(
        mid,
        refresh_page=refresh_page,
        page_size=page_size,
    )


@command(app, help='查看稿件')
async def info(
    bvid: str = Argument(help='稿件 bvid'),
    mid: int = OPT_MID,
):
    #  subprocess.run(['open', f'{settings.full_host}/api/archive/{bvid}.json?auth_user_id={mid}'])
    #  bili = get_bili(mid)
    #  archive = bili.find_archive(bvid)
    archive = await archive_srv.find_archive(bvid)
    if not archive:
        print(f"[red]ERROR[/red] 找不到稿件: {bvid}")
        return
    archive.pprint()


@command(app, help='刷新稿件扩展')
def refresh_ext(
    bvid: str = Argument(help='稿件 bvid 或者标题'),
    mid: int = Option(settings.default_auth_user_id, help='授权用户mid'),
    album_id: str = Option(None, help='专辑mid'),
):
    bili = get_bili(mid)
    season_configs = bili.get_season_configs(album_id=album_id)
    album_ids = set([o.album_id for o in season_configs])
    for aid in album_ids:
        m = get_manage(aid, mid)
        m.refresh_archive_ext(bvid)

    # 打印详情
    info(bvid=bvid, mid=mid)


@command(app, help='刷新所有稿件扩展')
def refresh_ext_all(
    mid: int = Option(0, help='授权用户mid'),
    album_id: str = Option(None, help='授权用户mid'),
):
    refresh_archive_ext(user_id=mid, album_id=album_id)
    refresh_episode_archive(user_id=mid)


@command(app, name='pre-upload', help='上传稿件', prompt_fields=['mid'])
def pre_upload(
    video_path: str = Argument(help='视频地址'),
    mid: int = Option(0, help='用户id'),
    season_id: int = Option(None, help='合集id'),
    dtime: str = Option(None, help='预发布时间'),
    tag: str = Option(None, help="标签")
):
    bili = get_bili(mid)
    dirname = os.path.dirname(video_path)
    video_name = os.path.basename(video_path)
    video_name, _ = os.path.splitext(video_name)
    covers = tools.get_episode_split_cover_names(dirname, video_name)
    if not covers:
        logger.error(f"视频: {video_name} 找不到封面，跳过上传")
        return
    cover = os.path.join(dirname, covers[-1])
    # 获取标签
    if not tag:
        season_config = bili.match_title_to_season_config(video_name)
        if season_config:
            album = get_album(season_config.album_id)
            tag = album.title
    if not tag:
        p_error("没有匹配到标签")
        return
    req = ArchiveUploadReqDTO(path=video_path, cover=cover, tag=tag, dtime=dtime)
    bili.pre_upload(req)


@command(app, name='pre-upload-episode', help='预上传剧集分段稿件', prompt_fields=['mid', 'album_id', 'dtime'])
def pre_upload_episode(
    episode_id: str = Argument(help='剧集'),
    mid: int = Option(0, help='用户id'),
    album_id: str = Option('', help='专辑'),
    season_id: int = Option(None, help='合集id'),
    dtime: str = Option(None, help='预发布时间'),
    one_script: bool = Option(True, help='是否一个脚本上传'),
    default_cover: str = Option(None, help='默认封面'),
):
    m = get_manage(album_id, mid)
    # 查找剧集
    episode = m.pm.get_episode_by_id(episode_id)
    if not episode:
        p_error(f"{episode_id} 找不到")
        return

    # 查看视频是否拆分
    split_dirs = tools.get_episode_split_cache_dirs(
        m.bili.auth.bili_name, album_id, episode_id
    )
    if not split_dirs:
        echo(f"ERROR: {episode_id} 还没有拆分")
        return
    split_dir = split_dirs[-1]
    logger.info(f"视频目录: {split_dir}")
    video_names = tools.get_episode_split_video_names(split_dir)
    logger.info(f"待上传视频列表: {video_names}")

    # 判定是否一个脚本执行
    bash_path = ""
    with_to_season = True
    if one_script:
        bash_dir = os.path.join(const.CACHE_DIR, 'bin')
        now = datetime.today().timestamp()
        bash_path = os.path.join(bash_dir, f"upload_{m.bili.auth.bili_name}_{episode_id}_{now}.sh")
        with_to_season = False

    # 上传视频后要执行的脚本
    sleep_s = 10
    after_scripts = [
        f"echo '等待 {sleep_s} 秒钟添加到合集'",
        f"sleep {sleep_s}",
        const.SEASON_REFRESH_CMD.format(mid=mid),
    ]

    logger.info("开始上传视频")
    for video_name in video_names:
        cover = None
        if default_cover:
            cover = default_cover
        else:
            covers = tools.get_episode_split_cover_names(split_dir, video_name)
            if not covers:
                exit(f"视频: {video_name} 找不到封面，跳过上传")
            cover = os.path.join(split_dir, covers[-1])

        logger.info(f"视频: {video_name} 封面地址: {cover}")

        video_path = os.path.join(split_dir, video_name)
        req = ArchiveUploadReqDTO(path=video_path, cover=cover, tag=m.pm.album.title, dtime=dtime)
        m.bili.pre_upload(req, bash_path=bash_path, with_to_season=with_to_season)

        # 添加脚本
        after_scripts.append(const.ACHIVE_REFRESH_ONE_CMD.format(mid=mid, title=req.title))
        after_scripts.append(const.ARCHIVE_REFRESH_EXT_CMD.format(title=req.title, mid=mid))
        after_scripts.append(const.ARCHIVE_TO_SEASON_CMD.format(title=req.title, mid=mid))

    # 添加脚本添加合集内容
    if one_script:
        with open(bash_path, 'a') as f:
            f.write('\n'.join(after_scripts))
            f.write('\n')

        echo("查看生成脚本:")
        subprocess.run(['cat', bash_path])
        echo("")
        echo("")
        echo("脚本地址如下:")
        echo("")
        echo(bash_path)
        echo("")


@command(app, help='添加到合集')
def to_season(
    bvid_or_title: str = Argument(help='视频bvid或者标题'),
    mid: int = OPT_MID,
    season_id: int = Option(0, help='合集id'),
    section_id: int = Option(0, help='小节id'),
):
    bili = get_bili(mid)
    arch = bili.find_archive(bvid_or_title)
    if not arch:
        echo(f"ERROR: {bvid_or_title} 找不到稿件")
        return
    if not arch.cid:
        return
    if not season_id:
        season = bili.find_season(arch.season_title)
        if not season:
            echo(f"ERROR: {arch.season_title} 找不到合集")
            return
        season_id = season.id
    res = bili.add_archive_to_season(arch, season_id, section_id=section_id)
    if res.is_success:
        echo("添加成功")
    else:
        echo("添加失败")
