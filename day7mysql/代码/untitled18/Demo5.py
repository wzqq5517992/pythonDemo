# coding:utf8


"""查询操作"""

import mysql.connector as mysql

# 打开数据库连接
# 地址 用户名 密码  指定哪个数据库

cnx = mysql.connect(user='root', password='MyNewPass4!', host='47.93.248.15', database='mystudent', port=20010)
# 获得操作语句的游标
cursor = cnx.cursor()

# 查询操作需要返回数据集
sqlstr = "select * from student"
cursor.execute(sqlstr)
# 这里多一步  不在是提交，查询内容
result = cursor.fetchall()
# 可以遍历这个结果集
for row in result:
    print(row[0], end=' ')
    print(row[1], end=' ')
    print(row[2], end=' ')
    print(row[3])
