#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorCollection
from typing import Type
from bili_cli.model.base import BaseORM
from .mongo import get_async_mongo_client
from bili_cli.model import (
    Archive,
)


class BaseCrud:
    model: Type[BaseORM]

    def __init__(self, model: Type[BaseORM]):
        self.model = model
        self.client = get_async_mongo_client()

    def get_db(self) -> AsyncIOMotorCollection:
        return self.client[self.model.Meta.DB][self.model.Meta.TABLE]

    async def save(self, model: BaseORM):
        model.update_time = datetime.now()
        data = model.get_save_data()
        id = model.get_id()
        return self.get_db().update_one({"_id": id}, {"$set": data}, upsert=True)


archive = BaseCrud(Archive)
