import json
import sender, utils

EVENT = [
    'new_group',  # 新加入群聊
    'new_friend',  # 新增好友
    'new_group_member',  # 新增群聊成员
    'lose_group',  # 退出群聊
    'lose_friend',  # 删除好友
    'lose_group_member',  # 成员退出群聊
    'group_property_change',  # 群聊属性变化
    'group_member_property_change',  # 成员属性变化
    'friend_property_change',  # 好友属性变化
    'user_property_change'  # 帐号属性变化
]


def judge(data):
    if data['post_type'] == 'event' and data['event'] in EVENT:
        return data['event']
    else:
        return False


def process():
    data = utils.load_file()
    event = judge(data)
    if event == 'new_group_member':
        print(data['params'][0]['id'])
        # sender.group_welcome(data['params'][0]['id'])
