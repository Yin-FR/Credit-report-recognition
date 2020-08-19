#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: data_store.py
# @Author: 檀寅
# @Time: 2020年08月19日09:46
# @说明: 存储数据到数据库（mysql）

import pymysql
import pandas as pd

def data_store(dic, account):
    info = []
    for each_pic_info in dic.values():
        for each_key, each_value in zip(each_pic_info.keys(), each_pic_info.values()):
            if each_key == '被查询者姓名':
                name = each_value
            else:
                name = ' '
            info.append({each_key: each_value})
    account_info = pd.read_csv(account)
    [host, user, password, database] =  [account_info[each][0] for each in account_info.columns]
    config = {
        "host": host,
        "user": user,
        "password": password,
        "database": database
    }
    db = pymysql.connect(**config)
    cursor = db.cursor()

    sql = "	INSERT INTO index_info(name) VALUES('{}')".format(name)
    cursor.execute(sql)
    db.commit()

    sql = "SELECT id FROM index_info ORDER BY id DESC LIMIT 1 ;"
    cursor.execute(sql)
    data = cursor.fetchall()
    id = str(data[0][0])

    sql = "CREATE TABLE {} (item_key VARCHAR(255) UNIQUE NOT NULL, item_value VARCHAR(255)) ;".format('table_' + id)
    cursor.execute(sql)
    db.commit()

    sql = " INSERT INTO {}(item_key, item_value) VALUES ('id', '{}') ;".format('table_' + id, id)
    cursor.execute(sql)
    db.commit()

    for each in info:
        for each_key, each_value in zip(each.keys(), each.values()):
            sql = "INSERT INTO {} (item_key, item_value) VALUES ('{}', '{}')".format('table_' + id, each_key, each_value)
            cursor.execute(sql)
            db.commit()

    return "完成"