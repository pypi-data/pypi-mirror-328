#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
import time
from datetime import datetime
from typing import Optional, Self
from bili_cli.base import PrettyModel
from pydantic import Field


class BaseORM(PrettyModel):
    id: str = Field("", title="视频id")
    is_delete: int = Field(0, title="是否删除")
    db_path: str = Field("", title="数据地址", exclude=True)
    create_time: Optional[datetime] = Field(default_factory=datetime.now, title="创建时间")
    update_time: Optional[datetime] = Field(default_factory=datetime.now, title="创建时间")

    class Meta():
        TABLE = ""
        DB = "bilibili"

    def get_id(self) -> str:
        return str(self.id)

    def get_save_data(self) -> dict:
        return self.dict()

    @classmethod
    def create_id(cls) -> str:
        return str(int(time.time() * 1000))

    def enable_delete(self) -> Self:
        """使用防刷屏"""
        self.is_delete = 1
        return self
