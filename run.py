#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：engine 
@File    ：run.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/18 3:50 下午 
'''
from unittest import result
from celery.utils.log import get_logger
from engine.tasks import outbound
from celery import group, chain, chord
from engine.Freeswitch import command
from sql import getnumlist,update_data
logger = get_logger(__name__)


##按一定并发推送到celery
try:
    while True:
        number_pool = []
        uuid_pool = []
        fs_cps = int(command('show calls count').split('\n')[1].split(' ')[0])
        if fs_cps <= 20 :
            max_call = 20 - fs_cps
            print ("max call is %s"%max_call)
            uuid_pool,number_pool = getnumlist(max_call)
            for number,uuid in zip(number_pool,uuid_pool):
                result = outbound.apply_async(args=(number,uuid,))
                value = result.get().split(" ")[0] # 等待任务执行完毕后，才会返回任务返回值
                update_data(uuid=u,type="call_process",cause=value,text="",det_code="")
                print (value)
        else:
            print("celery queue is full")
except outbound.OperationalError as exc: # 任务异常处理
    logger.exception('Sending task raised: %r', exc)
