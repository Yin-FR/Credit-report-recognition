#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: table_rec.py
# @Author: 檀寅
# @Time: 2020年08月19日09:46
# @说明: 识别

import os
import pandas as pd
import base64
import json

import urllib.request

ENCODING = "utf-8"


# 获取图片的base64编码
def get_img_base64(imgPath):
    with open(imgPath, 'rb') as infile:
        s = infile.read()
        return base64.b64encode(s).decode(ENCODING)


# 获取http status code、header、content 用于调取接口
def predict(url, appcode, img_base64, kv_configure):
    param = {}
    param['image'] = img_base64
    if kv_configure is not None:
        param['configure'] = json.dumps(kv_configure)
    body = json.dumps(param)
    data = bytes(body, ENCODING)

    headers = {'Authorization': 'APPCODE %s' % appcode}
    request = urllib.request.Request(url=url, headers=headers, data=data)
    try:
        response = urllib.request.urlopen(request, timeout=30)
        return response.code, response.headers, response.read()
    except urllib.request.HTTPError as e:
        return e.code, e.headers, e.read()


# 调取接口
def call_api(imgPath, accountAli):
    """
        函数功能：调取Aliyun接口进行表格识别，识别结果以xlsx格式保存在特定路径下。
        ----------------------------------------------------------------
        :param imgPath: 待识别的png文件路径
        :param accountAli: Aliyun接口凭证路径，文件格式为csv，表头为：appcode
        :return: 返回tuple格式，各项按顺序为字符串，xlsx格式的json字符串，输出xlsx文件路径
    """
    img_path_dir, img_temp_name = os.path.split(imgPath)
    img_name, img_extension = os.path.splitext(img_temp_name)

    appcode = pd.read_csv(accountAli)['appcode'][0]
    url = 'http://form.market.alicloudapi.com/api/predict/ocr_table_parse'
    configure = {'format': 'xlsx'}  # 返回xlsx格式

    img_base64data = get_img_base64(imgPath)
    stat, header, content = predict(url, appcode, img_base64data, configure)
    # 若错误，则返回错误信息
    if stat != 200:
        print('Http status code: ', stat)
        print('Error msg in header: ', header['x-ca-error-message'] if 'x-ca-error-message' in header else '')
        print('Error msg in body: ', content)
        exit()
    result_str = content

    result_str.decode(ENCODING)
    result = json.loads(result_str)

    # 结果保存路径，若无该路径则创建
    xlsx_path = 'datas/rec_results'
    if not os.path.exists(xlsx_path):
        os.makedirs(xlsx_path)

    # 保存结果为xlsx格式
    xlsx_file = os.path.join(xlsx_path, img_name) + '.xlsx'
    with open(xlsx_file, 'wb') as fout:
        fout.write(base64.b64decode(result['tables']))

    print("识别完成")

    return result_str, result, xlsx_file