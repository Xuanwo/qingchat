# 0.3.3

## Bug Fixes

- Fix getenv error on Windows

# 0.3.2

## Bug Fixes

- Fix qrcode open error on Mac OS X

# 0.3.1

## Bug Fixes

- Fix `group clean` can't use
- Fix re.match error while choose Chinese group name

# 0.3.0

## Features

- add `config login`, allow user scan the qrcode directly

# 0.2.1

## Bug Fixes

- Fix error while delaytime set as Int
- Fix error while run `group choose` before `group list` and add info
- Complete `install_requires`

# 0.2.0

## Features

- add `group send -f` command, allow user to send message from file

## Bug Fixes

- Fix `os.mknod` can't use in win platform

## Breaking Changes

- `group_send_image` changed into `group_send_media`

# 0.1.0

## Features

- add `config ip/port` command

## Breaking Changes

- `write_config` changed into `save_config`
- `address` in config file changed into `ip`

# 0.0.3

## Features

- `group send` support send media like pics.
- `group choose` support regex like `Qingchat_test_*`

## Bug Fixes

- Fix error while config['group'] is empty

## Breaking Changes

- Do not support `group choose` without option anymore

# 0.0.2

## Features

- Support `group` command with `list`, `choose`, `send`

## Bug Fixes

- Fix config file in different platform

# 0.0.1

## Features

- Support CLI