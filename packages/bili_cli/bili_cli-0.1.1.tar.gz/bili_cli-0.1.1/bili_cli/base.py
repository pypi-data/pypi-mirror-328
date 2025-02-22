#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import os
import time
import json
from rich.console import Console
from datetime import datetime
from pydantic import Field, SkipValidation, BaseModel as PYBModel, ConfigDict
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.results import UpdateResult as MGUpdateResult
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from motor.core import AgnosticClient
from enum import Enum
from typing import Type, List, Self, Union, Dict, Optional, Any
from bili_cli.const import TABLE_DIR
from bili_cli.tools.loggers import logger
from wpy.path import read_dict, walkfile

console = Console()


class MongoService(object):
    mongo_client_dict = {}

    class Meta:
        HOST: str = os.getenv('BILI_MONGO_HOST') or 'localhost'
        PORT: str = int(os.getenv('BILI_MONGO_PORT') or 27017)

    @classmethod
    def get_instance(cls, mongo_type):
        """获取mongo连接，同一个mongo_type复用已有的连接"""
        if mongo_type not in cls.mongo_client_dict:
            cls.mongo_client_dict[mongo_type] = MongoClient(cls.Meta.HOST, cls.Meta.PORT)
        return cls.mongo_client_dict[mongo_type]


class AsyncMongoService(object):
    mongo_client_dict: Dict[str, AgnosticClient] = {}

    class Meta:
        HOST: str = os.getenv('BILI_MONGO_HOST') or 'localhost'
        PORT: str = int(os.getenv('BILI_MONGO_PORT') or 27017)

    @classmethod
    def get_instance(cls, mongo_type) -> AgnosticClient:
        """获取mongo连接，同一个mongo_type复用已有的连接"""
        if mongo_type not in cls.mongo_client_dict:
            cls.mongo_client_dict[mongo_type] = AsyncIOMotorClient(cls.Meta.HOST, cls.Meta.PORT)
        return cls.mongo_client_dict[mongo_type]


class BaseModel(PYBModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,  # 允许设置自定义类型
        from_attributes=True,  # 允许使用 from_orm
    )

    @property
    def model_dump_exclude(self) -> Optional[List[str]]:
        return None

    @property
    def model_dump_include(self) -> Optional[List[str]]:
        return None

    def dict(self) -> dict:
        exclude = ['model_dump_exclude']
        if isinstance(self.model_dump_exclude, list):
            exclude.extend(self.model_dump_exclude)
        include = None
        if isinstance(self.model_dump_include, list):
            include = self.model_dump_include
        return self.model_dump(
            by_alias=True,
            exclude=exclude,
            include=include,
        )

    def json(self) -> str:
        return self.model_dump_json(by_alias=True)

    def pprint(self):
        console.print_json(self.json())


class PrettyModel(BaseModel):

    @classmethod
    def table_headers(cls) -> List[str]:
        return []

    def table_line(self) -> List[str]:
        return []


class BaseORM(PrettyModel):
    id: str = Field("", title="视频id")
    is_delete: int = Field(0, title="是否删除")
    db_path: str = Field("", title="数据地址", exclude=True)
    create_time: Optional[datetime] = Field(default_factory=datetime.now, title="创建时间")
    update_time: Optional[datetime] = Field(default_factory=datetime.now, title="创建时间")

    class Meta():
        TABLE = ""
        DB = ""

    def get_id(self) -> str:
        return str(self.id)

    def get_save_data(self) -> dict:
        return self.dict()

    @classmethod
    def get_db(cls) -> 'BaseDB':
        return DB_MAP[cls.Meta.DB]

    @classmethod
    def create_id(cls) -> str:
        return str(int(time.time() * 1000))

    @classmethod
    def find(cls, query: 'Query') -> 'QueryResult':
        db = cls.get_db()
        return db.find(query)

    @classmethod
    def find_by_id(cls, id) -> 'BaseORM':
        db = cls.get_db()
        return db.find_by_id(id, cls)

    def save(self):
        db = self.get_db()
        return db.save(self)

    def dump_file(self, path):
        db = self.get_db()
        return db.dump_file(self, path)

    def enable_delete(self) -> Self:
        """使用防刷屏"""
        self.is_delete = 1
        return self


class QueryResult(BaseModel):
    data: List[BaseORM] = Field([])
    total: int = Field(0)


class UpdateResult(BaseModel):
    count: int = Field(0)


class ConditionType(Enum):
    IN = 'in'
    EQ = 'eq'
    LIKE = 'like'


