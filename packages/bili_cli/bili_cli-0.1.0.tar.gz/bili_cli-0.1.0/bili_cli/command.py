#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from datetime import datetime

from bili_cli.cmd.app import app
from bili_cli.prompt.app import Prompt


def main():
    import sys
    args = sys.argv[1:]
    if not args:
        Prompt().run()
    else:
        app()


if __name__ == "__main__":
    begin = datetime.now()
    main()
    end = datetime.now()
    et = (end - begin).total_seconds()
    print(f"time used: {et}")
