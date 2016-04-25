from config import address
import config
import re
import utils


def invite(person_id, group_name):
    """
    Invite someone into group

    :param person_id: the one you want to invite
    :param group_name: the group you want to invite into
    """
    data = {
        "friend": person_id,
        "displayname": group_name
    }
    r = utils.post(address + 'invite_friend', data).json()
    if not r['code']:
        print("已邀请好友 %s 加入群组 %s" % (person_id, group_name))
    else:
        print("邀请失败!")


def kick(person_id, group_name):
    """
    Kick someone from group (you must be the admin of this group)

    :param person_id: the one you want to kick
    :param group_name: the group you want to kick from
    """
    data = {
        "member": person_id,
        "displayname": group_name
    }
    r = utils.post(address + 'kick_group_member', data).json()
    if not r['code']:
        print("指定成员 %s 已经从群组 %s 中删除" % (person_id, group_name))
    else:
        print("删除失败!")


def list():
    """
    Show all your group

    :return: the json of group info
    """
    current_config = config.load()
    r = utils.get(address + 'get_group_info')
    print("您的群组为：")
    current_config['group'] = []
    content = r.json()
    for i in content:
        current_config['group'].append(i['displayname'])
        print("群名称： " + i['displayname'])
    config.save(config)
    return current_config['group']


def choose(group_name):
    """
    Add group_name into chosen_group list

    :param group_name: group_name to be chosen, support re
    :return: list of chonsen groups
    """
    current_config = config.load()
    if 'chosen_group' not in config or not current_config['chosen_group']:
        current_config['chosen_group'] = []
    if not current_config['group']:
        print("请先获取群组信息")

    for i in group_name:
        for j in current_config['group']:
            if re.match(i, j) \
                    and re.match(i, j).group() != '' \
                    and j not in current_config['chosen_group']:
                # Sometime re.match will return empty str
                current_config['chosen_group'].append(j)

    config.save(current_config)
    print("您已经选择的群组：")
    for i in current_config['chosen_group']:
        print("群名称： " + i)


def send_text(group_name, content):
    """
    Send text message to your chosen_group list

    :param group_name: the group you want to send to
    :param content: your text message
    """
    data = {
        'displayname': group_name,
        'content': content
    }
    r = utils.post(address + 'send_group_message', data).json()
    if not r['code']:
        print("消息已发送到 %s " % (group_name))
    else:
        print("消息发送失败!")


def send_media(group_name, media):
    """
    Send media message to your chosen_group list

    :param media: your media in url or path
    """
    data = {
        'displayname': group_name,
        'media_path': media
    }
    r = utils.post(address + 'send_group_message', data).json()
    if not r['code']:
        print("多媒体已发送到 %s " % (group_name))
    else:
        print("多媒体发送失败!")


def clean():
    """
    Clean all your chosen_group list

    """
    tmpconfig = config.load()
    if 'chosen_group' in tmpconfig:
        del tmpconfig['chosen_group']
        config.save(tmpconfig)
        print("您选中的群组均已被删除。")
