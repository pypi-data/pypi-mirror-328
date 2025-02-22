#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from typing import Dict
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient
from bili_cli.config.settings import settings


class MongoService:
    mongo_client_dict: Dict[str, MongoClient] = {}

    class Meta:
        HOST: str = settings.MONGO_HOST
        PORT: str = settings.MONGO_PORT

    @classmethod
    def get_instance(cls, mongo_type):
        """获取mongo连接，同一个mongo_type复用已有的连接"""
        if mongo_type not in cls.mongo_client_dict:
            cls.mongo_client_dict[mongo_type] = MongoClient(cls.Meta.HOST, cls.Meta.PORT)
        return cls.mongo_client_dict[mongo_type]


class AsyncMongoService(object):
    mongo_client_dict: Dict[str, AgnosticClient] = {}

    @classmethod
    def get_instance(cls, mongo_type) -> AgnosticClient:
        """获取mongo连接，同一个mongo_type复用已有的连接"""
        if mongo_type not in cls.mongo_client_dict:
            cls.mongo_client_dict[mongo_type] = AsyncIOMotorClient('localhost', 27017)
        return cls.mongo_client_dict[mongo_type]


def get_async_mongo_client(mongo_type: str = 'common') -> AgnosticClient:
    return AsyncMongoService.get_instance(mongo_type)
