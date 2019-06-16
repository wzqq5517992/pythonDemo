#coding:utf8
#全局变量  修改全局变量


a=100
def test1():
    global a
    #修改全局变量，通过一个关键字global 声明引用的是全局变量，这样就可以进行修改
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


#总结
#全局变量在函数中可以引用，但是不能修改
#在函数中出现变量名=数据 意味着变量名为局部变量
#如果需要函数中修改全局变量 需要使用global来声明为全局变量


