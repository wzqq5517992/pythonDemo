#coding:utf8

#综合练习
#如何做到我要插入一个同学，这个同学存在就不插入，如果不存在，就执行插入操作


#思路
#先查询这个同学在不在
#如果不存在执行插入语句

import mysql.connector as mysql
cnx=mysql.connect(user='root',password='MyNewPass4!',host='47.93.248.15',database='mystudent',port=20010)
#获得操作语句的游标
cursor=cnx.cursor()

#执行插入
sqlstr="select * from student where stu_name='全村的希望'"
cursor.execute(sqlstr)
result=cursor.fetchall()
#如果结果集有数据，则表示他存在
if len(result)>0:
    print("存在")
else:
    print("不存在")
    sqlstr="insert into student(id,stu_name,age,grade_id)values(10,'全村的希望',20,19)"
    cursor.execute(sqlstr)
    #不要忘记提交
    cnx.commit()



