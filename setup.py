#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import qingchat

entry_points = {
    "console_scripts": [
        "qingchat = qingchat.cli:main",
    ]
}

setup(
    name="qingchat",
    version=qingchat.__version__,
    url="https://xuanwo.org/",
    author="Xuanwo",
    author_email="xuanwo.cn@gmail.com",
    description="Qingchat is a simple wechat framework, written in Python.",
    long_description="Qingchat is a simple wechat framework, written in Python.",
    keywords="qingchat, wechat",
    license="MIT License",
    packages=find_packages(),
    include_package_data=True,
    entry_points=entry_points,
    requires=[
        'requests',
        'pyyaml',
        'flask',
    ],
    install_requires=[
        'docopt',
        'pyyaml',
        'requests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
    ],
)
