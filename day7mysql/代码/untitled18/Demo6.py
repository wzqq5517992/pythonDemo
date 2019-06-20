# coding:utf8


"""更新操作"""

# 导入驱动
# as 相当于给他起了一个小明
import mysql.connector as mysql

# 打开数据库连接
# 地址 用户名 密码  指定哪个数据库
cnx = mysql.connect(user='root', password='Wzq5517992@', host='47.93.37.94', database='student', port=3306)
# 获得操作语句的游标
cursor = cnx.cursor()
# 拼接数据库语句
# 更新操作  等同于插入操作
# 插入操作
sqlstr_grade = "update grade set grade_name='三班' where grade_name='二年级二班'"
sqlstr_student = "update student set name='蔡依林-jolin' where id=61"
cursor.execute(sqlstr_student)
# 必须通过commit进行提交到数据库进行执行
cnx.commit()
