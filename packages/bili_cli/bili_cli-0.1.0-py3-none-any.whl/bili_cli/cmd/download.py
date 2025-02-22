#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
import os
import requests
from typer import (
    Argument,
    Option,
)
from bili_cli.bili import get_bili
from bili_cli.const import COMMON_HEADERS
from bili_cli.tools import get_bvid_from_url
from bili_cli.dtos import Durl
from bili_cli.tools.download import (
    download_archive,
    DownloadArchiveReq
)
from .base import OPT_MID, exit


def default_dl_dir():
    return os.path.expanduser("~/Downloads")


def download(
    url_or_bvid: str = Argument(help='URL 或者 BVID'),
    mid: int = OPT_MID,
    download_dir: str = Option(..., '-d', '--download-dir', help='下载目录', default_factory=default_dl_dir),
    resolution: str = Option('1080p', '-r', '--resolution', help='分辨率')
):
    bili = get_bili(mid)
    bvid = url_or_bvid
    if url_or_bvid.startswith("http"):
        bvid = get_bvid_from_url(url_or_bvid)
    if not bvid:
        exit("获取不到 bvid")
    print(f"开始查询视频: {bvid}")
    arch = bili.get_archive_info(url_or_bvid)
    print(f"视频名称: {arch.title}")
    if arch.videos == 1:
        # 下载单个视频
        cid = arch.cid
        play_info = bili.get_player_url(arch.bvid, cid, resolution=resolution)
        filename = f"{arch.title}.mp4"

        req = DownloadArchiveReq(
            resolution=resolution,
            archive=arch,
            player=play_info,
            download_dir=download_dir
        )
        download_archive(req)
    else:
        download_dir = os.path.join(download_dir, arch.title)
        print(download_dir)
        try:
            os.mkdir(download_dir)
        except Exception:
            pass
        for p in arch.pages:
            cid = p.cid
            play_info = bili.get_player_url(arch.bvid, cid, resolution=resolution)
            filename = f"{p.part}.mp4"
            req = DownloadArchiveReq(
                resolution=resolution,
                archive=arch,
                player=play_info,
                download_dir=download_dir,
                filename=filename
            )
            download_archive(req)


def download_mp4(durl: Durl, path: str):
    if os.path.exists(path) and os.path.getsize(path) == durl.size:
        print(f"文件已存在，且下载完成: {path}")
        return

    print(f"开始下载文件到: {path}")
    url = durl.url
    res = requests.get(url, headers=COMMON_HEADERS, stream=True)
    # 检查请求是否成功
    if res.status_code == 200:
        # 打开一个文件用于写入二进制数据
        with open(path, 'wb') as file:
            # 以128KB的块写入文件
            for chunk in res.iter_content(chunk_size=128*1024):
                if chunk:  # 过滤掉保持连接的chunk
                    file.write(chunk)
        print("视频下载完成")
    else:
        print(f"下载失败，状态码：{res.status_code}")
