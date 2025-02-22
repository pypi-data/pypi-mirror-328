#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import time
import subprocess
import os
from urllib.parse import urlparse
from typing import Callable, Dict, Any
from datetime import timedelta, datetime
from functools import wraps
from .loggers import logger
from bili_cli import const
from inspect import signature


def format_duration(duration: float) -> str:
    return str(timedelta(seconds=round(float(duration))))


def build_episode_id(season: int, ep, s_count=2, ep_count=2):
    return f"S{season:0>2}E{ep:0>2}"


def make_pagination(
    total_items: list, page: int = 1, pagesize: int = 10,
    page_func: Callable = None, sort: str = "+order", items_name: str = 'items'
):
    start = (page-1) * pagesize
    end = start + pagesize
    # 排序
    is_reverse = False
    if sort.startswith("-"):
        is_reverse = True
    if sort:
        sort_name = sort.replace("-", "").replace("+", "")
        total_items.sort(key=lambda o: getattr(
            o, sort_name), reverse=is_reverse)
    items = total_items[start:end]

    if page_func:
        page_func(items)

    res = {
        "data": {
            items_name: items,
            "total": len(total_items)
        }
    }
    return res


def time_statistics(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录函数开始执行的时间
        logger.info(f"{func.__name__} begin at {datetime.now()}")
        result = func(*args, **kwargs)  # 执行函数
        end_time = time.time()  # 记录函数执行结束的时间
        logger.info(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper


def show_in_finder(path: str):
    logger.info(f"open path: {path}")
    if os.path.exists(path):
        cmds = ["open", "-R", path]
        subprocess.run(cmds, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return True
    return False


def get_episode_split_cache_dirs(bili_name: str, album_id: str, episode_id: str) -> list:
    '''获取剧集分割缓存目录列表'''
    prefix = f"{bili_name}-{episode_id}-{album_id}-"
    dirs = []
    for name in os.listdir(const.CACHE_DIR):
        if not name.startswith(prefix):
            continue
        dirs.append(os.path.join(const.CACHE_DIR, name))
    dirs.sort()
    return dirs


def get_episode_split_video_names(cache_dir: str) -> list:
    '''获取视频分割的视频名称列表'''
    names = []
    for video_name in os.listdir(cache_dir):
        if not video_name.endswith('.mp4'):
            continue
        names.append(video_name)
    names.sort()
    return names


def get_episode_split_cover_names(cache_dir: str, video_name: str) -> list:
    '''获取视频分割的视频封面名称列表'''
    if video_name.endswith(".mp4"):
        video_name, _ = os.path.splitext(video_name)
    names = []
    for name in os.listdir(cache_dir):
        if not name.endswith('.png'):
            continue
        if not name.startswith(video_name):
            continue
        names.append(name)
    names.sort()
    return names


def get_func_params_default(func) -> Dict[str, Any]:
    sig = signature(func)
    data = {}
    for key, value in sig.parameters.items():
        data[key] = value.default
    return data


def get_bvid_from_url(url: str):
    parse = urlparse(url)
    paths = parse.path.split('/')
    for item in paths:
        if item.startswith('BV'):
            return item
    return None
