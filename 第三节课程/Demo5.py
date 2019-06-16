#coding:utf8
#全局变量


a=100
def test1():
    #局部变量和全局变量同名，会只用局部变量值
    a=300
    print("----test1---修改前----a={}".format(a))
    a=400
    print("----test1---修改后----a={}".format(a))

#test2读取的还是全局变量，不会受到test1的影响
def test2():
    print("-----test2---a={}".format(a))

test1()
test2()
#在函数里面声明的变量，叫做局部变量


