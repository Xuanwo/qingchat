#!/usr/bin/env python
# -*- coding: utf-8 -*-

from qingchat import cli
import nose
import os
from unittest import mock
import yaml


def setup():
    os.environ['HOME'] = os.getcwd()  # set test env
    global home
    home = os.getenv('HOME') + '/.config/qingchat'
    os.makedirs('.config/qingchat')
    initconfig = {
        'ip': '127.0.0.1',
        'port': 3000
    }
    with open(home + '/config.yml', 'w+') as f:
        f.write(yaml.dump(initconfig, default_flow_style=False))
        f.close()


def teardown():
    if os.path.isfile(home + '/config.yml'):
        os.remove(home + '/config.yml')
    if os.path.exists(home):
        os.removedirs(home)


def test_init():
    teardown()
    testconfig = {
        'ip': '127.0.0.1',
        'port': 3000
    }
    assert cli.init()==testconfig

def test_save_config():
    pass


def test_load_config():
    pass


def test_config_ip():
    pass


def test_config_port():
    pass


def test_login():
    pass


def test_group_list():
    pass


def test_group_choose():
    pass


def test_group_send_text():
    pass


def test_group_send_media():
    pass


def test_group_send_by_file():
    pass


def test_group_clean():
    pass


def test_main():
    pass
