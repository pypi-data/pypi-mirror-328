#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import os
from typing import List
from bili_cli.music.models import Music, MusicTimeline
from bili_cli.video import ffmpeg_utils


def is_music_file(path) -> bool:
    if os.path.isdir(path):
        return False
    music_set = set(['flac', 'ogg', 'mp3'])
    mname, ext = path.rsplit(".", 1)
    if ext not in music_set:
        return False
    return True


def build_music(dir) -> Music:
    if is_music_file(dir):
        return build_music_by_file(dir)

    def _filter_path(d, func):
        for name in os.listdir(d):
            _path = os.path.join(d, name)
            if func(name):
                return _path
        return ""

    def _build_tl(tl_dir) -> MusicTimeline:
        tl = MusicTimeline()
        dir_name = os.path.basename(tl_dir)
        _, t = dir_name.split('-')
        tl.time = float(t)
        for n in os.listdir(tl_dir):
            _p = os.path.join(tl_dir, n)
            if n.startswith('album'):
                #  print('-')
                tl.album_image = _p
            elif n.endswith('.png') or n.endswith('.jpg'):
                tl.bg_image = _p
        if not tl.bg_image and not tl.album_image:
            raise ValueError(f"{tl_dir} not have image")
        return tl.load()

    def is_music(path: str):
        if path.endswith('.flac') or path.endswith(
                '.mp3') or path.endswith('.ogg'):
            return True
        return False

    path = _filter_path(dir, is_music)
    lrc = _filter_path(dir, lambda x: x.endswith('.lrc'))
    play_type = 'person'
    pt_path = _filter_path(dir, lambda x: x.startswith('play_type'))
    if pt_path:
        play_type = pt_path.split('-')[-1]
    tls = []
    for name in os.listdir(dir):
        _path = os.path.join(dir, name)
        if name.startswith('timeline-'):
            tls.append(_build_tl(_path))
            continue
        elif name.startswith('tl-'):
            tls.append(_build_tl(_path))
            continue

    item = Music(path=path, lrc=lrc)
    item.timelines = tls
    item.play_type = play_type
    # 是否有艺术家
    artist_path = _filter_path(dir, lambda x: x.startswith('artist-'))
    if artist_path:
        item.artist = artist_path.split('-')[-1]
    return item.load()


def build_album_musics(dir: str) -> List[Music]:
    album_image = os.path.join(dir, 'album.png')
    music_set = set(['flac', 'ogg', 'mp3'])
    musics = []
    for name in os.listdir(dir):
        mname, ext = name.rsplit(".", 1)
        if ext not in music_set:
            continue
        path = os.path.join(dir, name)
        lrc_path = os.path.join(dir, f"{mname}.lrc")
        if not os.path.exists(lrc_path):
            continue
        m = Music(path=path, lrc=lrc_path)
        m.timelines = [MusicTimeline(album_image=album_image)]
        m.play_type = 'album'
        m.load()
        musics.append(m)
    return musics


def build_music_by_file(path: str) -> Music:
    dir, name = os.path.split(path)
    basename = name.rsplit('.', 0)
    album_image = os.path.join(dir, f'{basename}.png')
    if not os.path.exists(album_image):
        album_image = os.path.join(dir, 'album.png')
    music_set = set(['flac', 'ogg', 'mp3'])
    mname, ext = name.rsplit(".", 1)
    if ext not in music_set:
        return None
    lrc_path = os.path.join(dir, f"{mname}.lrc")
    if not os.path.exists(lrc_path):
        return None
    m = Music(path=path, lrc=lrc_path)
    m.timelines = [MusicTimeline(album_image=album_image)]
    m.play_type = 'album'
    m.load()
    return m

def make_video_by_music(m: Music) -> str:
    path = os.path.join(
            os.path.dirname(m.path), "frame", 'album', f"{m.get_title()}.mp4")
    rex = os.path.join(m.frame_album_dir, "frame_%d.png")
    print(rex)
    print(path)
    ffmpeg_utils.image_to_mp4(rex, 1, path)


if __name__ == "__main__":
    filepath = '/Volumes/Getea/影片/音乐/周杰伦/八度空间/周杰伦 - 分裂.flac'
    m = build_music_by_file(filepath)
    path = make_video_by_music(m)
    print(path)
    #  m = build_music('/Volumes/Getea/影片/音乐/优秀单曲/绿色')
    #  print(m.path)
    #  print(m.lrc)
    #  print(m.play_type)
    #  for tl in m.timelines:
    #  print(tl)
    #  print(tl.time, tl.bg_image)

    #  items = musics = build_album_musics('/Volumes/Getea/影片/音乐/周杰伦/JAY')
    #  for item in items:
        #  print(item)
