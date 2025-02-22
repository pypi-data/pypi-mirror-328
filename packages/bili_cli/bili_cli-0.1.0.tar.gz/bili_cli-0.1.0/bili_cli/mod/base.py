#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import pydantic
from bili_cli.base import BaseModel


class BaseEpisode(BaseModel):
    album_id: str = pydantic.Field("", title="专辑")
    episode_id: str = pydantic.Field("", title="专辑")
    season: int = pydantic.Field(1, title="")
    ep: int = pydantic.Field(0, title="集数，数值")

