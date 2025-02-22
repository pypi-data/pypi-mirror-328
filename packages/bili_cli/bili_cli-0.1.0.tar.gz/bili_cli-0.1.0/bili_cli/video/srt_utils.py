#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import pysrt
import wpy
from pysrt.srtitem import SubRipItem, SubRipTime
from pysrt.srtfile import SubRipFile
from bili_cli.video.models import SubtitlePart, Subtitle
from datetime import timedelta
from pypinyin import lazy_pinyin


def srt_to_timedelta(t: SubRipTime) -> timedelta:
    return timedelta(
        hours=t.hours, minutes=t.minutes,
        seconds=t.seconds, milliseconds=t.milliseconds)


def srt_to_part(sub: SubRipItem, ahead_seconds=0) -> SubtitlePart:
    start = srt_to_timedelta(sub.start) - timedelta(seconds=ahead_seconds)
    td = sub.end - sub.start
    t = srt_to_timedelta(td) - timedelta(seconds=ahead_seconds)
    return SubtitlePart.load(sub.text, start, t)


def get_subtitle(path: str, with_pinyin=False) -> Subtitle:
    sub = pysrt.open(path)
    for i, d in enumerate(sub.data):
        if with_pinyin:
            sub.data[i].text += "\n" + ''.join(lazy_pinyin(d.text))
    s = Subtitle(srt=sub)
    s.md5 = wpy.md5file(path)
    return s


def search_srt_parts(
        sub: str  | Subtitle, keywords: list) -> SubtitlePart:
    if isinstance(sub, str):
        sub = get_subtitle(sub, True)
        srt = sub.srt
        video = sub.video
    elif isinstance(sub, Subtitle):
        srt = sub.srt
        video = sub.video
    #  print(video)
    data: SubRipItem
    res = []
    for data in srt.data:
        for key in keywords:
            key_pinyin = ''.join(lazy_pinyin(key))
            if key in data.text or key_pinyin in data.text:
                part = srt_to_part(data)
                part.video = video
                #  print(part)
                res.append(part)
                break
    return res




if __name__ == "__main__":
    path = "/Users/wxnacy/Movies/电视剧/爱情公寓2/S02E02.srt"
    sub = get_subtitle(path)
    print(sub.dict())
    import pickle

    with open('/Users/wxnacy/Downloads/test.pickle', 'wb') as f:
        # 序列化对象到一个data.pickle文件中
        # 指定了序列化格式的版本pickle.HIGHEST_PROTOCOL
        pickle.dump(sub, f, pickle.HIGHEST_PROTOCOL)

    with open('/Users/wxnacy/Downloads/test.pickle', 'rb') as f:
    # 从data.pickle文件中反序列化对象
    # pickle能够自动检测序列化文件的版本
    # 所以这里可以不用版本号
        data = pickle.load(f)
        print(data.md5)

    #  search_srt_parts(
        #  "/Users/wxnacy/Movies/电视剧/爱情公寓2/S02E02.srt", ["计划", "羽墨"])
    #  print(lazy_pinyin(["你好", "哈哈"]))
