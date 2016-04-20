import json
import sender, utils

# TODO: 处理来自openwx的上报信息

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

