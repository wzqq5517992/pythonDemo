import json
file = open("时间.txt", "r")
js = file.read()
time = json.loads(js)
file.close()
file = open("人物.txt", "r")
js = file.read()
man = json.loads(js)
file.close()
file = open("地点.txt", "r")
js = file.read()
place = json.loads(js)
file.close()
file = open("事件.txt", "r")
js = file.read()
incident = json.loads(js)
file.close()


def story():
    time1 = input(print("请输入时间："))
    man1 = input(print("请输入人物："))
    place1 = input(print("请输入地点："))
    incident1 = input(print("请输入事件："))
    story1 = time[time1] + man[man1] + place[place1] + incident[incident1]
    print("请看小故事：%s" % story1)


while True:
    judge = input("请输入（看故事请输入1，写入新故事请输入2，退出请输入任意健）：")
    if judge == "1":
        story()
    elif judge == "2":
        judge1 = int(input(print("请输入(写入时间输入1，写入人物输入2，写入地点输入3，写入事件输入4)：")))
        if judge1 == 1:
            print("目前有%d个内容，键值请从%d以后输入！" % (len(time), len(time)))
            key = int(input("请输入键值："))
            value = input("请输入值：")
            time2 = {key: value}
            time.update(time2)
            file = open("时间.txt", "w")
            js = json.dumps(time)
            file.write(js)
            file.close()
            print("写入成功！")
        elif judge1 == 2:
            print("目前有%d个内容，键值请从%d以后输入！" % (len(man), len(man)))
            key = int(input("请输入键值："))
            value = input("请输入值：")
            man2 = {key: value}
            man.update(man2)
            file = open("人物.txt", "w")
            js = json.dumps(man)
            file.write(js)
            file.close()
            print("写入成功！")
        elif judge1 == 3:
            print("目前有%d个内容，键值请从%d以后输入！" % (len(place), len(place)))
            key = int(input("请输入键值："))
            value = input("请输入值：")
            place2 = {key: value}
            place.update(place2)
            file = open("地点.txt", "w")
            js = json.dumps(place)
            file.write(js)
            file.close()
            print("写入成功！")
        elif judge1 == 4:
            print("目前有%d个内容，键值请从%d以后输入！" % (len(incident), len(incident)))
            key = int(input("请输入键值："))
            value = input("请输入值：")
            incident2 = {key: value}
            incident.update(incident2)
            file = open("事件.txt", "w")
            js = json.dumps(incident)
            file.write(js)
            file.close()
            print("写入成功！")
        else:
            print("请输入正确的内容！")
    else:
        print("欢迎再次使用！")
        break
