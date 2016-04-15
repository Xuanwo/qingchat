#!/usr/bin/env python
# -*- coding: utf-8 -*-

from qingchat import cli
import os
import sys
import yaml


def test_home():
    if sys.platform == 'darwin':
        user = os.environ['USER']
        assert cli.home == '/Users/%s/.qingchat' % (user)


def test_init():
    pass


def test_save_config(tmpdir):
    tmp_config_path = tmpdir.join('/config.yml')
    tmp_config_path.write('')
    tmp_config_file = str(tmp_config_path.dirpath()) + '/config.yml'
    test_dict = {
        "test": "test_data"
    }
    cli.save_config(test_dict, tmp_config_file)
    with open(tmp_config_file) as f:
        assert yaml.load(f) == test_dict


def test_load_config(tmpdir):
    tmp_config_path = tmpdir.join('/config.yml')
    test_data = '''
        "test": "test_data"
    '''
    tmp_config_path.write(test_data)
    tmp_config_file = str(tmp_config_path.dirpath()) + '/config.yml'
    real_data = cli.load_config(tmp_config_file)
    with open(tmp_config_file) as f:
        assert yaml.load(f) == real_data


def test_config_ip(tmpdir):
    test_ip = '8.8.8.8'
    tmp_config_path = tmpdir.join('/config.yml')
    tmp_config_path.write('"ip": "127.0.0.1"')
    tmp_config_file = str(tmp_config_path.dirpath()) + '/config.yml'
    cli.config_ip(test_ip, tmp_config_file)
    with open(tmp_config_file) as f:
        assert f.read() == 'ip: %s\n' % (test_ip)


def test_config_port(tmpdir):
    test_port = 4000
    tmp_config_path = tmpdir.join('/config.yml')
    tmp_config_path.write('"port": 3000')
    tmp_config_file = str(tmp_config_path.dirpath()) + '/config.yml'
    cli.config_port(test_port, tmp_config_file)
    with open(tmp_config_file) as f:
        assert f.read() == 'port: %s\n' % (test_port)


def test_config_login():
    pass
