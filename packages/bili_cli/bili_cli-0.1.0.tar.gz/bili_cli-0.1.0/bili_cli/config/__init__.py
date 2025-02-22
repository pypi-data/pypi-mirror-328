#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com

from bili_cli.config.config import *
from bili_cli.config.season import *
from bili_cli.config.album import *
from bili_cli.config.user import *
from bili_cli.config.user_album import *
from .settings import settings
from .config import (
    set_default_auth_user_id,
    get_default_auth_user_id
)


__all__ = [
    'settings',
    'set_default_auth_user_id',
    'get_default_auth_user_id',
]
