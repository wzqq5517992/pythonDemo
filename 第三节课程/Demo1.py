#coding:utf8

#定义函数
# def print_info():
#     print('__________________')
#     print('人生苦短，我用Python')
#     print('__________________')
# print_info()
#
#
# #带参数的函数
# #计算正方体的体积
# def get_volume(x):
#     print("体积是"+str(x*x*x))
# get_volume(3)
# get_volume(4)
# #如果带多个参数呢？多个参数，使用逗号进行隔开
# def get_values(x,y):
#     print("长方形面积"+str(x*y))
# get_values(3,4)

#带返回值的函数
def get_volume1(x):
    return x*x*x

c=get_volume1(3)
print(c)

#如果函数的返回值有多个呢？
def get_volume2(x):
    #想要得到立方体面积，正方形的面积
    return x*x*x,x*x

#在调用时候，有2个参数进行接收
d,e=get_volume2(4)
print(d)
print(e)










