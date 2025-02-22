#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import pydantic
import pygame
import scipy
import cv2
import os
from scipy.ndimage import gaussian_filter
from pygame.color import Color
#  import copy
from enum import Enum
from typing import Union, Tuple, List
from pygame.surface import Surface
from pygame.font import Font as F
from bili_cli.base import BaseModel
from bili_cli import types
from . import color, fonts
from .models import Music, MusicTimeline
from .AudioAnalyzer import AudioAnalyzer

pygame.init()

ColorValue = Union[Color, int, str, Tuple[int, int, int]]


class Circle(BaseModel):
    x: int = pydantic.Field(title='横坐标')
    y: int = pydantic.Field(title='竖坐标')
    min_radius: int = pydantic.Field(200, title='最小半径')
    max_radius: int = pydantic.Field(250, title='最大半径')


class DisplaySizeType(Enum):
    CENTER = 'center'


Size = Tuple[float, float]
Point = Tuple[float, float]


class Font(BaseModel):
    font: str = pydantic.Field(fonts.FONT_SS)
    size: int = pydantic.Field()
    color: ColorValue = pydantic.Field((255, 255, 255))
    f: F = pydantic.Field(None)
    sur: Surface = pydantic.Field(None)

    def load(self) -> 'Font':
        self.f = F(self.font, self.size)
        #  self.f.bold = True
        return self

    def render(self, text: str) -> Surface:
        if not self.f:
            self.load()
        return self.f.render(text, True, self.color)


class Screen(BaseModel):
    w: float = pydantic.Field()
    h: float = pydantic.Field()
    sur: Surface = pydantic.Field(None)

    def load(self) -> 'Screen':
        self.sur = pygame.display.set_mode([self.w, self.h])
        return self


class Template(BaseModel):
    title_font: Font = pydantic.Field(None)
    artist_font: Font = pydantic.Field(None)
    time_font: Font = pydantic.Field(None)
    lrc_font: Font = pydantic.Field(None)


text_color = (139, 0, 139)
#  text_color = (0, 139, 139)
text_color = color.COLOR_WHITE

CIRCLE_TEMPL = Template(
    title_font=Font(size=80, color=text_color).load(),
    artist_font=Font(size=30, color=text_color).load(),
    time_font=Font(size=30, color=text_color).load(),
    lrc_font=Font(size=50, color=text_color).load(),
)
VERTICAL_TEXT_COLOR = color.COLOR_WHITE
VERTICAL_TEMPL = Template(
    title_font=Font(size=80, color=VERTICAL_TEXT_COLOR).load(),
    artist_font=Font(size=30, color=VERTICAL_TEXT_COLOR).load(),
    time_font=Font(size=30, color=VERTICAL_TEXT_COLOR).load(),
    lrc_font=Font(size=50, color=VERTICAL_TEXT_COLOR).load(),
)

_AUDIO_ANALYZER_MAP = {}


def get_or_create_analyzer(path, md5) -> AudioAnalyzer:
    cache = _AUDIO_ANALYZER_MAP.get(md5)
    if not cache:
        analyzer = AudioAnalyzer()
        analyzer.load(path)
        _AUDIO_ANALYZER_MAP[md5] = analyzer
    return _AUDIO_ANALYZER_MAP[md5]


