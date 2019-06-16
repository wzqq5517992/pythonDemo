print("抽签游戏马上要开始喽，请大家积极参与！")
while True:
    time_num = int(input("1.你现在是否要随机生成时间(YES:1,NO:2):"))
    time_one = ["情人节", "今天", "端午节", "清明节", "前几天", "除夕夜里", "劳动节", "国庆节"]
    time_two = ["早上", "中午", "晚上", "半夜"]
    if time_num == 2:
        print("你选择了否 游戏结束了！")
        break

    place_num = int(input("2.你现在是否要随机生成地点(YES:1,NO:2):"))
    place = ["电梯里", "厕所的马桶盖上", "小树林", "荒地上"]
    if place_num == 2:
        print("你选择了否 游戏结束了！")
        break
    person_num = int(input("3.你现在是否要随机选择任务(YES:1,NO:2):"))
    person = ["小庞", "小宋", "小李", "小常", "小王"]
    if person_num == 2:
        print("你选择了否 游戏结束了！")
        break
    event_num = int(input("4.你现在是否要随机选择事件(YES:1,NO:2):"))
    event = ["吃翔", "放屁", "看书", "遛狗", "谈恋爱"]
    if event_num == 2:
        print("你选择了否 游戏结束了！")
        break
    if time_num == 1 and place_num == 1 and person_num == 1 and event_num == 1:
        import random

        random.seed()
        print("************************")
        print(random.choice(time_one) + random.choice(time_two)
              + random.choice(person) + "在" + random.choice(place)
              + random.choice(event))
        print("************************")
        flag = int(input("游戏结束了 是否要再来一局呢(YES:1,NO:2):"))
        if flag != 1:
            break
    else:
        print("你选择的有问题哦，重新选择把")
        continue
