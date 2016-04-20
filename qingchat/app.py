#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
import group
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    r = group.list()
    return r['name']


@app.route('/group')
def test():
    pass


@app.route('/friend')
def x():
    pass


@app.route('/listen')
def xx():
    pass


if __name__ == '__main__':
    app.run(debug=True)
