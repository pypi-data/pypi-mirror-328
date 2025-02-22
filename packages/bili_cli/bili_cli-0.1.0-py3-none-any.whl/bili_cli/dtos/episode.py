#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from pydantic import Field
from typing import List
from .base import ApiListResDTO
from ..mod import EpisodeModel


class GetEpisodesResDTO(ApiListResDTO):
    data: List[EpisodeModel] = Field([], title='请求列表')
