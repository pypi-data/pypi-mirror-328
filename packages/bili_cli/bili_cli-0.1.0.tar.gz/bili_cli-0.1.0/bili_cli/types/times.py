#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import math
from datetime import timedelta


class Duraction(float):

    def __str__(self) -> str:
        return str(timedelta(seconds=math.floor(float(self))))


if __name__ == "__main__":
    d = Duraction(123.1)
    print(d)
    print(str(d))
    print(isinstance(d, float))
