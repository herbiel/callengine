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
def getnumlist(limit):

    conn = pymysql.connect(
        host=getmysql()[0],
        port=3306,
        user=getmysql()[2],
        passwd=getmysql()[3],
        db=getmysql()[1]
    )

    sql = 'select uuid,number from record where idle = "True" limit %s'%limit
    cur = conn.cursor()
    cur.execute(sql)
    uuidlist = []
    numberlist = []
    results = cur.fetchall()
    for i in results:
        uuidlist.append(i[0])
        numberlist.append(i[1])
    conn.close()
    return uuidlist,numberlist


def update_data(uuid):

    conn = pymysql.connect(
        host=getmysql()[0],
        port=3306,
        user=getmysql()[2],
        passwd=getmysql()[3],
        db=getmysql()[1]
    )
    res_str = "False"
    sql = sql = 'update record set idle = "%s" where uuid = "%s"'%(res_str,uuid)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()

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
            for i,u in zip(number_pool,uuid_pool):
                result = outbound.apply_async(args=(i,u,))
                value = result.get() # 等待任务执行完毕后，才会返回任务返回值
                update_data(u)
                print(value)
        else:
            print("celery queue is full")
except outbound.OperationalError as exc: # 任务异常处理
    logger.exception('Sending task raised: %r', exc)
