print("你好，我是机器人小U，现在和你玩一个游戏：抽签写故事。具体要素如下：\n"
      "时间（1-3）：早上、中午、半夜\n"
      "人物（1-4）：小明、小李、小白、小黑\n"
      "地点（1-4）：在房上、在地下、在电梯里、在厕所里\n"
      "事件（1-4）：吃饭、遛狗、飞翔、看书\n"
      "请根据提示输入对应的数字")
def check_a():
    global a
    while True:
        a = int(input("请输入对应的时间，数字1-3："))
        if a>3 or a<1:
            print("输入错误，请重新输入！")
        else:
            break
def check_b():
    global b
    while True:
        b = int(input("请输入对应的人物，数字1-4："))
        if b>4 or b<1:
            print("输入错误，请重新输入！")
        else:
            break
def check_c():
    global c
    while True:
        c = int(input("请输入对应的地点，数字1-4："))
        if c>4 or c<1:
            print("输入错误，请重新输入！")
        else:
            break
def check_d():
    global d
    while True:
        d = int(input("请输入对应的事件，数字1-4："))
        if d>4 or d<1:
            print("输入错误，请重新输入！")
        else:
            break
check_a()
check_b()
check_c()
check_d()
print("接下来请耐心等待，故事即将产生。")
time=["早上","中午","半夜"]
person=["小明","小李","小白","小黑"]
place=["在房上","在地下","在电梯里","在厕所里"]
thing=["吃饭","遛狗","飞翔","看书"]
story=time[a-1]+person[b-1]+place[c-1]+thing[d-1]
print(story)
f=open("story.txt","a")
f.write(story)
f.close()

