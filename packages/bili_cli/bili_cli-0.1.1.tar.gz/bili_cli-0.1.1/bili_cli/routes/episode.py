#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from fastapi import APIRouter, Query
from .base import APIResponse, QUERY_UID
from bili_cli.config import settings
from bili_cli import manage as bm
from bili_cli.dtos import GetEpisodesResDTO


router = APIRouter(
    default_response_class=APIResponse,
)


@router.get("", response_model=GetEpisodesResDTO)
def get_episodes(
    manage_name: str = Query(settings.default_album_id, title="专辑"),
    auth_user_id: int = QUERY_UID,
    page: int = 1, pagesize: int = 30,
    season: int = Query(0),
    name: str = "",
    bili_name: str = "",
):
    season = int(season) if season else 0
    result = bm.find_episodes(manage_name, auth_user_id, season=season,
                              page=page, pagesize=pagesize)
    return result


@router.get("/split")
def split_episode(
    episode_id: str,
    manage_name: str = Query(settings.default_album_id, title="专辑"),
    auth_user_id: int = QUERY_UID,
):
    res = bm.split_episode(manage_name, auth_user_id, episode_id)
    return res


@router.get("/part/make")
def make_episode_part(
    episode_id: str = Query(..., title='剧集id'),
    manage_name: str = settings.default_album_id,
    auth_user_id: int = QUERY_UID,
):
    return bm.make_episode_part_video(manage_name, auth_user_id, episode_id, is_async=True)
