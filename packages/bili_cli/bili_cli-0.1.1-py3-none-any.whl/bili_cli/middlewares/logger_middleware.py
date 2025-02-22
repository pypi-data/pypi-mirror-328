#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from bili_cli.tools import logger


class LoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 在请求处理之前执行的代码
        request.query_params
        params = request.query_params
        logger.info(f"Query: {params}")

        # 调用下一个中间件或路由处理函数
        response: Response = await call_next(request)
        # 添加自定义头部
        #  response.headers["X-Custom-Header"] = "CustomValue"

        return response