class Condition(BaseModel):
    field: str = Field()
    value: SkipValidation[Any] = Field()
    type: ConditionType = Field()

    def hit(self, ins: BaseORM) -> bool:
        ins_value = getattr(ins, self.field)
        if self.type == ConditionType.LIKE:
            return self.value in ins_value
        elif self.type == ConditionType.EQ:
            return str(self.value) == str(ins_value)
        elif self.type == ConditionType.IN:
            res = False
            if isinstance(self.value, list):
                res = ins_value in self.value
            if not res and isinstance(ins_value, list):
                return self.value in ins_value
            return res


class Query(BaseModel):
    clz: Type[BaseORM] = Field(None)
    properties: Dict[str, 'Proper'] = Field({})
    clz_title: str = Field("")
    conditions: List[Condition] = Field([])
    page_num: int = Field(1)
    start: int = Field(0)
    limit: int = Field(100000000)
    #  pagesize: int = Field(10000000)
    sorts: List['Sort'] = Field([])

    class Proper(BaseModel):
        title: str = Field("")
        type: str = Field("")
        default: SkipValidation[Any] = Field(None)

    class Sort(BaseModel):
        field: str
        type: str = Field('asc')

        def is_asc(self) -> bool:
            return self.type == 'asc'

    @classmethod
    def default(cls) -> Self:
        item = cls()
        return item.eq('is_delete', 0)

    @classmethod
    def build(cls, clz: Type[BaseORM]) -> Self:
        item = cls.default()
        item.clz = clz
        #  schema = clz.schema()
        #  item.clz_title = schema.get("title")
        #  properties = schema.get("properties") or {}
        #  pros = {}
        #  for key, p in properties.items():
        #  pros[key] = cls.Proper(**p)
        #  item.properties = pros
        return item

    def page(self, page: int) -> Self:
        self.start = (page - 1) * self.limit
        self.page_num = page
        return self

    def pagesize(self, limit: int) -> Self:
        self.limit = limit
        self.start = (self.page_num - 1) * self.limit
        return self

    def like(self, field: str, value: str) -> Self:
        c = Condition(field=field, type=ConditionType.LIKE, value=value)
        self.conditions.append(c)
        return self

    def eq(self, field: str, value: str) -> Self:
        c = Condition(field=field, type=ConditionType.EQ, value=value)
        self.conditions.append(c)
        return self

    def in_(self, field: str, value: list | str | int | bool
            ) -> Self:
        c = Condition(field=field, type=ConditionType.IN, value=value)
        self.conditions.append(c)
        return self

    def sort(self, field: str, type: str) -> Self:
        s = self.Sort(field=field, type=type)
        self.sorts.append(s)
        return self

    def hit(self, data: BaseORM) -> bool:
        for cond in self.conditions:
            if not cond.hit(data):
                return False
        return True


class MongoQuery(Query):

    conditions: dict = Field({})
    projection: Optional[dict] = Field(None, title='查询字段 ')

    def eq(self, field: str, value: str) -> Self:
        self.conditions[field] = value
        return self

    def in_(self, field: str, value: list | str | int | bool
            ) -> Self:
        self.conditions[field] = {"$in": value}
        return self

    def like(self, field: str, value: str) -> Self:
        self.conditions[field] = {"$regex": value}
        return self

    def lte(self, field: str, value: str) -> Self:
        self.conditions[field] = {"$lte": value}
        return self

    def gte(self, field: str, value: str) -> Self:
        self.conditions[field] = {"$gte": value}
        return self

    def include(self, *fields) -> Self:
        self.projection = {}
        for field in fields:
            self.projection[field] = 1
        return self

    def sort(self, field: str, typ: Union[int, str] = None) -> Self:
        if not typ:
            typ = field[0]
            field = field[1:]
            if typ == '+':
                typ = 'asc'
            else:
                typ = 'desc'
        s = self.Sort(field=field, type=typ)
        self.sorts.append(s)
        return self

    def to_query_ext(self) -> dict:
        data = {}
        data['skip'] = self.start
        data['limit'] = self.limit
        sorts = []
        for s in self.sorts:
            t = -1
            if s.is_asc():
                t = 1
            sorts.append((s.field, t))
        data['sort'] = sorts
        if self.projection:
            data['projection'] = self.projection
        return data


