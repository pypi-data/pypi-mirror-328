#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import os
import sys
from loguru import logger

logger.remove(0)

logger.add(os.path.expanduser('~/Downloads/bili_cli/logs/bili.log'), rotation='500 MB')
stdout_id = logger.add(sys.stdout, level="INFO")


def set_logger_level(level: str):
    global stdout_id
    logger.remove(stdout_id)
    stdout_id = logger.add(sys.stdout, level=level)


if __name__ == "__main__":
    logger.info("info")
    logger.debug("debug")
    set_logger_level("DEBUG")
    logger.info("info")
    logger.debug("debug")
    set_logger_level("INFO")
    logger.info("info")
    logger.debug("debug")
