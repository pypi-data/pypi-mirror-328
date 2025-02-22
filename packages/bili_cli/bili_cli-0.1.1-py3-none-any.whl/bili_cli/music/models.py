#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import pydantic
import pygame
import os
import cv2
from typing import List
from pydantic import model_validator
from pylrc.classes import LyricLine
from pygame.surface import Surface

from bili_cli.base import BaseModel
from bili_cli import mod
from .tools import build_audio_info
from .lrc import get_lrc_lines


class MusicTimeline(BaseModel):
    bg_image: str = pydantic.Field("", title="背景图片")
    bg_image_sur: Surface = pydantic.Field(None)
    album_image: str = pydantic.Field("", title="背景图片")
    album_image_sur: Surface = pydantic.Field(None)
    font: str = pydantic.Field("pingfang", title='字体')
    time: float = pydantic.Field(0, title="时间点")

    def load(self, screen_w: int = 0, screen_h: int = 0) -> 'MusicTimeline':
        if self.bg_image:
            self.bg_image_sur = pygame.image.load(self.bg_image)
        if self.album_image:
            self.album_image_sur = pygame.image.load(self.album_image)
            if screen_w:
                album_w = screen_w / 4
                self.album_image_sur = pygame.transform.scale(
                        self.album_image_sur, (album_w, album_w))
            if not self.bg_image:
                self.bg_image_sur = self.album_image_sur
                if screen_w:
                    sur = pygame.transform.scale(self.album_image_sur,
                                                (screen_w, screen_w))
                    # 获取图像的像素数据
                    #  pixels = pygame.surfarray.array3d(sur)
                    image_array = pygame.surfarray.array3d(sur)

                    # 将numpy数组转换为OpenCV图像
                    image_opencv = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)

# 对OpenCV图像应用高斯模糊
                    gb = 195
                    blurred_image_opencv = cv2.GaussianBlur(image_opencv, (gb, gb), 0)

# 将OpenCV图像转换回numpy数组
                    blurred_image_array = cv2.cvtColor(blurred_image_opencv, cv2.COLOR_BGR2RGB)

# 将numpy数组转换回Pygame图像
                    sur = pygame.surfarray.make_surface(blurred_image_array)
                    self.bg_image_sur = sur
        else:
            self.album_image_sur = pygame.image.load(self.bg_image)
        return self


class Music(BaseModel):
    title: str = pydantic.Field('', title="名称")
    album: str = pydantic.Field('', title="名称")
    artist: str = pydantic.Field('', title="名称")
    path: str = pydantic.Field(title="地址")
    play_type: str = pydantic.Field('', title="播放类型")
    lrc: str = pydantic.Field("", title="歌词")
    lyric_lines: List[LyricLine] = pydantic.Field([])
    timelines: List[MusicTimeline] = pydantic.Field([])
    info: mod.AudioInfoModel = pydantic.Field(None, title='详细信息')
    frame_album_dir: str = pydantic.Field("", title="专辑帧图存放文件夹")

    def load(self) -> 'Music':
        self.info = build_audio_info(self.path)
        if self.lrc:
            self.lyric_lines = get_lrc_lines(self.lrc)

        timelines = self.timelines
        tl_last: MusicTimeline = timelines[-1]
        tl_e = MusicTimeline(
            bg_image=tl_last.bg_image,
            album_image=tl_last.album_image,
            font=tl_last.font,
            time=20 * 60
        ).load()
        self.timelines.append(tl_e)
        self.frame_album_dir = os.path.join(
                os.path.dirname(self.path), "frame", 'album', self.get_title())
        return self

    def get_title(self):
        return self.title or self.info.title

    def get_album(self):
        return self.album or self.info.album

    def get_artist(self):
        return self.artist or self.info.artist

    def get_lyric_line(self, time: float) -> LyricLine:
        count = len(self.lyric_lines)
        for i in range(count):
            j = i+1
            if j == count:
                break
            s = self.lyric_lines[i]
            e = self.lyric_lines[j]
            if s.time <= time and time < e.time:
                return s
        return None

    def get_timeline(self, time: float) -> MusicTimeline:
        main_tl = self.timelines[0]
        tl = MusicTimeline(
            bg_image_sur=main_tl.bg_image_sur,
            bg_image=main_tl.bg_image,
            album_image=main_tl.album_image,
            album_image_sur=main_tl.album_image_sur,
            time=time
        )
        tl_count = len(self.timelines)
        for i in range(tl_count):
            j = i+1
            if j == tl_count:
                break
            tl_s = self.timelines[i]
            tl_e = self.timelines[j]
            if tl_s.time <= time and time < tl_e.time:
                if tl_s.bg_image_sur:
                    tl.bg_image_sur = tl_s.bg_image_sur
                    tl.bg_image = tl_s.bg_image
                    tl.album_image = tl_s.album_image
                    tl.album_image_sur = tl_s.album_image_sur
                tl.time = time
                break

        return tl
