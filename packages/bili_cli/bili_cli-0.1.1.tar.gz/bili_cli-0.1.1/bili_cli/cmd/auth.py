#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from typer import Typer, Option, Argument
from rich import print
from bili_cli.mod import AuthUser
from bili_cli.tools.pretty_print import print_pretty
from bili_cli.bili import get_bilis
from bili_cli.config import set_default_auth_user_id, get_default_auth_user_id
from .base import command

app = Typer()


@command(app, name='list')
def _list():
    users = list(AuthUser.find())
    users.sort(key=lambda o: o.mid)
    default_uid = get_default_auth_user_id()
    for user in users:
        if user.mid == default_uid:
            user.is_default = True

    print("账户列表如下:")
    print_pretty(users)


@command(app, help='刷新 auth')
def refresh(mid: int = Option(None, help='用户id')):
    for bili in get_bilis(mid):
        bili.refresh_auth()
        print(f"刷新 {bili.auth.name} 成功")


@command(app, help='默认使用哪个用户')
def use(mid: int = Argument(..., help='用户id')):
    res = set_default_auth_user_id(mid)
    if res.modified_count:
        user = AuthUser.find_by_id(mid)
        print(f"设置用户[cyan]成功[/cyan]: {user.name}({user.mid})")
    else:
        print(f"设置用户[red]失败[/red]: {mid}")
