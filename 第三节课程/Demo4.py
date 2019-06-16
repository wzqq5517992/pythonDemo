#coding:utf8
#全局变量和局部变量
def test1():
    a =300
    print("----test1---修改前----a={}".format(a))
    a=200
    print("----test1---修改后----a={}".format(a))
def test2():
    a=400
    print("-----test2---a={}".format(a))

test1()
test2()
#在函数里面声明的变量，叫做局部变量


