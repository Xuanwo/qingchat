# Qingchat

This package is still under development, **do not** use it in production evrironment.
[中文文档参见此处]()

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
if `group id` is given, add this group into your list.

```
qingchat group send -t <content>
qingchat group send -i <media>
```

Send message to your list.
`content` can be text and `media` can be any media in your computer or url.

## Todo
- [x] Provide a auto setup for environment.
- [ ] Auto show qrcode for login.
- [x] Finish work of cli.
- [x] Group
- [ ] Friend
- [ ] User