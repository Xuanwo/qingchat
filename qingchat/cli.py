#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Qingchat CLI

Usage:
  qingchat config ip <ip>
  qingchat config port <port>
  qingchat config login
  qingchat group list
  qingchat group choose <group_name>...
  qingchat group clean
  qingchat group send -t <content>
  qingchat group send -i <media>
  qingchat group send -f <file> [<delaytime>]

Options:
  -h --help     Show this screen.
  -v --version     Show version.
"""

from docopt import docopt
import group
import os
import requests
import sys
import webbrowser
import yaml

home = os.path.expanduser('~/.qingchat')
address = ''
config = {}


def init():
    """
    Read config file in ~/qingchat/config.yml
    If not exsit, add the initconfig about ip and port

    :return: the content fo config file in yaml
    """
    initconfig = dict()
    if not os.path.exists(home):  # create dir for config file
        os.makedirs(home)
    if not os.path.isfile(home + '/config.yml'):  # create config file if noy exist
        open(home + '/config.yml', "w+").close()
        initconfig['ip'] = "127.0.0.1"
        initconfig['port'] = 3000
        save_config(initconfig)
    else:
        initconfig = load_config()

    address = 'http://%s:%d/openwx/' % (initconfig['ip'], initconfig['port'])

    return initconfig


def save_config(content, config_file=home + '/config.yml'):
    """
    Save config into config file

    :param content: content of config in yaml
    :param configfile: config file
    """
    with open(config_file, "w") as f:
        f.write(yaml.dump(content, default_flow_style=False))


def load_config(config_file=home + '/config.yml'):
    """
    Load config file from config file in yaml

    :return: yaml of config file
    """
    with open(config_file, "r") as f:
        content = yaml.load(f)
    return content


def config_ip(ip, config_file=home + '/config.yml'):
    """
    Set your server ip as ip

    :param ip: your server's ip
    """
    tmpconfig = load_config(config_file)
    tmpconfig['ip'] = ip
    print("您的服务器端IP地址被设置为： %s" % ip)
    save_config(tmpconfig, config_file)
    return ip


def config_port(port, config_file=home + '/config.yml'):
    """
    Set your server ip as port

    :param port: your server's port
    """
    tmpconfig = load_config(config_file)
    tmpconfig['port'] = port
    print("您的服务器端端口被设置为： %d" % port)
    save_config(tmpconfig, config_file)
    return port


def config_login(config_file=home + '/config.yml'):
    """
    Download qrcode.jpg and show them in webbrowser

    """
    qrcode = "http://%s/qrcode.jpg" % config['ip']  # get qrcode from server
    r = requests.get(qrcode)
    with open("qrcode.jpg", "wb") as f:
        f.write(r.content)
        f.close()

    print("请扫描二维码登录微信")
    if sys.platform.startswith('darwin'):
        os.system("open qrcode.jpg")
    else:
        webbrowser.open("qrcode.jpg")


def main():
    """
    Parse the argument and load config file

    """
    arguments = docopt(__doc__, version='Qingchat 0.3.2')
    config = init()

    if arguments['config']:  # config command
        if arguments['ip']:  # config ip
            config_ip(arguments['<ip>'])
        elif arguments['port']:  # config port
            config_port(arguments['<port>'])
        elif arguments['login']:  # config login
            config_login()
    elif arguments['group']:  # group command
        if arguments['list']:  # group list
            group.group_list()
        elif arguments['choose']:  # group choose
            group.group_choose(arguments['<group_name>'])
        elif arguments['send']:
            if arguments['-t']:  # group send -t
                group.group_send_text(arguments['<content>'])
            elif arguments['-i']:  # group send -i
                group.group_send_media(arguments['<media>'])
            elif arguments['-f']:  # group send -f
                group.group_send_by_file(arguments['<file>'], arguments['<delaytime>'])
        elif arguments['clean']:
            group.group_clean()
    elif arguments['user']:  # user command
        pass


if __name__ == '__main__':
    main()
