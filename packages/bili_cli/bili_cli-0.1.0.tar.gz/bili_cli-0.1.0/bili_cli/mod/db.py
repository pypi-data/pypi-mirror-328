#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:


from bili_cli.base import BaseDB


class CommonDB(BaseDB):

    class Meta(BaseDB.Meta):
        TABLE = "common"


COMMON_DB = CommonDB()
