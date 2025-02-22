#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com
import inspect
import sys
from typing import Type
from bili_cli.base import BaseMongoORM

from .base import *
from .db import *
from .make import *
from .audio import *
from .typ import *
from .part import *
from .user import *
from .api import *
from .season import *
from .archive import *
from .reply import *
from .config import *
from .biliup import *
from ..models import *


def init_orm(cls: Type[BaseMongoORM]):
    for field, value in cls.model_fields.items():
        setattr(cls.F, field, value)


def init():
    clzs = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for name, clz in clzs:
        if issubclass(clz, BaseMongoORM):
            init_orm(clz)


#  init()
