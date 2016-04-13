#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from qingchat import group
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    r = group.group_list()
    return r['name']


@app.route('group')
def test():
    pass


if __name__ == '__main__':
    app.run(debug=True)
