# coding:utf8
"""
期望返回一个网页

"""

from flask import Flask
from flask import render_template
import json

app = Flask(__name__)


# 编写路由  你访问的网络地址，谁响应
@app.route("/")  # 实际上叫做装饰器
def hello_world():
    # render_template  里面实现读取templates文件夹下的html文件，进行返回数据
    return render_template('index.html')
    # return "hello world"


# 对网页传入数据
@app.route("/test1")
def test1():
    return render_template('index.html', num=1)


# 通过run进行启动
app.run()
