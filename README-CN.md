# Qingchat

这个包仍处于重度开发阶段，请**不要**应用于生产环境。

Qingchat 目前仅支持Python 3

## 安装

### Pip

```
pip3 install qingchat
```

## 配置

## 用法

### Config

```
qingchat config login
```

登录您的微信帐号（你首先需要配置好perl后端服务器）

```
qingchat config ip <ip>
```

设置您的服务器ip为`<ip>`

```
qingchat config port <port>
```

设置您的服务器端口为`<port>`

### Group

```
qingchat group list
```

显示所有你的群组

```
qingchat group choose <group_name>...
```

将指定群组加入你的列表，并显示你列表中已经拥有的群组。

> `<group_name>` 参数支持正则，你可以使用`test*` 来选择 `test1`, `test2` 及其他

```
qingchat group send -t <content>
qingchat group send -i <media>
qingchat group send -f <file> [<delaytime>]
```

向你列表中的群组发送内容。
- `-t`参数用于发送文本信息
- `-i`参数用于发送各种媒体文件（*图片会以缩略图形式显示，但音频文件会以文件形式显示*）
- `-f`参数用于从文件中发送信息，一行一条（以回车区分），以`!`（英文半角）符号开头的行将会被识别为媒体文件发送

> `<media>` 参数支持文件绝对路径或Url
> `<file>` 参数仅支持本地绝对路径，仅支持纯文本文件
> `<delaytime>` 参数用于设置发送消息间的间隔时间，单位为秒，默认为0