class MusicPlayer(BaseModel):
    circle: Circle = pydantic.Field(None)
    screen: Screen = pydantic.Field()
    musics: List[Music] = pydantic.Field([], title='音乐')
    templ: Template = pydantic.Field(None, title="模板")
    play_index: int = pydantic.Field(0, title="播放索引")
    start_time: float = pydantic.Field(0, title="播放开始时间")

    @classmethod
    def build(
        cls, display_size: Union[Size, DisplaySizeType],
        musics: List[Music]
    ) -> 'MusicPlayer':
        screen_size = display_size
        screen = Screen(w=screen_size[0], h=screen_size[1]).load()

        circle_x = int(screen_size[0]/2)
        circle_y = int(screen_size[1]/2)
        min_r = int(screen_size[1]/2 * 0.8)
        max_r = min_r + 50
        c = Circle(x=circle_x, y=circle_y, min_radius=min_r, max_radius=max_r)

        item = cls(
            screen=screen,
            circle=c,
            musics=musics,
            templ=CIRCLE_TEMPL,
        )
        #  item.start_time = 200

        return item

    def get_play_time(self) -> float:
        pos = pygame.mixer.music.get_pos()
        if pos == -1:
            return self.get_cur_music().info.duration
        return pos / 1000.0 + self.start_time

    def get_play_progress(self) -> float:
        play_time = self.get_play_time()
        progress =  play_time / self.get_cur_music().info.duration
        #  print(f"播放时间: {play_time} 进度: {progress}")
        return progress

    def get_cur_music(self) -> Music:
        return self.musics[self.play_index]

    def get_cur_analyzer(self) -> AudioAnalyzer:
        m = self.get_cur_music()
        return get_or_create_analyzer(m.path, m.info.md5)

    def load_cur_music(self, play_type=''):
        cur_music = self.get_cur_music()
        if not play_type:
            play_type = cur_music.play_type
        if play_type == 'album':
            for tl in cur_music.timelines:
                tl.load(screen_w=self.screen.w)

    def play(self, play_type=''):
        cur_music = self.get_cur_music()
        # 创建图片文件夹
        #  self.load_music(cur_music, play_type=play_type)
            #  self.draw_album()
        if not os.path.exists(cur_music.frame_album_dir):
            os.makedirs(cur_music.frame_album_dir)
        pygame.mixer.music.load(cur_music.path)
        pygame.mixer.music.play(0, start=self.start_time)

    def save_play_album_frame(self):
        cur_music = self.get_cur_music()
        play_second = int(self.get_play_time())
        image_path = os.path.join(
                cur_music.frame_album_dir, f"frame_{play_second}.png")
        pygame.image.save(self.screen.sur, image_path)

    def is_play_finish(self) -> bool:
        return self.get_play_progress() == 1

    def cut(self):
        if self.play_index + 1 < len(self.musics):
            self.play_index += 1
            self.start_time = 0
            self.load_cur_music()
            self.play()

    def draw_bg(self):
        m = self.get_cur_music()
        tl = m.get_timeline(self.get_play_time())
        #  print(tl.time, self.get_play_progress())
        #  scaled_image = pygame.transform.scale(tl.bg_image_sur, (1280, 720))
        #  self.screen.sur.blit(scaled_image, (0, 0))
        self.screen.sur.blit(tl.bg_image_sur, tl.bg_image_sur.get_rect())

        mid_h = self.screen.h/2

        up_h = mid_h

        music = self.get_cur_music()
        text = music.get_artist()
        if text:
            _, s_h = self.draw_text_mid(
                self.templ.artist_font, music.get_artist(), up_h
            )
            up_h = s_h

        text = music.get_title()
        if text:
            _, t_h = self.draw_text_mid(
                self.templ.title_font, music.get_title(), up_h
            )

        # 歌词
        lyric_line = music.get_lyric_line(self.get_play_time())
        if lyric_line:
            text = lyric_line.text
            _, t_h = self.draw_text_mid(
                self.templ.lrc_font, text, mid_h, is_up=False
            )

        self.draw_progress()

    def draw_album_image(self, tl: MusicTimeline):
        sur = tl.album_image_sur
        bg_w, bg_h = sur.get_size()
        bg_x = self.screen.w / 4 - bg_w/2
        bg_y = self.screen.h / 2 - bg_h/2

        self.screen.sur.blit(sur, (bg_x, bg_y))

    def draw_album_bg_image(self, tl: MusicTimeline):

        sur = tl.bg_image_sur
        w = 0
        h = self.screen.h / 2 - sur.get_height() / 2
        self.screen.sur.blit(sur, (w, h))

    def draw_album(self):
        """专辑模式"""
        m = self.get_cur_music()
        tl = m.get_timeline(self.get_play_time())
        #  print(tl)
        #  print(tl.time, self.get_play_progress())

        self.draw_album_bg_image(tl)
        self.draw_album_image(tl)

        mid_h = self.screen.h/2

        up_h = mid_h
        text_w_offset = self.screen.w / 4

        music = self.get_cur_music()
        text = music.get_artist()
        if text:
            _, s_h = self.draw_text_mid(
                self.templ.artist_font, music.get_artist(), up_h,
                w_offset=text_w_offset,
            )
            up_h = s_h

        text = music.get_title()
        if text:
            _, t_h = self.draw_text_mid(
                self.templ.title_font, music.get_title(), up_h,
                w_offset=text_w_offset,
            )

        # 歌词
        lyric_line = music.get_lyric_line(self.get_play_time())
        if lyric_line:
            text = lyric_line.text
            _, t_h = self.draw_text_mid(
                self.templ.lrc_font, text, mid_h, is_up=False,
                w_offset=text_w_offset,
            )

        self.draw_progress(w_offset=text_w_offset)

    def draw_text_mid(self, font: Font, text, h: int, is_up=True, margin=10, w_offset: float = 0):

        # 绘制文本
        fw, fh = font.f.size(text)
        fx = self.screen.w/2 - (fw/2) + w_offset
        if is_up:
            fy = h - fh - margin
        else:
            fy = h + margin
        # 绘制阴影
        offset = font.size // 15 + 1
        offset = 1
        #  drop_font = Font(size=font.size, color=(128,128,128)).load()
        drop_font = Font(size=font.size, color=color.COLOR_BLACK).load()
        self.screen.sur.blit(drop_font.render(
            text), (fx + offset, fy + offset))

        # 绘制文本
        self.screen.sur.blit(font.render(text), (fx, fy))

        return fx, fy

    def draw_progress(self, w_offset: float = 0):
        mid_h = self.screen.h/2
        line_s = self.screen.w/2 - self.circle.min_radius + 10 + w_offset
        line_e = self.screen.w/2 + self.circle.min_radius - 10 + w_offset
        line_w = line_e - line_s
        point_s = (line_s, mid_h)
        point_e = (line_e, mid_h)
        pygame.draw.aaline(self.screen.sur, (0, 255, 255),
                           point_s, point_e, blend=1)

        # 进度
        p_r = 5
        progress_x = line_s + line_w * self.get_play_progress() + (p_r/2)
        pygame.draw.circle(self.screen.sur, color.COLOR_SKY_BLUE1,
                           (progress_x, mid_h), p_r)

        # 时间
        m = self.get_cur_music()
        play_d = types.Duraction(self.get_play_time())
        play_d_t = str(play_d)
        if play_d > 0:
            play_d_t = play_d_t[2:]
        total_dur = str(m.info.dur)
        if m.info.duration > 0:
            total_dur = total_dur[2:]
        time_text = f"{play_d_t}/{total_dur}"
        time_font = self.templ.time_font
        fw, fh = time_font.f.size(time_text)
        tx = line_w + line_s - fw
        ty = mid_h - fh - 10
        # 绘制阴影
        offset = time_font.size // 15 + 1
        offset = 1
        #  drop_font = Font(size=font.size, color=(128,128,128)).load()
        drop_font = Font(size=time_font.size, color=color.COLOR_BLACK).load()
        self.screen.sur.blit(drop_font.render(
            time_text), (tx + offset, ty + offset))

        # 绘制时间
        self.screen.sur.blit(time_font.render(time_text), (tx, ty))


if __name__ == "__main__":
    import time
    b = time.time()
    filename = "/Users/wxnacy/Music/爱情公寓歌曲/靠近-罗震环.mp3"
    #  m = Music(
    #  name=filename,
    #  path=filename,
    #  timelines=[
    #  MusicTimeline(
    #  bg_image='/Users/wxnacy/Movies/视频制作/电视剧/爱情公寓/插曲合集/靠近1.jpeg', time=0),
    #  MusicTimeline(
    #  bg_image='/Users/wxnacy/Movies/视频制作/电视剧/爱情公寓/插曲合集/靠近2.png', time=5),
    #  ]
    #  ).load()
    #  for t in range(7):

    e = time.time()
    print(e-b)
