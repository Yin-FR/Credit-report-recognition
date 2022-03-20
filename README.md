# Chinese Credit Report Recognization (Bank of China)
# 中文征信报告识别（中国银行）
### 配置要求：
- 项目后端基于**python3.7**实现，调用阿里OCR表格识别API
- 项目前端基于**Vue.js 2.6.11**实现
- 接口框架：**Flask 1.1.2**
- 数据库：**MySQL**
----
### 使用场景
用户通过网页端拍照上传/从相册选择符合条件的征信报告图片，后端将上传图片识别为表格，并通过kv对形式返回网页端展示给用户。若信息识别不完全，则要求用户手动补全所缺信息或重新上传图片。获取所需信息后，浏览器提醒用户校对信息，用户确认无误后，后端根据由服务器传回的信息，判断该用户是否通过征信审核，并将审核结果和用户信息录入数据库。

----
### 工作流程
- 总体流程：
<img src="https://github.com/YinTAN-Stan/Credit-Doc-Recognition-completed-version/blob/master/back_end/imgs/total_process.png?raw=true">

- 后端流程：
<img src="https://github.com/YinTAN-Stan/Credit-Doc-Recognition-completed-version/blob/master/back_end/imgs/server_process.png?raw=true">

