#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import os
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # 使用 env 字段来指定环境变量名称
    default_auth_user_id: int = Field(..., title='默认用户id', env="BILI_DEFAULT_AUTH_USER_ID")
    default_album_id: str = Field(..., title='默认专辑', env="BILI_DEFAULT_ALBUM_ID")

    DEFAULT_AUTH_USER_ID: int = Field(..., title='默认用户id')
    DEFAULT_ALBUM_ID: str = Field(..., title='默认专辑')
    QY_KEY: str = Field("", title='企业微信 api key')
    VIDEO_SHOT_DIR: str = Field(os.path.expanduser("~/Prictures/QQPlayer"), title="截图目录")
    SERVER_HOST: str = Field("0.0.0.0", title="服务地址")
    SERVER_PORT: int = Field(8006, title="服务端口")

    CONFIG_ROOT: str = os.path.expanduser("~/Downloads/bili_cli")   # 配置根目录
    CONFIG_DIR: str = os.path.join(CONFIG_ROOT, "config")   # 配置文件目录

    # mongo
    MONGO_HOST: str = Field("localhost", title="mongo 地址")
    MONGO_PORT: int = Field(27017, title="mongo 端口")

    # 可以使用 env_prefix 来指定环境变量的前缀
    class Config:
        #  env_prefix = "BILI_"
        env_prefix = "BILI_"
        #  env_file = os.path.join(os.getenv("PYTHONPATH"), ".env")

    @property
    def full_host(self):
        host = self.SERVER_HOST
        if host == '0.0.0.0':
            host = 'localhost'
        return f"http://{host}:{self.SERVER_PORT}"


# 创建 Settings 实例
settings = Settings()
