#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from fastapi import APIRouter
from .base import APIResponse
from bili_cli.config import get_albums
from bili_cli.dtos import GetAlbumsResDTO
from .base import response_model


router = APIRouter(
    default_response_class=APIResponse,
)


@router.get("", response_model=response_model(GetAlbumsResDTO))
def _get_albums():
    albums = get_albums()
    return GetAlbumsResDTO(data=albums)
