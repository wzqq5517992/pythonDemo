"""
时间   早上、中午、半夜
人物   小明、小李、小白、小黑
地点   在房上、在地下、在电梯里、在厕所里
事件   吃饭、遛狗、飞翔、看书
"""
import json


def  get_resource():
    """定义方法读取资源文件中数据"""
    f = open("resource.txt" , "r" , encoding="UTF-8")
    resource = f.read()
    f.close()
    dict1 = json.loads(resource)
    return dict1

# 定义一个全局变量接收文件中读取的数据
dict1=get_resource()


def get_time(num):
    """根据输入的数字获取时间"""
    return dict1["时间"][num-1]


def get_person(num):
    """根据输入的数字获取人物"""
    return dict1["人物"][num-1]


def get_addr(num):
    """根据输入的数字获取地点"""
    return dict1["地点"][num-1]


def get_event(num):
    """根据输入的数字获取事件"""
    return dict1["事件"][num-1]


def write_file(content):
    """将结果写入文件"""
    f = open("result.txt", "a")
    f.write(content)
    f.close()





