#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from fastapi import APIRouter
from ..mod import AuthUser
from ..dto import BaseResDTO
from ..base import MongoQuery


router = APIRouter()


@router.get("/user")
def get_users():
    users = AuthUser.find(MongoQuery.build(AuthUser))
    users = [o for o in users]
    return BaseResDTO(data={"data": users, "total": len(users)})
