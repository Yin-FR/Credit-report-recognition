#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: manager.py.py
# @Author: 檀寅
# @Time: 2020年08月19日10:11
# @说明: 脚本执行模块

from flask_script import Manager
from app.app import app1

if __name__ == "__main__":
    server = Manager(app1)

    server.run()