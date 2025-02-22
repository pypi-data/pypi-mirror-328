#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import uuid
import os

from datetime import datetime
from typing import Dict, Any

from pydantic import BaseModel, Field
from sqlalchemy import (create_engine, Column, String, and_,)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .context import get_session
from bili_cli.const import DATA_DIR

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}?check_same_thread=false'.format(
    os.path.join(DATA_DIR, "data.db")
)
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
Base = declarative_base()



class AbsORM():

    """模型基类"""
    __tablename__ = ''
    id = Column(String(32), primary_key=True, default=uuid.uuid4)

    @classmethod
    def session(cls) -> sessionmaker:
        """doc"""
        raise NotImplemented

    def format(self):
        if not self.id:
            self.id = str(uuid.uuid4())

    def save(self):
        """TODO: Docstring for save.
        :returns: TODO

        """
        self.format()
        self.session().add(self)
        self.session().commit()
        return self

    @classmethod
    def find(cls, query: dict = None):
        """TODO: Docstring for find.

        :**kwargs: TODO
        :returns: TODO

        """
        if not query:
            query = {}
        return cls.session().query(cls).filter_by(**query).all()

    @classmethod
    def find_one(cls, query):
        """TODO: Docstring for find.

        :**kwargs: TODO
        :returns: TODO

        """
        return cls.session().query(cls).filter_by(**query).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.find_one({"id": _id})

    @classmethod
    def insert_many(cls, items):
        """批量插入

        :items: TODO
        :returns: TODO

        """
        cls.session().execute(cls.__table__.insert(), items)
        cls.session().commit()

    @classmethod
    def delete(cls, query):
        """删除

        """
        args = []
        for key, value in query.items():
            k = getattr(cls, key) == value
            args.append(k)
        sql = cls.__table__.delete().where(and_(*args))
        cls.session().execute(sql)
        cls.session().commit()

    @classmethod
    def count(cls, query):
        """TODO: Docstring for count.
        :returns: TODO

        """
        return cls.session().query(cls.id).filter_by(**query).count()

    @classmethod
    def update(cls, query, update_data):
        """修改数据

        :query: TODO
        :update_data: TODO
        :returns: TODO

        """
        for item in cls.find(query):
            for k, v in update_data.items():
                setattr(item, k, v)
            item.save()

    def dict(self):
        data = dict(self.__dict__)
        data.pop('_sa_instance_state', None)
        return data


class BaseORM(AbsORM):

    class Meta:
        session: sessionmaker = None
        #  sessionmaker: type = None

    @classmethod
    def session(cls) -> sessionmaker:
        """doc"""
        _session = cls.Meta.session or get_session()
        return _session


def create_sessionmaker(database_uri: str, engine_ext: dict = None) -> type:
    if not engine_ext:
        engine_ext = {}

    engine = create_engine(database_uri, **engine_ext)
    return sessionmaker(bind=engine)


def init_orm(database_uri: str, engine_ext: dict = None) -> None:

    if not engine_ext:
        engine_ext = {}

    engine = create_engine(database_uri, **engine_ext)
    BaseORM.Meta.session = sessionmaker(bind=engine)()


def init_db(database_uri: str, engine_ext: dict = None) -> None:

    if not engine_ext:
        engine_ext = {}

    engine = create_engine(database_uri, **engine_ext)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()
    #  Task( url = 'test').save()
    #  for item in Task.find({ "url": 'test' }):
    #  print(item)
    #  print(item.id)
    #  SubTask.update({ "task_id": "1ba2807b-864f-4813-83ee-09ff0be5d7b6" }, {"status": "success"})

