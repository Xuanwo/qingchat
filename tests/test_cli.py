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
    if not os.path.exists(home):
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


@nose.with_setup(setup, teardown)
def test_init():
    teardown()
    testconfig = {
        'ip': '127.0.0.1',
        'port': 3000
    }
    assert cli.init() == testconfig


@nose.with_setup(setup, teardown)
def test_save_config():
    testconfig = {
        'ip': '0.0.0.0',
        'port': 4000
    }
    cli.save_config(testconfig)
    with open(home + '/config.yml', "r") as f:
        content = yaml.load(f)
        f.close()
    assert testconfig == content


@nose.with_setup(setup, teardown)
def test_load_config():
    testconfig = {
        'ip': '127.0.0.1',
        'port': 3000
    }
    assert cli.load_config() == testconfig


@nose.with_setup(setup, teardown)
def test_config_ip():
    configip = '0.0.0.0'
    assert cli.config_ip(configip) == configip


@nose.with_setup(setup, teardown)
def test_config_port():
    configport = 4000
    assert cli.config_port(configport) == configport


@nose.with_setup(setup, teardown)
def test_login():
    pass


@nose.with_setup(setup, teardown)
def test_group_list():
    pass


@nose.with_setup(setup, teardown)
def test_group_choose():
    pass


@nose.with_setup(setup, teardown)
def test_group_send_text():
    pass


@nose.with_setup(setup, teardown)
def test_group_send_media():
    pass


@nose.with_setup(setup, teardown)
def test_group_send_by_file():
    pass


@nose.with_setup(setup, teardown)
def test_group_clean():
    pass


@nose.with_setup(setup, teardown)
def test_main():
    pass
