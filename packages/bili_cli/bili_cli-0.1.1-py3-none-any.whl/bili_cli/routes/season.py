#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from fastapi import APIRouter
from ..mod import SeasonModel
from .base import APIResponse, response_model


router = APIRouter(
    default_response_class=APIResponse,
)


@router.get("/{sid}.json", response_model=response_model(SeasonModel))
def get_season_json(
    sid: int,
):
    item = SeasonModel.find_by_id(sid)
    if not item:
        return 1, f"合集: {sid} 找不到"
    return item
