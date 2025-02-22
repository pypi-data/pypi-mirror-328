#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
import asyncio
import time
import inspect
import sys
from datetime import datetime, timedelta
from typing import Optional, List
from rich import print
from functools import wraps
from typer import Option, Typer, Argument
from typer.models import ParameterInfo
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from bili_cli.tools import logger, get_func_params_default
from bili_cli.config import settings, get_default_auth_user_id, AlbumConfig
from bili_cli.mod import AuthUser
from bili_cli.api import APIError

ARG_ALBUM_ID = Argument(settings.default_album_id, help='专辑')
ARG_MID = Argument(get_default_auth_user_id, help='用户id')

OPT_MID = Option(help='用户ID', default_factory=get_default_auth_user_id)
OPT_MID_NONE = Option(0, help='用户ID')
OPT_ALBUM_ID = Option(settings.default_album_id, help='专辑')
OPT_PAGE = Option(1, help='页码')
OPT_PAGESIZE = Option(10, help='每页条数')


class ExitError(Exception):
    pass


def exit(msg: str):
    raise ExitError(msg)


def get_func(func_name: str):
    for name, func in inspect.getmembers(
            sys.modules[__name__], inspect.isfunction):
        if name == func_name:
            return func
    return None


def command(
    app: Typer = None,
    *,
    name: Optional[str] = None,
    help: Optional[str] = None,
    prompt_fields: List[str] = None,
):
    def command_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 给参数默认值
            default_map = get_func_params_default(func)
            for key, value in default_map.items():
                if key not in kwargs and isinstance(value, ParameterInfo):
                    kwargs[key] = value.default

            # prompt fields
            if prompt_fields:
                for p_field in prompt_fields:
                    if kwargs.get(p_field):
                        continue
                    prompt_func_name = f"prompt_{p_field}"
                    print(prompt_func_name)
                    prompt_func = get_func(prompt_func_name)
                    if prompt_func:
                        kwargs[p_field] = prompt_func()

            start_time = time.time()  # 记录函数开始执行的时间
            logger.debug(f"{func.__name__} {kwargs} begin at {datetime.now()}")
            # 打印用户
            mid = kwargs.get('mid')
            if mid:
                user = AuthUser.find_by_id(mid)
                if user:
                    logger.info(f"当前用户: {user.name_fmt}")
            result = None
            try:
                async def _run():
                    await func(*args, **kwargs)  # 执行函数

                # 判断是否为异步函数
                if inspect.iscoroutinefunction(func):
                    result = asyncio.run(_run())
                else:
                    result = func(*args, **kwargs)
            except ExitError as e:
                p_error(e)
            except APIError as e:
                p_error(e)
            end_time = time.time()  # 记录函数执行结束的时间
            logger.debug(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
            return result
        # 添加 typer
        if app:
            app.command(name, help=help)(wrapper)
        return wrapper
    return command_wrapper


def p_error(text: str):
    print(f"[red]ERROR[/red] {text}")


def prompt_mid(prompt_text: str = "请输入 user_id") -> int:
    users = AuthUser.find()
    msg = f"{prompt_text}> "
    words = []
    display_dict = {}
    display_meta = {}
    for user in users:
        word = f"{user.mid}"
        words.append(word)
        display_dict[word] = user.name
        display_meta[word] = f"{user.mid}"

    logger.debug(words)
    logger.debug(display_dict)
    completer = WordCompleter(words, display_dict=display_dict, meta_dict=display_meta)
    res = prompt(msg, complete_in_thread=True, completer=completer)
    return int(res)


def prompt_album_id(prompt_text: str = "请输入专辑") -> str:
    items = AlbumConfig.find()
    msg = f"{prompt_text}> "
    words = []
    display_dict = {}
    display_meta = {}
    for item in items:
        word = item.id
        words.append(word)
        display_dict[word] = item.title
        display_meta[word] = word

    logger.debug(words)
    logger.debug(display_dict)
    completer = WordCompleter(words, display_dict=display_dict, meta_dict=display_meta)
    return prompt(msg, complete_in_thread=True, completer=completer)


def prompt_date(prompt_text: str = "请选择日期") -> str:
    words = []
    for i in range(7):
        words.append((datetime.now() + timedelta(days=i)).date().isoformat())

    msg = f"{prompt_text}> "
    completer = WordCompleter(words)
    return prompt(msg, complete_in_thread=True, completer=completer)


def prompt_time(prompt_text: str = "请选择时间") -> str:
    words = []
    for i in range(24):
        dt = datetime.now() + timedelta(hours=i+5)
        if dt.hour >= 0 and dt.hour < 9:
            continue
        words.append(dt.time().strftime("%H:00:00"))

    msg = f"{prompt_text}> "
    completer = WordCompleter(words)
    return prompt(msg, complete_in_thread=True, completer=completer)


def prompt_dtime() -> str:
    _date = prompt_date()
    _time = prompt_time()
    if _date and _time:
        return f"{_date} {_time}"
    return None
