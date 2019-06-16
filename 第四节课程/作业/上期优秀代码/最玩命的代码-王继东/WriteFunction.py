#coding:utf8
import json
def Write_Time(time_insert):
    f = open("time.txt", 'r')
    time_strget = f.read()
    time_dictget = json.loads(time_strget)
    f.close()
    length = len(time_dictget)
    # print(length)
    w = open("time.txt", 'w')
    time_num = str(length + 1)
    time_dictget[time_num] = time_insert
    time_str = json.dumps(time_dictget)
    w.write(time_str)
    print("%s添加成功，编号为%s"%(time_insert,time_num))
    print("如果需要再次查看食用手册，请输入‘8’")
    w.close()

def Write_Name(name_insert):
    f = open("name.txt", 'r')
    name_strget = f.read()
    name_dictget = json.loads(name_strget)
    f.close()
    length = len(name_dictget)
    # print(length)
    w = open("name.txt", 'w')
    name_num = str(length + 1)
    name_dictget[name_num] = name_insert
    name_str = json.dumps(name_dictget)
    w.write(name_str)
    print("%s添加成功，编号为%s"%(name_insert,name_num))
    print("如果需要再次查看食用手册，请输入‘8’")
    w.close()

def Write_Place(place_insert):
    f = open("place.txt", 'r')
    place_strget = f.read()
    place_dictget = json.loads(place_strget)
    f.close()
    length = len(place_dictget)
    # print(length)
    w = open("place.txt", 'w')
    place_num = str(length + 1)
    place_dictget[place_num] = place_insert
    place_str = json.dumps(place_dictget)
    w.write(place_str)
    print("%s添加成功，编号为%s"%(place_insert,place_num))
    print("如果需要再次查看食用手册，请输入‘8’")
    w.close()

def Write_Event(event_insert):
    f = open("time.txt", 'r')
    event_strget = f.read()
    event_dictget = json.loads(event_strget)
    f.close()
    length = len(event_dictget)
    # print(length)
    w = open("event.txt", 'w')
    evnet_num = str(length + 1)
    event_dictget[evnet_num] = event_insert
    event_str = json.dumps(event_dictget)
    w.write(event_str)
    print("%s添加成功，编号为%s"%(event_insert,evnet_num))
    print("如果需要再次查看食用手册，请输入‘8’")
    w.close()