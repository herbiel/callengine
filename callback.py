#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：engine 
@File    ：getconfig.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/18 2:17 下午 
'''

from sql import getreslist
import json

result = getreslist(10)
class create_dict(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value
mydict = create_dict()
for row in result:
    mydict.add(row[2],({"uuid":row[0],"number":row[1],"result":row[3]}))

stud_json = json.dumps(mydict, indent=2, sort_keys=True)

print(stud_json)

