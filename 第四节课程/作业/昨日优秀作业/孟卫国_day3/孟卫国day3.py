""""
作业三   文字编故事
时间   早上、中午、半夜
人物   小明、小李、小白、小黑
地点   在房上、在地下、在电梯里、在厕所里
事件   吃饭、遛狗、飞翔、看书
通过不同的抽签组合，可以出现很多有意思的事件，比如  早上 小明 在厕所里 吃饭，遇到这样的，就会捧腹大笑，现在通常程序来实现以上功能
要求
程序一开始输入4个数字，4321
生成一段故事 
把这段故事保存为文件
                                孟卫国        2019-06-15

"""
import random


def sjsj():
    shijian = ['早上', '中午', '半夜']  # 使用random 随机取时间
    shijian = random.choice(shijian)
    return shijian


def sjrw():
    renwu = ['小明', '小李', '小白', '小黑']  # 使用random 随机人物
    renwu = random.choice(renwu)
    return renwu


def sjdd():
    didian = ['在房上', '在地下', '在电梯里', '在厕所里']  # 使用random 随机地点
    didian = random.choice(didian)
    return didian


def sjsw():
    shiwu = ['吃饭', '遛狗', '飞翔', '看书']  # 使用random 随机取事务
    shiwu = random.choice(shiwu)
    return shiwu


while True:
    a = input("请输入数字")  # 输入故事的计数
    if int(a) <= 49:
        b = ("第" + a + "个故事：" + sjsj() + sjrw() + sjdd() + sjsw())  # 调用之前的生成的函数，拼接成需要的故事
        print(b)  # 打印故事
        f = open("第" + a + "个故事.txt", "w")  # 打开（新建）txt
        f.write(b)  # 写入故事
        f.close()  # 关闭文本
    elif int(a) >= 50:
        break  # 退出程序
