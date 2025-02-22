#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import os
import json


def write_dict(filepath, data):
    """保存成 dict 格式文件"""
    filepath = os.path.expanduser(filepath)
    with open(filepath, 'w') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))
