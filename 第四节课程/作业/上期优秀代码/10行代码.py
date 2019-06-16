from random import *
list1 = [["早上", "中午", "傍晚", "半夜"], ["小明", "小李", "小王", "小黑"], ["在房上", "在地下", "在电梯里", "在厕所里"], ["吃饭", "遛狗", "飞翔", "看书"]]
while True:
    novel = input("请输入数字1随机生成小说(否则退出系统):")
    if novel == "1":
        fiction = choice(list1[0]) + choice(list1[1]) + choice(list1[2]) + choice(list1[3])
    else:
        print("系统已退出")
    with open('小说.txt', "a") as file:
        file.write(fiction)