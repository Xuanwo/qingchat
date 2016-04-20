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

import config
from docopt import docopt
import qingchat
import group
import sender


def main():
    """
    Parse the argument and load config file

    """
    arguments = docopt(__doc__, version=qingchat.__version__)
    currnet_config = config.init()

    if arguments['config']:  # config command
        if arguments['ip']:  # config ip
            config.set_ip(arguments['<ip>'])
        elif arguments['port']:  # config port
            config.set_port(arguments['<port>'])
        elif arguments['login']:  # config login
            config.login()
    elif arguments['group']:  # group command
        if arguments['list']:  # group list
            group.list()
        elif arguments['choose']:  # group choose
            group.choose(arguments['<group_name>'])
        elif arguments['send']:
            if arguments['-t']:  # group send -t
                group.send_text(arguments['<content>'])
            elif arguments['-i']:  # group send -i
                group.send_media(arguments['<media>'])
            elif arguments['-f']:  # group send -f
                sender.group_send_by_file(arguments['<file>'], arguments['<delaytime>'])
        elif arguments['clean']:
            group.clean()
    elif arguments['user']:  # user command
        pass


if __name__ == '__main__':
    main()
