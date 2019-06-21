# coding:utf8
"""
1、建立flask工程
2、连接数据库
3、建立路由
4、读取数据库信息
5、返回页面和数据库读取信息
6、页面使用jinja2模板语言进行循环
"""

from flask import Flask
from flask import render_template
import mysql.connector as mysql
import requests

cnx = mysql.connect(user='root', password='Wzq5517992@', host='47.93.37.94', database='movie', port=3306)
# 获得游标
cursor = cnx.cursor()

app = Flask(__name__)


@app.route('/')
def test123():
    cursor.execute("select name,playUrl,score from movie ")
    restul = cursor.fetchall()


    movielist = []
    for m in restul:
        movielist.append({'name': m[0], 'playurl': m[1], 'score': m[2]})

    return render_template('index1.html', movies=movielist)


app.run()