class BaseMongoORM(BaseORM):

    class F:
        pass

    class Meta():
        TABLE = ""
        DB = "bili_common"

    @classmethod
    def get_db(cls) -> Collection:
        return MongoService.get_instance('common')[cls.Meta.DB][cls.Meta.TABLE]

    def get_save_data(self) -> dict:
        data = self.dict()
        data.pop('db_path', None)
        return data

    def save(self, db: Collection = None) -> MGUpdateResult:
        if not db:
            db = self.get_db()
        self.update_time = datetime.now()
        data = self.get_save_data()
        id = self.get_id()
        return db.update_one({"_id": id}, {"$set": data}, upsert=True)

    @classmethod
    def find_by_id(cls, id, db: Collection = None) -> Self:
        if not db:
            db = cls.get_db()
        id = str(id)
        doc = db.find_one({"_id": id})
        if doc:
            return cls(**doc)
        return None

    @classmethod
    def find(cls, query: Union[Dict, MongoQuery] = None, db: Collection = None,
             **kwargs):
        if not db:
            db = cls.get_db()
        if isinstance(query, MongoQuery):
            query: MongoQuery
            kwargs.update(query.to_query_ext())
            query = query.conditions
        logger.debug(f"find query: {query} kw: {kwargs}")
        docs = db.find(query, **kwargs)
        for doc in docs:
            yield cls(**doc)

    @classmethod
    def find_page_items(
            cls, query: Union[Dict, MongoQuery] = None,
            db: Collection = None, page=1, pagesize=10, **kwargs):
        if not db:
            db = cls.get_db()
        if isinstance(query, MongoQuery):
            query: MongoQuery
            kwargs.update(query.to_query_ext())
            query = query.conditions
        else:
            skip = (page-1) * pagesize
            limit = pagesize
            kwargs['skip'] = skip
            kwargs['limit'] = limit
        logger.debug(f"find_page_items query: {query}")
        logger.debug(f"find_page_items kwargs: {kwargs}")
        docs = db.find(query, **kwargs)
        items = [cls(**doc) for doc in docs]
        total = db.count_documents(query)
        return QueryResult(data=items, total=total)

    def dump_file(self, path):
        with open(path, 'w') as f:
            f.write(json.dumps(json.loads(self.json()), indent=4, ensure_ascii=False))
        return UpdateResult(count=1)


class BaseDB(BaseModel):

    class Meta():
        NAME = ""
        DB = ""

    @classmethod
    def get_db(cls, table) -> Collection:
        return MongoService.get_instance(cls.Meta.DB)[cls.Meta.DB][table]

    @classmethod
    def create_table(cls, clz: Type[BaseORM]):
        try:
            os.makedirs(cls.generate_table_path(clz))
        except Exception:
            pass

    @classmethod
    def generate_table_path(cls, clz: Type[BaseORM] | BaseORM):
        path = os.path.join(TABLE_DIR, cls.Meta.NAME, clz.Meta.TABLE)
        if isinstance(clz, BaseORM):
            return os.path.join(path, clz.get_id() + ".json")
        return path

    @classmethod
    def save(cls, clzs: BaseORM) -> UpdateResult:
        if not clzs.Meta.TABLE:
            raise ValueError("TABLE is None")
        #  cls.create_table(clzs.__class__)

        data = clzs.get_save_data()
        data.pop('db_path', None)
        id = clzs.get_id()
        return cls.get_db(clzs.Meta.TABLE).update_one(
            {"_id": id}, {"$set": data}, upsert=True)

        #  return cls.dump_file(clzs, cls.generate_table_path(clzs))

    @classmethod
    def dump_file(cls, clzs: BaseORM, path: str) -> UpdateResult:
        with open(path, 'w') as f:
            f.write(clzs.model_dump_json(by_alias=True))
        return UpdateResult(count=1)

    @classmethod
    def find_by_id(cls, id: str | int, clz: Type[BaseORM]) -> BaseORM:
        id = str(id)
        path = cls.generate_table_path(clz)
        path = os.path.join(path, id + ".json")
        if not os.path.exists(path):
            return None
        data = read_dict(path)
        data['db_path'] = path
        return clz(**data)

    @classmethod
    def find_one(cls, query: Query) -> BaseORM:
        result = cls.find(query)
        if result.total > 0:
            return result.data[0]
        return None

    @classmethod
    def find(cls, query: Query) -> QueryResult:
        dir = cls.generate_table_path(query.clz)
        #  count = 0
        items = []
        for path in walkfile(dir):
            if not path.endswith(".json"):
                continue
            data = read_dict(path)
            data['db_path'] = path
            item = query.clz(**data)
            if not query.hit(item):
                continue
            #  yield item
            items.append(item)
            #  count += 1
        if query.sorts:
            sort = query.sorts[0]
            is_reverse = not sort.is_asc()
            items.sort(key=lambda o: getattr(
                o, sort.field), reverse=is_reverse)
        end = query.start + query.limit
        return QueryResult(
            data=items[query.start:end], total=len(items))

    @classmethod
    def delete_by_id(cls, id: str | int, clz: Type[BaseORM]) -> UpdateResult:
        item = cls.find_by_id(id, clz)
        if item:
            item.is_delete = 1
            return cls.save(item)
        return UpdateResult()


