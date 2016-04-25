import os
import requests
import sys
import webbrowser
import yaml

home = os.path.expanduser('~/.qingchat')
address = ''
current_config = {}


def init():
    """
    Read config file in ~/.qingchat/config.yml
    If not exsit, add the initconfig about ip and port

    :return: the content fo config file in yaml
    """
    initconfig = dict()
    if not os.path.exists(home):  # create dir for config file
        os.makedirs(home)
    if not os.path.isfile(home + '/config.yml'):  # create config file if noy exist
        open(home + '/config.yml', "w+").close()
        initconfig['ip'] = "127.0.0.1"
        initconfig['port'] = 3000
        initconfig['qrcode_port'] = 3001
        save(initconfig)
    else:
        initconfig = load()

    address = 'http://%s:%d/openwx/' % (initconfig['ip'], initconfig['port'])

    return initconfig


def save(content, config_file=home + '/config.yml'):
    """
    Save config into config file

    :param content: content of config in yaml
    :param config_file: config file
    """
    with open(config_file, "w") as f:
        f.write(yaml.dump(content, default_flow_style=False))


def load(config_file=home + '/config.yml'):
    """
    Load config file from config file in yaml

    :return: yaml of config file
    """
    with open(config_file, "r") as f:
        content = yaml.load(f)
    return content


def set_ip(ip, config_file=home + '/config.yml'):
    """
    Set your server ip as ip

    :param ip: your server's ip
    """
    tmpconfig = load(config_file)
    tmpconfig['ip'] = ip
    print("您的服务器端IP地址被设置为： %s" % ip)
    save(tmpconfig, config_file)
    return ip


def set_port(port, config_file=home + '/config.yml'):
    """
    Set your server ip as port

    :param port: your server's port
    """
    tmpconfig = load(config_file)
    tmpconfig['port'] = port
    print("您的服务器端端口被设置为： %d" % port)
    save(tmpconfig, config_file)
    return port


def set_qrocde_port(port, config_file=home + '/config.yml'):
    '''
    Set your qrcode port

    :param port: qrcode port
    :param config_file: config file location
    '''
    tmpconfig = load(config_file)
    tmpconfig['qrcode_port'] = port
    print("您的二维码端口被设置为: %d" % port)
    save(tmpconfig, config_file)
    return port


def login(address, qrcode_port):
    """
    Download qrcode.jpg and show them in webbrowser

    """
    qrcode = "http://%s:%d/qrcode.jpg" % (address, qrcode_port)  # get qrcode from server
    r = requests.get(qrcode)
    with open("qrcode.jpg", "wb") as f:
        f.write(r.content)

    print("请扫描二维码登录微信")
    if sys.platform.startswith('darwin'):
        os.system("open qrcode.jpg")
    else:
        webbrowser.open("qrcode.jpg")
