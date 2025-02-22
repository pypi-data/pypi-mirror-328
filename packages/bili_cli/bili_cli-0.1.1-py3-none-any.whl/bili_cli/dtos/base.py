#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from pydantic import Field
from bili_cli.base import BaseModel
from ..dto import *


class ApiListResDTO(BaseModel):
    data: list = Field([], title="数据")
    total: int = Field(0, title="总数")
