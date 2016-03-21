# Qingchat

这个包仍处于重度开发阶段，请**不要**应用于生产环境。

## 安装

### Pip

```
pip3 install qingchat
```

## 配置

## 用法

### Group

```
qingchat group list
```

显示所有你的群组

```
qingchat group choose <group_name>...
```

将指定群组加入你的列表，并显示你列表中已经拥有的群组。

> <group_name>参数支持正则，你可以使用`test*` 来选择 `test1`, `test2` 及其他

```
qingchat group send -t <content>
qingchat group send -i <media>
```

向你列表中的群组发送内容。
`-t`参数用于发送文本信息，`-i`参数用于发送各种媒体文件（*图片会以缩略图形式显示，但音频文件会以文件形式显示*）
