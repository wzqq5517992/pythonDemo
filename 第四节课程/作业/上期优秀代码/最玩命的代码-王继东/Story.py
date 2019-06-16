#coding:utf8
from StoryFunction import *
from WriteFunction import *
from print_readme import *
from initialization import *
from StoryRecord import *
# 打印使用手册
print_readme()

while True:
    command = int(input("请输入您想做的事："))
    if command == 1 :
        time_num = str(input("请输入时间"))
        neme_num = str(input("请输入人物"))
        place_num = str(input("请输入地点"))
        event_num = str(input("请输入事件"))
        stime = Get_Time(time_num)
        name = Get_Name(neme_num)
        place = Get_Place(place_num)
        event = Get_Event(event_num)
        story =stime + name + place + event
        Story_record(story)
        print("本次您选择的故事是：" + story)
        print("本次故事已完成，请问您接下来要做什么？")
    elif command == 8 :
        break
    else:
        if command == 2 :
            time_write = input("请添加新的时间：")
            Write_Time(time_write)
        elif command == 3 :
            name_write = input("请添加新的人物：")
            Write_Name(name_write)
        elif command == 4 :
            place_write = input("请添加新的地点：")
            Write_Place(place_write)
        elif command == 5 :
            event_write = input("请添加新的事件：")
            Write_Event(event_write)
        elif command == 6 :
            Initialize_tnpe()
        elif command == 7:
            Initialize_story()
        elif command == 9 :
            print_readme()
        else:
            print("无法识别您的指令，请重新输入")


