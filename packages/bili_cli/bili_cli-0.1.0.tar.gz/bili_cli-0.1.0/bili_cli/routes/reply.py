#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from typing import Optional
from fastapi import APIRouter, Query
from .base import APIResponse
from bili_cli.bili import get_bili
from bili_cli.config import settings
from bili_cli.dtos import GetReplysResDTO


router = APIRouter(
    default_response_class=APIResponse,
)


@router.get("", response_model=GetReplysResDTO)
def get_replys(
    auth_user_id: int = Query(settings.default_auth_user_id, title='用户id'),
    up_like: Optional[int] = Query(None, title='用户id'),
    page: int = 1, pagesize: int = 10,
    keyword: str = ""
):
    bili = get_bili(auth_user_id)
    return bili.find_replys(message_like=keyword, is_up_like=up_like, page=page, pagesize=pagesize)
