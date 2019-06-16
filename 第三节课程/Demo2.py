#coding:utf8
#函数的嵌套
#多个函数之前的调用

#定义2个函数  testA  testB
#testA中调用testB  可不可以？
def testB():
    print("------testB start-----")
    print("------testB执行内容-----")
    print("------testB end-------")

def testA():
    print("------testA start-----")
    testB()
    print("------testA end-------")

testA()

