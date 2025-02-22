#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from datetime import datetime


def build_timestamp() -> int:
    return int(datetime.now().timestamp())
