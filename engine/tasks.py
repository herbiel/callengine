#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：engine 
@File    ：tasks.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/18 11:24 上午 
'''
from subprocess import call
import celery
import time
from celery.utils.log import get_task_logger
from engine import app
from engine.Freeswitch import command



@app.task
def outbound(number):
    call_cmd = 'originate sofia/internal/sip:%s@192.168.50.16:5080 sleep:5000,hangup inline'%number
    res = command(call_cmd)
    return res

