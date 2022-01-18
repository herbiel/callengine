#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：engine 
@File    ：run.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/18 3:50 下午 
'''
from celery.utils.log import get_logger
from engine.tasks import outbound
from celery import group, chain, chord
logger = get_logger(__name__)
try:
    result = outbound.apply_async(args=(50033,))
    value = result.get() # 等待任务执行完毕后，才会返回任务返回值
    print(value)
except outbound.OperationalError as exc: # 任务异常处理
    logger.exception('Sending task raised: %r', exc)
