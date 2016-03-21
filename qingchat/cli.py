#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Qingchat CLI

Usage:
  qingchat group list
  qingchat group choose <group_name>...
  qingchat group send -t <content>
  qingchat group send -i <media>
  qingchat group clean

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import requests
import yaml
import os
from docopt import docopt
import json


def init():
    global home
    home = os.getenv('HOME') + '/.config/qingchat'  # need to be tested on Mac OS, and do not support Win

    if not os.path.exists(home):  # create dir for config file
        os.makedirs(home)
    if not os.path.isfile(home + '/config.yml'):  # create config file if noy exist
        os.mknod(home + '/config.yml')
        with open(home + '/config.yml', "w") as f:
            initconfig = dict()
            initconfig['address'] = "127.0.0.1"
            initconfig['port'] = 3000
            f.write(yaml.dump(initconfig, default_flow_style=False))
            f.close()


def group_list():
    url = address + 'get_group_info'  # get wechat group info
    r = requests.get(url)
    print("您的群组为：")
    content = r.json()
    for i in content:
        print("群名称： " + i["displayname"])


def group_choose(group_name):
    if 'chosen_group' not in config:
        config['chosen_group'] = []
    for i in group_name:
        if i not in config['chosen_group']:
            config['chosen_group'].append(i)
    with open(home + '/config.yml', 'w') as f:
        f.write(yaml.dump(config, default_flow_style=False))
        f.close()
    print("您已经选择的群组：")
    for i in config['chosen_group']:
        print("群名称： " + i)


def group_send_text(content):
    data = {
        'displayname': '',
        'content': ''
    }
    url = address + 'send_group_message'
    for i in config['chosen_group']:
        data['displayname'] = i
        data['content'] = content
        r = requests.post(url, data=data)
        print(r.json())


def group_send_image(media):
    data = {
        'displayname': '',
        'media_path': ''
    }
    url = address + 'send_group_message'
    for i in config['chosen_group']:
        data['displayname'] = i
        data['media_path'] = media
        r = requests.post(url, data=data)
        print(r.json())


def group_clean():
    if 'chosen_group' in config:
        del config['chosen_group']
        with open(home + '/config.yml', 'w') as f:
            f.write(yaml.dump(config, default_flow_style=False))
            f.close()
        print("您选中的群组均已被删除。")


def main():
    arguments = docopt(__doc__, version='Qingchat 0.0.1')
    init()
    global config, address
    with open(home + '/config.yml', 'r') as f:  # load config file
        config = yaml.load(f)
        f.close()
    address = 'http://%s:%d/openwx/' % (config['address'], config['port'])

    if arguments['group']:  # group command
        if arguments['list']:
            group_list()
        elif arguments['choose']:
            group_choose(arguments['<group_name>'])
        elif arguments['send'] and arguments['-t']:
            group_send_text(arguments['<content>'])
        elif arguments['send'] and arguments['-i']:
            group_send_image(arguments['<media>'])
        elif arguments['clean']:
            group_clean()
    elif arguments['user']:  # group command
        pass


if __name__ == '__main__':
    main()