class BaseMongoDB(BaseDB):

    @classmethod
    def find_by_id(cls, id: str | int, clz: Type[BaseORM]
                   ) -> BaseORM:
        id = str(id)
        doc = cls.get_db(clz.Meta.TABLE).find_one({"_id": id})
        if doc:
            return clz(**doc)
        return None

    @classmethod
    def find_items(cls, query: MongoQuery):
        clz = query.clz

        db = cls.get_db(clz.Meta.TABLE)
        q = query.conditions
        kw = query.to_query_ext()
        logger.info(f"db: {cls.Meta.DB} table: {clz.Meta.TABLE} query: {q} params: {kw}")
        docs = db.find(q, **kw)
        for doc in docs:
            yield clz(**doc)

    @classmethod
    def find_page_items(cls, query: MongoQuery):
        clz = query.clz
        db = cls.get_db(clz.Meta.TABLE)
        kwargs = query.to_query_ext()
        q = query.conditions
        logger.debug(f"db: {cls.Meta.DB} table: {clz.Meta.TABLE} query: {q} params: {kwargs}")
        docs = db.find(q, **kwargs)
        items = [clz(**doc) for doc in docs]
        total = db.count_documents(q)
        return QueryResult(data=items, total=total)

    @classmethod
    def count(cls, clz: Type[BaseORM], query: dict = None):
        db = cls.get_db(clz.Meta.TABLE)
        return db.count_documents(query)


class AsyncCommonORM(BaseORM):

    class Meta():
        TABLE = ""
        DB = "bili_common"

    @classmethod
    def get_db(cls, table) -> AsyncIOMotorCollection:
        return AsyncMongoService.get_instance(cls.Meta.DB)[cls.Meta.DB][table]

    async def save(self) -> MGUpdateResult:
        db = self.get_db(self.Meta.TABLE)
        self.update_time = datetime.now()
        data = self.get_save_data()
        id = self.get_id()
        return await db.update_one({"_id": id}, {"$set": data}, upsert=True)

    @classmethod
    async def find_by_id(
            cls, id: str | int) -> BaseORM:
        id = str(id)
        doc = await cls.get_db(cls.Meta.TABLE).find_one({"_id": id})
        if doc:
            return cls(**doc)
        return None

    @classmethod
    async def find_page_items(cls, query: MongoQuery) -> QueryResult:
        clz = query.clz
        db = cls.get_db(clz.Meta.TABLE)
        kwargs = query.to_query_ext()
        q = query.conditions
        docs = db.find(q, **kwargs)
        items = [clz(**doc) async for doc in docs]
        total = await db.count_documents(q)
        return QueryResult(data=items, total=total)


class CommonDB(BaseDB):

    class Meta():
        NAME = 'common'


DB_MAP = {
    'common': CommonDB()
}


class UserORM(BaseMongoORM):
    name: str = Field("", alias='Name')

    class Meta(BaseORM.Meta):
        TABLE = 'user'
        DB = 'test'

    #  def get_id(self):
        #  return "1"


class WenDB(BaseDB):
    class Meta(BaseDB.Meta):
        NAME = 'wen'


if __name__ == "__main__":
    q = MongoQuery.default().in_('name', ['ww']).like('id', 'ss').sort('ctime', 'asc').sort('order', 'desc')
    #  print(q.conditions)
    print(q.to_query_ext())
    #  print(UserORM.__annotations__)
    #  print(UserORM.schema())
    #  print(UserORM.model_json_schema())
    #  print(WenDB.generate_table_path(UserORM))
    #  print(WenDB.generate_table_path(UserORM()))
    #  WenDB.save(UserORM(id="wwww"))
    #  item = WenDB.find_one(UserORM(id="wwww"))
    #  print(item)
    #  print(UserORM.__annotations__)
    #  print(UserORM.schema(), type(UserORM.schema()))
    #  UserORM(id="1", name="wxnacy").save()
    #  q = Query.build(UserORM).like('name', 'ss')
    #  print(q.hit(UserORM(name='ssss')))
    #  print(q.hit(UserORM(name='1234')))
