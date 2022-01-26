#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：engine 
@File    ：run.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/18 3:50 下午 
'''
import pymysql
from getconfig import getmysql


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


def update_data(uuid,type,cause,text,det_code):

    conn = pymysql.connect(
        host=getmysql()[0],
        port=3306,
        user=getmysql()[2],
        passwd=getmysql()[3],
        db=getmysql()[1]
    )
    if type == "idle":                
        res_str = "False"
        sql = 'update record set idle = "%s" where uuid = "%s"'%(res_str,uuid)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
    elif type == "det":
        sql = 'update record set detector_code = "%s",text = "%s" where uuid = "%s"'%(det_code,text,uuid)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
    elif type == "call_process":
        sql = 'update record set cause = "%s" where uuid = "%s"'%(cause,uuid)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
    else:
        return "error"

def getreslist(limit):
    
    conn = pymysql.connect(
        host=getmysql()[0],
        port=3306,
        user=getmysql()[2],
        passwd=getmysql()[3],
        db=getmysql()[1]
    )

    sql = 'select uuid,number,task_id,result from record where idle = "True" limit %s'%limit
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    conn.close()
    return results