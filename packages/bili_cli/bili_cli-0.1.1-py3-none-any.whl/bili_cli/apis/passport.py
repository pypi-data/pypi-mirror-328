#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from .. import dtos
from .base import BaseApi


class PassportApi(BaseApi):

    class Config(BaseApi.Config):
        HOST = "https://passport.bilibili.com"

    @classmethod
    def build(cls):
        return cls(auth=None)

    def qrcode_generate(self) -> dtos.QRCodeGenerateResDTO:
        return self.get("/x/passport-login/web/qrcode/generate", res_clz=dtos.QRCodeGenerateResDTO)

    def qrcode_poll(self, qrcode_key: str) -> dtos.QRCodePollResDTO:
        params = {"qrcode_key": qrcode_key}
        return self.get("/x/passport-login/web/qrcode/poll", params=params, res_clz=dtos.QRCodePollResDTO)


DEFAULT_PASSPORT_API = PassportApi.build()
