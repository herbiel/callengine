#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：engine 
@File    ：config.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/18 11:23 上午 
'''
BROKER_URL = 'redis://:123456@127.0.0.1:6379/0' # Broker配置，使用Redis作为消息中间件
CELERY_RESULT_BACKEND = 'redis://:123456@127.0.0.1:6379/1' # BACKEND配置，这里使用redis
CELERY_RESULT_SERIALIZER = 'json' # 结果序列化方案
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 # 任务过期时间
CELERY_TIMEZONE='Asia/Shanghai'   # 时区配置
CELERY_IMPORTS = (     # 指定导入的任务模块,可以指定多个
    'engine.tasks',
    'engine.period_task'
)
