#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：engine 
@File    ：period_task.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/18 11:24 上午 
'''

from engine import app
from celery.schedules import crontab

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5.0, to_string.s("celery peroid task"), name='to_string') # 每5秒执行add
    sender.add_periodic_task(
        crontab(minute='*/10'),      #每10分钟执行一次
        send_mail.s('hello, this is a celery'), name='send_mail'
    )

@app.task
def send_mail(content):
    print('send mail, content is %s' % content)

@app.task
def to_string(text):
    return 'this is a %s' % text