#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import typing
from typing import Type, Union, Optional, Tuple
from fastapi import Query

from fastapi.responses import JSONResponse
from bili_cli.config import settings, get_default_auth_user_id
from bili_cli.base import BaseModel

QUERY_UID = Query(title='用户id', default_factory=get_default_auth_user_id)


def response_model(_type: Type[BaseModel]):
    return Union[Tuple[int, str], Optional[_type]]


class APIResponse(JSONResponse):

    def render(self, content: typing.Any) -> bytes:
        """
        支持两种返回方式: 直接返回 data 内的结果或者返回 code 和 msg
        一般情况下 data 和 code 不用同时自定义
        """
        msg = ""
        _data = None
        if not isinstance(content, (list, tuple)) or len(content) < 2:
            # ep: return data
            code = 0
            _data = content
        else:
            # ep: return code, msg
            code = content[0]
            msg = content[1]

        if not isinstance(code, int):
            code = 0
            _data = None

        _content = {
            "code": code,
            "msg": msg,
            "data": _data,
        }
        return super().render(_content)
