 #!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from qingchat.cli import address

base = address + 'openwx/get_friend_info'


def get_friend_info():
    print(requests.get(base).text)




if __name__ == '__main__':
    get_friend_info()
