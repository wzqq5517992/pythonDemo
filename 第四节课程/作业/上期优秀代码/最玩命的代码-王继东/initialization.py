#coding:utf8
import json

time_dict = {'1':'早上', '2':'中午', '3':'傍晚', '4':'午夜'}

name_dict = {'1':'蔡徐坤', '2':'吴亦凡', '3':'吴京', '4':'董明珠'}

place_dict = {'1':'在桌子底下', '2':'在试衣间里', '3':'在马桶上', '4':'在河边'}

event_dict = {'1':'吃鸡腿', '2':'做寿司', '3':'流鼻血', '4':'吃手抓饭'}

def Initialize_tnpe():
    f=open("time.txt",'w')
    time_str = json.dumps(time_dict)
    f.write(time_str)
    f.close()

    f=open("name.txt",'w')
    name_str = json.dumps(name_dict)
    f.write(name_str)
    f.close()

    f=open("place.txt",'w')
    place_str = json.dumps(place_dict)
    f.write(place_str)
    f.close()

    f=open("event.txt",'w')
    event_str = json.dumps(event_dict)
    f.write(event_str)
    f.close()

def Initialize_story():
    f=open("story.txt",'w')
    story_str = "Story History"
    f.write(story_str)
    f.close()