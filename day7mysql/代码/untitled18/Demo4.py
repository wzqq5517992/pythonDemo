# coding:utf8


"""查询操作"""

# as 相当于给他起了一个小明
import mysql.connector as mysql

# 打开数据库连接
# 地址 用户名 密码  指定哪个数据库

cnx = mysql.connect(user='root', password='Wzq5517992@', host='47.93.37.94', database='student', port=3306)
# 获得操作语句的游标
cursor = cnx.cursor()
# 拼接数据库语句

# 插入操作
sqlstr_student = "insert into student(name,age,grade_id) values('蔡依林',19,1),('罗志祥',19,2)," \
                                                 "('潘玮柏',19,3),('杨丞琳',19,4)," \
                                                 "('安以轩',19,5),('何炅',19,6),('汪涵',19,7)," \
                                                 "('欧弟',17,8),('周杰伦',19,9),('李响',19,10)"

sqlstr_grade = "insert into grade(grade_name) values('一年级一班'),('二年级二班')"

cursor.execute(sqlstr_student)
# 必须通过commit进行提交到数据库进行执行
cnx.commit()
