#coding:utf8





"""删除操作"""




#as 相当于给他起了一个小明
import mysql.connector as mysql
#打开数据库连接
#地址 用户名 密码  指定哪个数据库

cnx=mysql.connect(user='root',password='MyNewPass4!',host='47.93.248.15',database='mystudent',port=20010)
#获得操作语句的游标
cursor=cnx.cursor()
#拼接数据库语句


#删除操作  等同于插入操作
#插入操作
sqlstr="delete from student where stu_name ='刘小白'"
cursor.execute(sqlstr)
#必须通过commit进行提交到数据库进行执行
cnx.commit()

