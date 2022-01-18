#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：engine 
@File    ：calltest.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/18 2:34 下午 
'''
from getconfig import getmysql
import pymysql

print(getmysql()[3])
def save_db():

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
    results = cur.fetchall()
    conn.close()
    print(results)

save_db()