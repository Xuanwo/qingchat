#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json
from qingchat.cli import address


def get_user_info():
    url = address + 'openwx/get_user_info'
    r = requests.get(url)
    # print(r.json())
    return r.json()


if __name__ == '__main__':
    get_user_info()
