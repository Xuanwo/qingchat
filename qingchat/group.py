from cli import address, config, home
import cli
import re
import requests
import time


def group_list():
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
    cli.save_config(config)
    return config['group']


def group_choose(group_name):
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


def group_send_text(content):
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


def group_send_media(media):
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


def group_send_by_file(file, delaytime=0):
    """
    Send message to your chosen_group list by file

    :param file: the path to the file you want to use
    :param delaytime: set the delaytime in two message in seconds, defaults to 0s
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
    Clean all your chosen_group list

    """
    tmpconfig = cli.load_config()
    if 'chosen_group' in tmpconfig:
        del tmpconfig['chosen_group']
        cli.save_config(tmpconfig)
        print("您选中的群组均已被删除。")
