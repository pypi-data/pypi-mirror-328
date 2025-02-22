#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from fastapi import APIRouter, Query
from ..mod import ArcAuditModel
from .base import APIResponse
from bili_cli.bili import get_bili
from bili_cli.dtos import BaseResDTO
from bili_cli.config import settings
from bili_cli.cmd.archive import refresh_archive as cmd_refresh_archive


router = APIRouter(
    default_response_class=APIResponse,
)


@router.get("/{bvid}.json")
def get_archive_json(
    bvid: str,
    auth_user_id: int = Query(settings.default_auth_user_id),
    is_remote: int = 0
):
    bili = get_bili(int(auth_user_id))
    if is_remote:
        res = bili.get_archive(bvid)
        return res
    else:
        item = bili.find_by_id(bvid, ArcAuditModel)
        return BaseResDTO(data=item)


@router.get("/refresh")
def refresh_archive(
    auth_user_id: int = Query(settings.default_auth_user_id),
):
    cmd_refresh_archive(mid=auth_user_id, print_data=False, total_page=1)
    return {}
