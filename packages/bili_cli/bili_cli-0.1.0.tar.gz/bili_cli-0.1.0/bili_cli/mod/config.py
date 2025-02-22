#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from pydantic import Field, SkipValidation
from typing import Any
from bili_cli.base import BaseMongoORM


class ConfigModel(BaseMongoORM):
    key: str = Field(title="配置 key")
    data: SkipValidation[Any] = Field(None, title="内容")

    class Meta(BaseMongoORM.Meta):
        TABLE = "config"

    def get_id(self):
        return str(self.key)

    @classmethod
    def table_headers(cls) -> list:
        return ['key', 'data']
