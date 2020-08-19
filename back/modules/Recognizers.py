#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: Recognizers.py
# @Author: 檀寅
# @Time: 2020年08月19日09:46
# @说明: 

import os
from abc import ABCMeta, abstractmethod

from modules.img_propro import rotCorrect
from modules.table_rec import call_api
from modules.result_process import result_process
from modules.show_results import show_result


class Recognizers(metaclass=ABCMeta):
    def __init__(self, filePath, accounts, index):
        self.file_path = filePath
        self.file_type = os.path.split(self.file_path)[1]
        self.account_ali = accounts['ali']
        self.account_mysql = accounts['mysql']
        self.index = index

    # 文件类型转换， 若为pdf则转换为img格式
    @abstractmethod
    def file_type_convert(self):
        pass

    # img预处理
    @abstractmethod
    def img_pre_processing(self):
        pass

    # 表格识别
    @abstractmethod
    def table_recog(self):
        pass

    # 结果后处理
    @abstractmethod
    def result_process(self):
        pass

    # 将结果转换为k-v形式
    @abstractmethod
    def transfer_result(self):
        pass

    # 将识别结果发送至服务器
    @abstractmethod
    def call_service(self):
        pass

    # 将结果存储至database
    @abstractmethod
    def store_into_database(self):
        pass


# img格式识别
class Recognizer_img(Recognizers, metaclass=ABCMeta):
    def __init__(self, imgPath, accounts, index):
        super().__init__(imgPath, accounts, index)

    def file_type_convert(self):
        pass

    def img_pre_processing(self):
        rotCorrect(self.file_path)

    def table_recog(self):
        self.result_path = call_api(self.file_path, self.account_ali)[2]
        return self.result_path

    @abstractmethod
    def result_process(self):
        pass

    @abstractmethod
    def transfer_result(self):
        pass

    @abstractmethod
    def store_into_database(self):
        pass

    @abstractmethod
    def call_service(self):
        pass


class Recognizer_img_0(Recognizer_img):
    def __init__(self, imgPath, accounts, index):
        super().__init__(imgPath, accounts, index)

    def result_process(self):
        result_process(self.index, self.result_path)

    def transfer_result(self):
        self.result_json = show_result(self.result_path, self.index)
        return self.result_json

    def store_into_database(self):
        pass

    def call_service(self):
        pass
