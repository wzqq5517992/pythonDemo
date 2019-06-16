#coding:utf8
import json

def Get_Time(time):
    f = open("time.txt", 'r')
    time_strget = f.read()
    time_dictget = json.loads(time_strget)
    # print(time_dictget)
    return time_dictget[time]
    f.close()

def Get_Name(name):
    f = open("name.txt", 'r')
    name_strget = f.read()
    name_dictget = json.loads(name_strget)
    # print(name_dictget)
    return name_dictget[name]
    f.close()

def Get_Place(place):
    f = open("place.txt", 'r')
    place_strget = f.read()
    place_dictget = json.loads(place_strget)
    # print(place_dictget)
    return place_dictget[place]
    f.close()

def Get_Event(event):
    f = open("event.txt", 'r')
    event_strget = f.read()
    event_dictget = json.loads(event_strget)
    # print(event_dictget)
    return event_dictget[event]
    f.close()
