#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

SEASON_REFRESH_CMD = "bili-cli season refresh --mid {mid}"

ACHIVE_REFRESH_CMD = "bili-cli archive refresh --mid {mid} --total-page {total_page}"
ACHIVE_REFRESH_ONE_CMD = "bili-cli archive refresh-one {title} --mid {mid}"
ARCHIVE_REFRESH_EXT_CMD = "bili-cli archive refresh-ext '{title}' --mid {mid}"
ARCHIVE_TO_SEASON_CMD = "bili-cli archive to-season '{title}' --mid {mid}"
