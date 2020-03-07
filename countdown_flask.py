#!/usr/bin/python3

'''
More info: https://palletsprojects.com/p/flask/
https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
'''

from flask import Flask, escape, request
import datetime

app = Flask(__name__)

@app.route('/')
def countdown():
    CurrentDate = datetime.datetime.now()
    Leave = "30/01/2020 15:00"
    Leave = datetime.datetime.strptime(Leave, "%d/%m/%Y %H:%M")
    countdown = Leave - CurrentDate
    return ("Hello Guilherme! \nYour leave will be in {} days!".format(countdown.days))
