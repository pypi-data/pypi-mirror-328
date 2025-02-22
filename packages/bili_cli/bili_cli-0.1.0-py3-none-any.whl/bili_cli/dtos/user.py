#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from pydantic import Field
from .base import BaseResDTO
from bili_cli.mod import Wbi, User


class WebInferfaceNavResDTO(BaseResDTO):
    mid: int = Field(0, title="用户mid")
    name: str = Field("", title="用户昵称", alias='uname')
    face: str = Field("", title="头像")
    money: float = Field(0, title="硬币")
    wbi: Wbi = Field(None, title="新版鉴权信息", alias='wbi_img')


class AccInfoResDTO(BaseResDTO, User):
    is_followed: bool = Field(False, title="是否关注此用户", description='true：已关注 false：未关注需要登录（Cookie）未登录恒为false')
