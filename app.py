#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2021/4/16 下午11:51
# @Author  : herbiel8800@gmail.com
# @Site    : 
# @File    : test.py
# @Software: PyCharm


from pydoc import text
from flask import Flask, request
from amd import detector
from sql import update_data
from speech import speech_det

app = Flask(__name__)


@app.route('/voice', methods=['POST'])
def detect_res():
    base_path = '/var/lib/freeswitch/recordings/detector/'
    uuid = request.values.get("uuid")
    call_status = request.values.get("call_status")
    number = request.values.get("number")
    if 'OK' in call_status:
        file_path = base_path + uuid + '_' + number +'.wav'
        det_res = detector(file_path)
        if det_res is not None :
            ## 3 空号,4语音邮箱,5语音邮箱转接,6号码被拉黑，7无法接通，8未知,9电话未接通
            det_text = speech_det(file_path)
            if "no existe" in det_text:
                det_code = 3
            elif "buzón" in det_text or "no puede ser completada" in det_text or "grabe" in det_text:
                det_code = 4
            elif "transferida" in det_text :
                det_code = 5
            elif "restringida" in det_text:
                det_code = 6
            elif "no está disponible" in det_text:
                det_code = 7
            else:
                det_code = 8
            save_db(uuid, number,det_res,call_status,det_text)
        else:
            # print det_res
            det_code = 8
        update_data(uuid,type="det",cause="",text=det_text,det_code=det_code)
    else:
        det_code = 9
        update_data(uuid,type="det",cause="",text="",det_code=det_code)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)