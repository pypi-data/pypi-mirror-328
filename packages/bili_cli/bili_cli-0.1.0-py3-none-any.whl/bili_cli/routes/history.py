#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from fastapi import APIRouter
from ..mod import RequestHistory
from ..base import MongoQuery
from .base import APIResponse
from ..dtos.history import RequestHistoryListResDTO


router = APIRouter(
    default_response_class=APIResponse,
)


@router.get("/request", response_model=RequestHistoryListResDTO)
def get_requests():
    query = (
        MongoQuery.build(RequestHistory).page(1).pagesize(10)
        .sort('create_time', typ='desc')
    )
    query_res = RequestHistory.find_page_items(query=query)
    res = RequestHistoryListResDTO()
    res.data = query_res.data
    res.total = query_res.total
    return res


@router.get("/request/{hid}", response_model=RequestHistory)
def get_request(hid: str):
    h = RequestHistory.find_by_id(hid)
    return h
