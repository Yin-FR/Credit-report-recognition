from flask import Flask, request
from flask_cors import CORS # 处理跨域请求
import os
import json

from modules.data_store import data_store
from modules.Recognizers import Recognizer_img_0

app1 = Flask(__name__)
CORS(app1, supports_credentials=True)

accounts = {
    'ali': 'static/accounts/accountAli.csv',
    'mysql': 'static/accounts/accountMysql.csv'
}

rcs = {
    'rc_0': None,
    'rc_1': None
}



@app1.route('/get/data', methods=['POST']) # 用于接收图片的接口
def getData():
    if request.method == 'POST':
        index = request.form.get('index')
        file_obj = request.files['file']
        pic_name = file_obj.filename
        if not os.path.exists('datas/imgs'):
            os.makedirs('datas/imgs')
        pic_path = os.path.join('datas/imgs', pic_name)
        file_obj.save(pic_path)
        if index == '0':
            rcs['rc_0'] = Recognizer_img_0(pic_path, accounts=accounts, index=index)
            rcs['rc_0'].img_pre_processing()
        elif index == '1':
            rcs['rc_1'] = Recognizer_img_0(pic_path, accounts=accounts, index=index)
        else:
            pass

        print(rcs)
        return "成功"

@app1.route('/get/js', methods=['POST']) # 用于存储数据的接口
def getJs():
    for root, dirs, files in os.walk('datas', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    if request.method == 'POST':
        data = request.get_data()
        data_dic = json.loads(data)
        res = data_store(data_dic, account="static/accounts/accountMysql.csv")
        res = json.dumps(res)



        return res

@app1.route('/return/data', methods=['GET']) # 用于接收识别请求并返回识别结果
def return_data():
    if request.method == 'GET':
        index = request.args.get('index')
        if index == '0':
            rc = rcs['rc_0']
        elif index == '1':
            rc = rcs['rc_1']
        else:
            rc = None
        rc.img_pre_processing()
        rc.table_recog()
        data = rc.transfer_result()
        return data

@app1.errorhandler(413)
def too_large_request(err):
    return json.dumps("图片模糊元素过多，请重新刷新页面并上传图片")


if __name__ == '__main__':
    app1.run()
