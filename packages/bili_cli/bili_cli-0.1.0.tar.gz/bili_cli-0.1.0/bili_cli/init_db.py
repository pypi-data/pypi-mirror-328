#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:


from bili_cli.config import init_album, init_user, init_ua
from bili_cli.make import init_vc


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    action = args[0]
    for init_func in (init_album, init_user, init_ua, init_vc):
        func_name = init_func.__name__
        if action in func_name:
            print('初始化', func_name)
            init_func()
