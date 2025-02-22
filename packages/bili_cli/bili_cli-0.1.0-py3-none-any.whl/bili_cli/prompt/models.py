#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from typing import (
    Any,
    Callable,
    Optional,
    TypeVar,
    Self,
)

CommandFunctionType = TypeVar("CommandFunctionType", bound=Callable[..., Any])


class CommandInfo:
    def __init__(
        self,
        name: Optional[str] = None,
        *,
        callback: Optional[CommandFunctionType] = None,
        help: Optional[str] = None,
    ):
        self.name = name
        self.callback = callback
        self.help = help


class GroupInfo:
    def __init__(
        self,
        name: str,
        *,
        help: Optional[str] = None,
    ):
        self.name = name
        self.help = help
        self.commands = []

    def add_command(self, command: CommandInfo) -> Self:
        self.commands.append(command)
        return self


DEFAULT_GROUP = GroupInfo('default')
