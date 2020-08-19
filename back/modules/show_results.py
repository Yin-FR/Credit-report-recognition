#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: show_results.py
# @Author: 檀寅
# @Time: 2020年08月19日09:46
# @说明: 返回json识别结果

import xlrd
import json


def show_result(xlsx_path, index):
    print(xlsx_path)

    information = []

    workbook = xlrd.open_workbook(xlsx_path)
    worksheets = workbook.sheets()

    items_searched_0 = ["被查询者姓名", "被查询者证件号码", "性别", "出生日期", "手机号码", "单位电话", "住宅电话", "通讯地址", "户籍地址"]
    items_searched_1_0 = ['贷款逾期：笔数', '贷款逾期：月份数', '贷款逾期：单月最高逾期总额', '贷款逾期：最长逾期月数', '贷记卡逾期：账户数',
                        '贷记卡逾期：月份数', '贷记卡逾期：单月最高逾期总额', '贷记卡逾期：最长逾期月数', '准贷记卡60天以上透支：账户数',
                        '准贷记卡60天以上透支：月份数', '准贷记卡60天以上透支：单月最高透支余额', '准贷记卡60天以上透支：最长透支月数']
    items_searched_1_0_origin = ['笔数', '月份数', '单月最高逾期总额', '最长逾期月数', '账户数', '单月最高透支余额', '最长透支月数']
    items_searched_1_1 = ['发卡法人机构数', '发卡机构数', '账户数', '授信总额', '单家行最高授信额', '单家行最低授信额', '已用额度', '最近6个月平均使用额度']
    items_searched_2 = ['']

    if index == '0':
        items_searched = items_searched_0
    elif index == '1':
        items_searched = items_searched_1_0 + items_searched_1_1
    elif index == '2':
        items_searched = items_searched_2
    else:
        items_searched = []

    for each_item in items_searched:
        information.append({'item': each_item, 'itemValue': None})

    if index == '0':
        for each_worksheet in worksheets:
            for i in range(each_worksheet.nrows):
                for j in range(each_worksheet.ncols):
                    if each_worksheet.cell(i, j).value in items_searched:
                        for each_item in information:
                            if each_item['item'] == each_worksheet.cell(i, j).value:
                                each_item['itemValue'] = each_worksheet.cell(i + 1, j).value

    if index == '1':
        months = []
        total_overdue = []
        month_overdue_max = []
        number_accounts = []
        print(months, total_overdue, month_overdue_max, number_accounts)
        for each_ws in worksheets:
            for i in range(each_ws.nrows):
                for j in range(each_ws.ncols):
                    if each_ws.cell(i, j).value == items_searched_1_0_origin[0]:
                        information[0]['itemValue'] = each_ws.cell(i + 1, j).value
                    if each_ws.cell(i, j).value == items_searched_1_0_origin[1]:
                        months.append(each_ws.cell(i + 1, j).value)
                    if each_ws.cell(i, j).value == items_searched_1_0_origin[2]:
                        total_overdue.append(each_ws.cell(i + 1, j).value)
                    if each_ws.cell(i, j).value == items_searched_1_0_origin[3]:
                        month_overdue_max.append(each_ws.cell(i + 1, j).value)
                    if each_ws.cell(i, j).value == items_searched_1_0_origin[4]:
                        number_accounts.append(each_ws.cell(i + 1, j).value)
                    if each_ws.cell(i, j).value == items_searched_1_0_origin[5]:
                        information[10]['itemValue'] = each_ws.cell(i + 1, j).value
                    if each_ws.cell(i, j).value == items_searched_1_0_origin[6]:
                        information[11]['itemValue'] = each_ws.cell(i + 1, j).value
        if len(months):
            information[1]['itemValue'] = months[0]
            if len(months) > 1:
                information[5]['itemValue'] = months[1]
                if len(months) > 2:
                    information[9]['itemValue'] = months[2]
        if len(total_overdue):
            information[2]['itemValue'] = total_overdue[0]
            if len(total_overdue) > 1:
                information[6]['itemValue'] = total_overdue[1]
        if len(month_overdue_max):
            information[3]['itemValue'] = month_overdue_max[0]
            if len(month_overdue_max) > 1:
                information[7]['itemValue'] = month_overdue_max[1]
        if len(number_accounts):
            information[4]['itemValue'] = number_accounts[0]
            if len(number_accounts) > 1:
                information[8]['itemValue'] = number_accounts[1]
        for each_ws in worksheets:
            for i in range(each_ws.nrows):
                for j in range(each_ws.ncols):
                    if each_ws.cell(i, j).value in items_searched_1_1:
                        for each_item in information:
                            if each_item['item'] == each_ws.cell(i, j).value:
                                each_item['itemValue'] = each_ws.cell(i + 1, j).value
    print(information)



    print(json.dumps(information))
    return json.dumps(information)