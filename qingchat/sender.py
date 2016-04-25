import group
import time


# TODO: 好友&群组批量发送消息,媒体文件

def group_welcome(groudid):
    group.send_text()


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
                group.send_media(i[1:])
            else:
                group.send_text(i)
    print("文件发送完毕！")

