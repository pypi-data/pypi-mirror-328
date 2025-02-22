#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:


from bili_cli import mod
from bili_cli.tools.hash import md5_file
import mutagen


def get_music_metadata(info, name):
    def _hand_list(items):
        if len(items) > 1:
            return ' '.join(items)
        else:
            return str(items[0])

    value = info.tags.get(name)
    print(name, value)
    if not value:
        return ""
    if isinstance(value, list):
        return _hand_list(value)
    if isinstance(value, mutagen.id3.TextFrame):
        return _hand_list(value.text)
    return ""


def build_audio_info(path, md5: str = "") -> mod.AudioInfoModel:
    if not md5:
        md5 = md5_file(path)
    info = mod.AudioInfoModel.find_by_id(md5)
    if not info:
        info = mod.AudioInfoModel(md5=md5)
    ma_info = mutagen.File(path)
    print(ma_info.tags)
    info.duration = ma_info.info.length

    info.album = get_music_metadata(
            ma_info, 'TALB') or get_music_metadata(ma_info, 'Album')
    info.title = get_music_metadata(
            ma_info, 'TIT2') or get_music_metadata(ma_info, 'Title')
    info.artist = get_music_metadata(
            ma_info, 'TPE1') or get_music_metadata(ma_info, 'Artist')
    info.date = get_music_metadata(ma_info, 'TDRC')
    info.save()

    return info


#  if __name__ == "__main__":
    #  path = '/Users/wxnacy/Downloads/就是我.flac'
    #  path = '/Users/wxnacy/Downloads/开不了口.aiff'
    #  path = '/Users/wxnacy/Downloads/虹之间.mp3'
    path = '/Volumes/Getea/影片/音乐/爱情公寓/靠近/罗震环-靠近.flac'
    path = '/Volumes/Getea/Downloads/贾玲 - 一切都来得及.ogg'
    info = build_audio_info(path)
    print(info)
