from config import address
import config
import cli
import re
import requests
import utils
import time


def add():
    pass


def delete():
    pass


def list():
    """
    Show all your group

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
    config.save(config)
    return config['group']


def choose(group_name):
    """
    Add group_name into chosen_group list

    :param group_name: group_name to be chosen, support re
    :return: list of chonsen groups
    """
    if 'chosen_group' not in config or not config['chosen_group']:
        config['chosen_group'] = []
    if not config['group']:
        print("请先获取群组信息")

    for i in group_name:
        for j in config['group']:
            if re.match(i, j) \
                    and re.match(i, j).group() != '' \
                    and j not in config['chosen_group']:
                # Sometime re.match will return empty str
                config['chosen_group'].append(j)

    cli.save_config(config)
    print("您已经选择的群组：")
    for i in config['chosen_group']:
        print("群名称： " + i)

    return config['chosen_group']


def send_text(content):
    """
    Send text message to your chosen_group list

    :param content: your text message
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


def send_media(media):
    """
    Send media message to your chosen_group list

    :param media: your media in url or path
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


def clean():
    """
    Clean all your chosen_group list

    """
    tmpconfig = config.load()
    if 'chosen_group' in tmpconfig:
        del tmpconfig['chosen_group']
        config.save(tmpconfig)
        print("您选中的群组均已被删除。")
