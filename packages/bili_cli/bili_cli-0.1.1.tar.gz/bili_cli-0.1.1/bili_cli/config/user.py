#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import pydantic
from typing import List
from bili_cli import const
from bili_cli.base import BaseMongoORM, AsyncCommonORM


class UserConfig(BaseMongoORM):
    id: str = pydantic.Field(title="id")
    name: str = pydantic.Field("", title="名称")
    cookie: str = pydantic.Field("", title="网络请求cookie")
    bili_jct: str = pydantic.Field("", title="post请求认证")

    class Meta(BaseMongoORM.Meta):
        TABLE = "user"

    @classmethod
    def build(cls, id) -> 'UserConfig':
        item = cls(id=id)
        #  item.cookie = const.COOKIES[id]
        #  item.bili_jct = const.BILI_JCT.get(id)
        #  cookies = item.cookie.split('; ')
        #  for cookie_str in cookies:
            #  ck, cv = cookie_str.split("=")
            #  if ck == 'bili_jct':
                #  item.bili_jct = cv.strip(';')
        return item


_users = [
    UserConfig.build(const.BILI_NAME_IPART),
    UserConfig.build(const.BILI_NAME_IPART2),
    UserConfig.build(const.BILI_NAME_WEN),
    UserConfig.build(const.BILI_NAME_WXNACY),
    UserConfig.build(const.BILI_NAME_XINXIN),
    UserConfig.build(const.BILI_NAME_FEIFEI),
]


def get_user(name) -> UserConfig:
    return UserConfig.find_by_id(name)


async def async_get_user(name) -> UserConfig:
    return await UserConfig.async_find_by_id(name)


def get_users() -> List[UserConfig]:
    return _users


def get_user_ids() -> List[UserConfig]:
    return [o.id for o in get_users()]


def init_user():
    print('init user')
    for user in _users:
        user.save()

