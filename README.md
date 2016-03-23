# Qingchat

This package is still under development, **do not** use it in production evrironment.
[中文文档参见此处](https://github.com/Xuanwo/qingchat/blob/master/README-CN.md)

Qingchat only support python3 now.

## Install

### Pip

```
pip3 install qingchat
```

## Setup

## Usage

### Config

```
qingchat config login
```

Login your wechat(you should setup your perl server)

```
qingchat config ip <ip>
```

Set your server ip as `<ip>`

```
qingchat config port <port>
```

Set your server port as `<port>`

### User

Under development

### Friend

Under development

### Group

```
qingchat group list
```

Show all your groups by name.

```
qingchat group choose <group_name>
```

Show all groups that you had chosen.
if `group_name` is given, add this group into your list.

> `group_name` support regex and you can use `test*` to choose `test1`, `test2` and so on.

```
qingchat group send -t <content>
qingchat group send -i <media>
qingchat group send -f <file> [<delaytime>]
```

Send message to your list.

- `-t` option is used to send text message
- `-i` option is used to send media message
- `-f` option is used to send message by file

> <media> can be absolute path or url
> <file> must be an absolute path to a pure text file, and do not support `doc`, `docs` and so on
> <delaytime> is the time between two message by seconds, default set to 0s