#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Qingchat CLI

Usage:
  qingchat config ip <ip>
  qingchat config port <port>
  qingchat group list
  qingchat group choose <group_name>...
  qingchat group send -t <content>
  qingchat group send -i <media>
  qingchat group send -f <file> [<delaytime>]
  qingchat group clean

Options:
  -h --help     Show this screen.
  -v --version     Show version.
"""

import requests
import yaml
import os
from docopt import docopt
import re
import time


def init():
    """

    :return: the content fo config file
    """
    global home
    home = os.getenv('HOME') + '/.config/qingchat'  # need to be tested on Mac OS, and do not support Win
    initconfig = dict()

    if not os.path.exists(home):  # create dir for config file
        os.makedirs(home)
    if not os.path.isfile(home + '/config.yml'):  # create config file if noy exist
        with open(home + '/config.yml', 'w') as f:
            f.write('')
            f.close()
        initconfig['ip'] = "127.0.0.1"
        initconfig['port'] = 3000
        save_config(initconfig)
    else:
        initconfig = load_config()

    return initconfig


def save_config(content):
    """

    :param content: content of config
    :return:
    """
    with open(home + '/config.yml', "w") as f:
        f.write(yaml.dump(content, default_flow_style=False))
        f.close()


def load_config():
    """

    :return: yaml of config file
    """
    with open(home + '/config.yml', "r") as f:
        content = yaml.load(f)
        f.close()
    return content


def config_ip(ip):
    tmpconfig = load_config()
    tmpconfig['ip'] = ip
    print("您的服务器端IP地址被设置为： %s" % ip)
    save_config(tmpconfig)


def config_port(port):
    tmpconfig = load_config()
    tmpconfig['port'] = port
    print("您的服务器端端口被设置为： %d" % port)
    save_config(tmpconfig)


def group_list():
    """

    :return: the json of group info
    """
    url = address + 'get_group_info'  # get wechat group info
    r = requests.get(url)
    print("您的群组为：")
    config['group'] = []
    content = r.json()
    for i in content:
        config['group'].append(i['displayname'])
        print("群名称： " + i['displayname'])
    save_config(config)
    return config['group']


def group_choose(group_name):
    """
    :param group_name: group_name to be chosen, support re
    :return: list of chonsen groups
    """
    if 'chosen_group' not in config or not config['chosen_group']:
        config['chosen_group'] = []
    if not config['chosen_group']:
        config['chosen_group'] = []

    for i in group_name:
        for j in config['group']:
            if re.match(i, j) and j not in config['chosen_group']:
                config['chosen_group'].append(j)

    save_config(config)
    print("您已经选择的群组：")
    for i in config['chosen_group']:
        print("群名称： " + i)

    return config['chosen_group']


def group_send_text(content):
    """

    :param content:
    :return:
    """
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


def group_send_media(media):
    """

    :param media:
    :return:
    """
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


def group_send_by_file(file, delaytime=0):
    """

    :param file: the path to the file you want to use
    :param delaytime: set the delaytime in two message in seconds, defaults to 0s
    :return:
    """
    with open(file, "r") as f:
        content = f.readlines()
        for i in content:
            time.sleep(float(delaytime))
            if i[0] == '!':
                group_send_media(i[1:])
            else:
                group_send_text(i)
    print("文件发送完毕！")


def group_clean():
    """

    :return:
    """
    if 'chosen_group' in config:
        del config['chosen_group']
        save_config(config)
        print("您选中的群组均已被删除。")


def main():
    """

    :return:
    """
    arguments = docopt(__doc__, version='Qingchat 0.1.0')
    global config, address
    config = init()
    address = 'http://%s:%d/openwx/' % (config['ip'], config['port'])

    if arguments['config']:
        if arguments['ip']:
            config_ip(arguments['<ip>'])
        elif arguments['port']:
            config_port(arguments['<port>'])
    elif arguments['group']:  # group command
        if arguments['list']:  # group list
            group_list()
        elif arguments['choose']:  # group choose
            group_choose(arguments['<group_name>'])
        elif arguments['send']:
            if arguments['-t']:  # group send -t
                group_send_text(arguments['<content>'])
            elif arguments['-i']:  # group send -i
                group_send_media(arguments['<media>'])
            elif arguments['-f']:  # group send -f
                group_send_by_file(arguments['<file>'], arguments['<delaytime>'])
    elif arguments['clean']:
        group_clean()
    elif arguments['user']:  # user command
        pass


if __name__ == '__main__':
    main()
