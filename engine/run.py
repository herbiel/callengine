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
import pymysql
from getconfig import getmysql
from engine.Freeswitch import command
logger = get_logger(__name__)

##取出号码
def getnumlist():

    conn = pymysql.connect(
        host=getmysql()[0],
        port=3306,
        user=getmysql()[2],
        passwd=getmysql()[3],
        db=getmysql()[1]
    )

    sql = 'select number from record where finish = "False"'
    cur = conn.cursor()
    cur.execute(sql)
    reslist = []
    results = cur.fetchall()
    for i in results:
        reslist.append(i[0])
    conn.close()
    return reslist



##按一定并发推送到celery
try:
    number_pool = []
    number_pool = getnumlist()
    for i in number_pool:
        fs_cps = int(command('show calls count').split('\n')[1].split(' ')[0])
        if fs_cps <=20 :
            result = outbound.apply_async(args=(i,))
            value = result.get() # 等待任务执行完毕后，才会返回任务返回值
            print(value)
        else:
            result = outbound.apply_async(args=(i,),countdown=60)
            value = result.get() # 等待任务执行完毕后，才会返回任务返回值
            print(value)
except outbound.OperationalError as exc: # 任务异常处理
    logger.exception('Sending task raised: %r', exc)
