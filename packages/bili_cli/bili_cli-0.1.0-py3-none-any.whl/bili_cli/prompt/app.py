#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import traceback
import os
from typing import List
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from bili_cli.tools import logger
from bili_cli.const import CACHE_DIR
from .models import GroupInfo, CommandInfo, CommandFunctionType


class Prompt:
    def __init__(self, groups: List[GroupInfo] = None):
        self.session = PromptSession(
                history=FileHistory(os.path.join(CACHE_DIR, "shell_history")),
                mouse_support=True,
                complete_in_thread=True
                )
        self.left_prompt = "未登录> "
        self.groups = groups

    def __call__(self):
        while True:
            try:
                text = self.session.prompt(
                    self.left_prompt,
                    default="test",
                    rprompt="right",
                )
            except KeyboardInterrupt:
                continue
            except EOFError:
                break
            except Exception:
                logger.error(traceback.format_exc())
                logger.error(traceback.format_stack())
            #  self._end_run()
        print("GoodBye!!")
    #  def get_command(self) -> CommandFunctionType:

