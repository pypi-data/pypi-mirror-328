#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:


import pydantic
from bili_cli.base import BaseORM
from bili_cli.types import Duraction


class AudioInfoModel(BaseORM):
    title: str = pydantic.Field("")
    album: str = pydantic.Field("")
    artist: str = pydantic.Field("")
    date: str = pydantic.Field("")
    md5: str = pydantic.Field()
    duration: float = pydantic.Field(0)
    sample_rate: int = pydantic.Field(0)
    #  dur: str = pydantic.Field(None, title="长度可视化")

    class Meta():
        TABLE = "audio_info"
        DB = 'common'

    def get_id(self):
        return self.md5

    #  @model_validator(mode='before')
    #  def validator_all(cls, values):
        #  values['dur'] = str(timedelta(
        #  seconds=math.floor(float(values['duration']))))
        #  return values

    @property
    def dur(self):
        """The dur property."""
        return Duraction(self.duration)
