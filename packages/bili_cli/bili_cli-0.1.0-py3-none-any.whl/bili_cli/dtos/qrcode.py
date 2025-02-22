#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from pydantic import Field
from .base import BaseResDTO


class QRCodeGenerateResDTO(BaseResDTO):
    url: str = Field("", title="二维码内容")
    qrcode_key: str = Field("", title="扫码登录秘钥")


class QRCodePollResDTO(BaseResDTO):
    url: str = Field("", title="游戏分站跨域登录 url")
    refresh_token: str = Field("", title="刷新 refresh_token")
    timestamp: int = Field(0, title="登录时间")
    code: int = Field(0, title="0：扫码登录成功 86038：二维码已失效 86090：二维码已扫码未确认 86101：未扫码")
    message: str = Field("", title="扫码状态信息")
