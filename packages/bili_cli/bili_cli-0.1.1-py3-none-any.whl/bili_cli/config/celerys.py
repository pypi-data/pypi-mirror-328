#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from celery import Celery

celery_config = {
    'broker_url': 'redis://localhost:6379/0',  # 使用Redis作为消息代理
    'result_backend': 'redis://localhost:6379/0',  # 使用Redis作为结果后端
    #  'worker_concurrency': 4,  # 进程数量
    'timezone': 'Asia/Shanghai',  # 设置时区
    #  'enable_utc': True  # 启用UTC
}

def make_celery():
    # 创建一个celery实例
    celery_app = Celery('bili')

# 从环境变量加载配置
    #  celery_app.config_from_envvar('CELERY_')
    celery_app.config_from_object(celery_config)
    celery_app.autodiscover_tasks()
    return celery_app


celery_app: Celery = make_celery()


@celery_app.task
def cal_test():
    print('cal_test')
    return 1



if __name__ == "__main__":
    res = cal_test.delay()
    print(res)
