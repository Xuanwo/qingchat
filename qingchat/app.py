#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from qingchat import friend
from qingchat import user
import json

app = Flask(__name__)
address = 'http://127.0.0.1:3000/'


@app.route('/')
def hello_world():
    r = user.get_user_info()
    return r['name']


@app.route('/user')
def show_user_info():
    r = user.get_user_info()
    return r


if __name__ == '__main__':
    app.run()
