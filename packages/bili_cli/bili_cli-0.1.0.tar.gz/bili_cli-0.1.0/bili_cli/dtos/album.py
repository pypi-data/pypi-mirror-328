#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from pydantic import Field
from typing import List
from .base import ApiListResDTO
from bili_cli.config.album import AlbumConfig


class GetAlbumsResDTO(ApiListResDTO):
    data: List[AlbumConfig] = Field([], title='请求列表')
