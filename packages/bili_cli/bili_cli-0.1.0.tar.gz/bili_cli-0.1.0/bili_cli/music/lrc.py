#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import pylrc
import chardet
from pylrc.classes import LyricLine
from typing import List


def get_path_content(path: str) -> str:
    try:
        with open(path, 'r') as file:
            return file.read()
    except UnicodeDecodeError:
        with open(path, 'r', encoding='GBK') as file:
            return file.read()


def get_lrc_lines(path) -> List[LyricLine]:
    return pylrc.parse(get_path_content(path))


if __name__ == "__main__":
    #  get_lrc_lines('/Volumes/Getea/影片/音乐/周杰伦/JAY/周杰伦 - 斗牛.lrc')
    res = get_path_content('/Volumes/Getea/影片/音乐/优秀单曲/被我弄丢的你/被我弄丢的你.lrc')
    print(res)
    res = get_path_content('/Volumes/Getea/影片/音乐/周杰伦/JAY/周杰伦 - 斗牛.lrc')
    print(res)
