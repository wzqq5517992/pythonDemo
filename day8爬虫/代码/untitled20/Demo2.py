# coding:utf8
"""
有了数据以后
期望搭建网站，是使用web框架
flask 更新很慢 不挑版本
pip install flask

"""

from flask import Flask
import json

app = Flask(__name__)


# 编写路由  你访问的网络地址，谁响应
@app.route("/")  # 实际上叫做装饰器
def hello_world():
    print("helloworld")
    return "hello world"


# 写接口的方式
@app.route("/jsontest")
def jsontest123():
    dict1 = {'name': 'wzq', 'age': 18}
    str1 = json.dumps(dict1)
    return str1


# 通过run进行启动
app.run()
