#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import speech_recognition as sr
import sys



def speech_det(audiofile):
    harvard = sr.AudioFile(audiofile)
    r = sr.Recognizer()
    with harvard as source:
        audio = r.record(source, duration=10)
    try:
        res_text = r.recognize_google(audio)
    except sr.UnknownValueError:
        res_text = "UnknownValueError"
    except sr.RequestError as e:
        res_text = "sr.RequestError"
    return res_text