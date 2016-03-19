#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Qingchat CLI

Usage:
  qingchat group list
  qingchat group choose <group_id>...
  qingchat group send -t <content>
  qingchat group send -i <image>

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import requests
import sys
import yaml
import os
from docopt import docopt
import json
import shutil


def init():
    global home
    home = os.getenv('HOME') + '/.config/qingchat'  # need to be tested on Mac OS, and do not support Win

    if not os.path.exists(home):  # create dir for config file
        os.makedirs(home)
    if not os.path.isfile(home + '/config.yml'):  # create config file from templates
        shutil.copyfile('config.yml', home + '/config.yml')


def group_list():
    url = address + 'get_group_info'  # get wechat group info
    r = requests.get(url)
    print("您的群组为：")
    content = r.json()
    for i in content:
        print("群名称： " + i["displayname"])
        print("群ID： " + i["id"])


def group_choose(group_id):
    if 'chosen_group' not in config:
        config['chosen_group'] = []
    for i in group_id:
        if i not in config['chosen_group']:
            config['chosen_group'].append(i)
    with open(home + '/config.yml', 'w') as f:
        f.write(yaml.dump(config, default_flow_style=False))
        f.close()
    print("您已经选择的群组：")
    for i in config['chosen_group']:
        print("群ID： " + i)


def group_send_text(content):
    data = {
        'id': '',
        # 'displayname': '',
        # 'media_path': '',
        'content': ''
    }
    url = address + 'send_group_message'
    for i in config['chosen_group']:
        data['id'] = i
        data['content'] = content
        r = requests.post(url, data=data)
        print(r.json())


def main():
    arguments = docopt(__doc__, version='Qingchat 0.0.1')
    init()
    global config, address
    with open(home + '/config.yml', 'r') as f:  # load config file
        config = yaml.load(f)
        f.close()
    address = 'http://%s:%d/openwx/' % (config['address'], config['port'])
    if arguments['group'] and arguments['list']:
        group_list()
    elif arguments['group'] and arguments['choose']:
        # print(arguments['<group_id>'])
        group_choose(arguments['<group_id>'])
    elif arguments['group'] and arguments['send'] and arguments['-t']:
        group_send_text(arguments['<content>'])


if __name__ == '__main__':
    main()
