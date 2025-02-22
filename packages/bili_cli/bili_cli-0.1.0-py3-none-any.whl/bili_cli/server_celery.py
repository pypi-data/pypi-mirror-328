#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:


from bili_cli.config.celerys import celery_app
from bili_cli import sche, server, manage



if __name__ == "__main__":
    res = sche.heart.delay()
    print(res)
