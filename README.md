# Qingchat

This package is still under development, **do not** use it in production evrironment.
[中文文档参见此处](https://github.com/Xuanwo/qingchat/blob/master/README-CN.md)

## Install

### Pip

```
pip3 install qingchat
```

## Setup

## Usage

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
`content` can be text and `media` can be any media in your computer or url.
And you can send message from file by `-f` option, `<file>` is the path to your file, and `<delaytime>` is the time you want to delay by seconds.