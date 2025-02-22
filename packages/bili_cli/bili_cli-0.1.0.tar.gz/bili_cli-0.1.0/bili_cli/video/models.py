#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
import pydantic
from pydantic import model_validator
from datetime import timedelta, datetime
from pysrt.srtfile import SubRipFile
from bili_cli.base import BaseModel


class Part(BaseModel):
    start: timedelta = pydantic.Field(title="开始时间")
    time: timedelta = pydantic.Field(title="时长")

    @model_validator(mode='before')
    def validator_all(cls, values):
        for key in ['start', 'time']:
            t = values.get(key)
            if isinstance(t, int):
                values[key] = timedelta(seconds=t)
            elif isinstance(t, str):
                dt = datetime.strptime(t, "%H:%M:%S")
                values[key] = timedelta(
                    hours=dt.hour, minutes=dt.minute, seconds=dt.second)
        return values

    @classmethod
    def load(cls, start, time) -> 'Part':
        return cls(start=start, time=time)

    def __sub__(self, small_one: 'Part') -> 'Part':
        if self.start < small_one.start:
            raise ValueError(f"{small_one} must lt {self}")
        if self.start == small_one.start:
            return None
        small_one_end = small_one.start.seconds + small_one.time.seconds
        return Part.load(small_one_end, self.start.seconds - small_one_end)

    def __eq__(self, other: 'Part') -> bool:
        return self.start.seconds == other.start.seconds and \
            self.time.seconds == other.time.seconds


class SubtitlePart(Part):
    video: str = pydantic.Field("", title="视频")
    text: str = pydantic.Field(title="内容")

    @classmethod
    def load(cls, text, start, time) -> 'SubtitlePart':
        return cls(text=text, start=start, time=time)


class Subtitle(BaseModel):
    srt: SubRipFile = pydantic.Field(title="字幕")
    md5: str = pydantic.Field("", title="原始文件md5")
    video: str = pydantic.Field("", title="视频")
