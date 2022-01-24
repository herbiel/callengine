#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：engine 
@File    ：getconfig.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/18 2:17 下午 
'''
import configparser
cf = configparser.ConfigParser()
cf.read('dbconfig.ini')

def getmysql():
    host = cf.get("Mysql-Database","host")
    db_name = cf.get("Mysql-Database","db")
    user = cf.get("Mysql-Database","user")
    password = cf.get("Mysql-Database","password")
    return host,db_name,user,password