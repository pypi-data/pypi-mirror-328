#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from pydantic import Field
from typing import List
from .base import ApiListResDTO
from ..mod import ReplyModel


class GetReplysResDTO(ApiListResDTO):
    data: List[ReplyModel] = Field([], title='请求列表')
