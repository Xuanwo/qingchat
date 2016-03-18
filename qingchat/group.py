#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from qingchat.cli import address


def get_group_info():
    url = address + 'openwx/get_group_info'
    r = requests.get(url)
    # print(requests.get(url).text)
    return r.json()


def send_group_message(id='', markname='', media_path='', content=''):
    data = {
        'id': id,
        'markname': markname,
        'media_path': media_path,
        'content': content
    }
    url = address + send_group_message
    r = requests.post(url, data=data)
    # print(r.json())
    return r.json()


if __name__ == '__main__':
    pass
    # get_group_info()
    # send_group_message(id='@@d9713265789d8e4aad433ebd8f1d8b72f82262e9798dced5ce181cea971feaa3',
    #                    content='test send from Qingchat again')
    # send_group_message(id='@@f5ccd4ad2eee415ecadac9bfb2e72af388b1e998d1c980990cfbe9164f8f0c54',
    #                    content='test send from Qingchat again')
    # send_group_message(id='@@d9713265789d8e4aad433ebd8f1d8b72f82262e9798dced5ce181cea971feaa3',
    #                    media_path='https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png')
    #
    # send_group_message(id='@@f5ccd4ad2eee415ecadac9bfb2e72af388b1e998d1c980990cfbe9164f8f0c54',
    #                    media_path='/media/Data/Code/qingchat/qingchat/logo.png')
    # send_group_message(id='@@d9713265789d8e4aad433ebd8f1d8b72f82262e9798dced5ce181cea971feaa3',
    #                    media_path='/media/Data/Code/qingchat/qingchat/logo.png')
    # send_group_message(markname='Qingchat_test_1',
    #                    content='test send from Qingchat')
