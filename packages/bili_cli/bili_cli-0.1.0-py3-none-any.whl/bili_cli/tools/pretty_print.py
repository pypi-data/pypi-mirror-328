#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from tabulate import tabulate
from typing import List
from bili_cli.base import PrettyModel


def print_pretty(items: List[PrettyModel], *, maxcolwidths=None):
    if not items:
        return
    fields = items[0].table_headers()
    tables = []
    for item in items:
        line = item.table_line()
        if not line:
            line = []
            for field in fields:
                line.append(getattr(item, field))
        tables.append(line)

    t = tabulate(tables, headers=fields, tablefmt='psql', showindex="always",
                 maxcolwidths=maxcolwidths)
    print(t)
