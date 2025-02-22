#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from typing import Optional, List
from pydantic import Field
from bili_cli.base import BaseMongoORM, BaseModel


class RequestModel(BaseModel):
    path: str = Field("", title="路径")
    params: Optional[dict] = Field({}, title="请求参数")
    data: Optional[dict] = Field({}, title="请求参数")
    headers: dict = Field({}, title="头信息")
    cookies: dict = Field({}, title="Cookies")


class ResponseModel(BaseModel):
    data: Optional[dict] = Field({}, title="请求参数")
    text: str = Field('', title="返回结果")
    content: bytes = Field('', title="返回结果")
    headers: dict = Field({}, title="头信息")
    cookies: dict = Field({}, title="Cookies")


class RequestHistory(BaseMongoORM):
    method: str = Field("", title="请求方式")
    url: str = Field("", title="地址")
    status_code: int = Field(0, title="状态码")
    request: RequestModel = Field(title='请求数据')
    response: ResponseModel = Field(title='返回结果')

    class Meta(BaseMongoORM.Meta):
        TABLE = "request_history"
        DB = "bili_record"

    def get_id(self) -> str:
        return str(self.response.headers.get('X-Bili-Trace-Id'))

    @classmethod
    def table_headers(cls) -> List[str]:
        return ['id', 'method', 'path', 'status', 'params', 'create_time']

    def table_line(self) -> List[str]:
        return [self.get_id(), self.method, self.request.path,
                self.status_code, self.request.params, self.create_time]
