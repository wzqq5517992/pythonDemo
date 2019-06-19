# coding:utf8


"""查询操作"""

# as 相当于给他起了一个小明
import mysql.connector as mysql

# 打开数据库连接
# 地址 用户名 密码  指定哪个数据库

cnx = mysql.connect(user='root', password='MyNewPass4!', host='47.93.248.15', database='mystudent', port=20010)
# 获得操作语句的游标
cursor = cnx.cursor()
# 拼接数据库语句

# 插入操作
sqlstr = "insert into student(id,stu_name,age,grade_id) values(7,'小明',19,14)"
cursor.execute(sqlstr)
# 必须通过commit进行提交到数据库进行执行
cnx.commit()
