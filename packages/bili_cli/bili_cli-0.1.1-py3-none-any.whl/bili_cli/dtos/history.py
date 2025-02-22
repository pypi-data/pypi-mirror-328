#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from pydantic import Field
from typing import List
from .base import ApiListResDTO
from ..mod import RequestHistory


class RequestHistoryListResDTO(ApiListResDTO):
    data: List[RequestHistory] = Field([], title='请求列表')
