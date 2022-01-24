#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 下午11:51
# @Author  : herbiel8800@gmail.com
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import pickle
import librosa
import numpy as np
import sys
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=UserWarning)
    loaded_model = pickle.load(open("models/model.pkl", "rb"))
def detector(wav_file):
    if loaded_model != None:
        X, sample_rate = librosa.load(wav_file, res_type='kaiser_fast')
        mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
        X = [mfccs]
        prediction = loaded_model.predict(X)
        return prediction[0]

    else:
        return 10