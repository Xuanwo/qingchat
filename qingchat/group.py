# !/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import urllib.parse
from qingchat.cli import address

base = address + 'openwx/send_group_message'


def get_group_info():
    print(requests.get(address + 'openwx/get_group_info').text)


def send_group_message(id='', markname='', media_path='', content=''):
    data = {'id': id,
            'markname': markname,
            'media_path': media_path,
            'content': content
            }
    r = requests.post(base, data=data)
    print(r.json())


if __name__ == '__main__':
    # get_group_info()
    # send_group_message(id='@@d9713265789d8e4aad433ebd8f1d8b72f82262e9798dced5ce181cea971feaa3',
    #                    content='test send from Qingchat again')
    # send_group_message(id='@@f5ccd4ad2eee415ecadac9bfb2e72af388b1e998d1c980990cfbe9164f8f0c54',
    #                    content='test send from Qingchat again')
    # send_group_message(id='@@d9713265789d8e4aad433ebd8f1d8b72f82262e9798dced5ce181cea971feaa3',
    #                    media_path='https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png')

    send_group_message(id='@@f5ccd4ad2eee415ecadac9bfb2e72af388b1e998d1c980990cfbe9164f8f0c54',
                       media_path='/media/Data/Code/qingchat/qingchat/logo.png')
    send_group_message(id='@@d9713265789d8e4aad433ebd8f1d8b72f82262e9798dced5ce181cea971feaa3',
                       media_path='/media/Data/Code/qingchat/qingchat/logo.png')
    # send_group_message(markname='Qingchat_test_1',
    #                    content='test send from Qingchat')
