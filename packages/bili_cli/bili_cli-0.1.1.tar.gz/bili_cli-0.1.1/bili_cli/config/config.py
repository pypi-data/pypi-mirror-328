#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:


from bili_cli.mod.config import ConfigModel
from .settings import settings


def set_default_auth_user_id(auth_user_id: int):
    return ConfigModel(key='default_uid', data=auth_user_id).save()


def get_default_auth_user_id() -> int:
    item = ConfigModel.find_by_id('default_uid')
    if item:
        return int(item.data)
    return settings.default_auth_user_id
