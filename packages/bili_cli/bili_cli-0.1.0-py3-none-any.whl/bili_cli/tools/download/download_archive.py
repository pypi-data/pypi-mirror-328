#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import os.path
import sys
import requests
from concurrent.futures import ThreadPoolExecutor
import signal
from functools import partial
from threading import Event
from typing import Iterable

from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)
from bili_cli.const import COMMON_HEADERS
from bili_cli.dtos import PlayerUrlResDTO
from bili_cli.video.ffmpeg_utils import concat_audio_to_video
from .dtos import DownloadArchiveReq

progress = Progress(
    TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
    BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    DownloadColumn(),
    "•",
    TransferSpeedColumn(),
    "•",
    TimeRemainingColumn(),
)


done_event = Event()


def handle_sigint(signum, frame):
    done_event.set()


signal.signal(signal.SIGINT, handle_sigint)


def download_url(task_id: TaskID, url: str, path: str) -> None:
    """Copy data from a url to a local file."""
    res = requests.get(url, headers=COMMON_HEADERS, stream=True)
    if res.status_code != 200:
        progress.stop_task(task_id)
        return
    content_length = res.headers['Content-length']
    progress.update(task_id, total=int(content_length))
    with open(path, "wb") as dest_file:
        progress.start_task(task_id)
        for chunk in res.iter_content(chunk_size=128*1024):
            if chunk:
                dest_file.write(chunk)
            progress.update(task_id, advance=len(chunk))
            if done_event.is_set():
                return
    progress.console.log(f"Downloaded {path}")


def download_and_merge(player: PlayerUrlResDTO, download_dir: str, filename: str):
    video_filename = f"{filename}.mp4"
    video_path = os.path.join(download_dir, video_filename)
    task_id = progress.add_task("download_video", filename=video_filename, start=False)
    download_url(task_id, player.dash.video[0].base_url, video_path)

    audio_filename = f"{filename}.mp3"
    audio_path = os.path.join(download_dir, audio_filename)
    task_id = progress.add_task("download_audio", filename=audio_filename, start=False)
    download_url(task_id, player.dash.audio[0].base_url, audio_path)

    concat_audio_to_video(
            video_path,
            audio_path,
            os.path.join(download_dir, filename),)

    os.remove(video_path)
    os.remove(audio_path)


def download_archive(req: DownloadArchiveReq):
    if req.resolution == '1080p':
        download_and_merge(req.player, req.download_dir, req.get_filename())
    else:
        video_filename = req.get_filename()
        video_path = os.path.join(req.download_dir, video_filename)
        task_id = progress.add_task("download_video", filename=video_filename, start=False)
        download_url(task_id, req.player.default_url, video_path)
