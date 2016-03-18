#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from qingchat.cli import address
import urllib.parse


def get_friend_info():
    url = address + 'openwx/get_friend_info'
    r = requests.get(url)
    # print(requests.get(url).text)
    return r.json()


def send_friend_message(id='', account='', displayname='', markname='', media_path=''):
    data = {
        'id': id,
        'account': account,
        'displayname': displayname,
        'markname': markname,
        'media_path': media_path
    }
    url = address + '/openwx/send_friend_message'
    r = requests.post(url, data=urllib.parse.urlencode(data))  # nice to be tested.
    return r.json()


if __name__ == '__main__':
    get_friend_info()
