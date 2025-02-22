#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from typing import Union
from pydantic import Field, BaseModel


class PartConfig(BaseModel):
    album_id: str = Field(title="专辑")
    max_duration: int = Field(0, title="最大时长")

    @classmethod
    def build(cls, album_id: str, max_duration: int = 0):
        return cls(
            album_id=album_id,
            max_duration=max_duration
        )


TypeRandPart = Union[str, dict, PartConfig]
