#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import hashlib


def md5_file(filename: str) -> str:
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def md5(text: str) -> str:
    return hashlib.md5(text.encode(encoding='UTF-8')).hexdigest()
