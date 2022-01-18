#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：engine 
@File    ：__init__.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/18 11:24 上午 
'''

from celery import Celery
app = Celery('engine')  # 创建 Celery 实例
app.config_from_object('engine.config')