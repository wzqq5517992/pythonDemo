from generate_function import *
from maintain_function import *


def main_function():
    inputType = input("输入1:生成故事,2:维护故事库")
    if inputType == '1':
        genStory()
    elif inputType == '2':
        maintainStory()


def genStory():
    while True:
        inputStr = input("请输入4个数字生成故事,退出请输quit")
        try:
            inputNum = int(inputStr)
            if len(inputStr) != 4:
                print("输入数字位数不足，请重新输入！")
                continue
            story = getStory(inputStr)
            print(story)
        except ValueError:
            if inputStr == 'quit':
                break
            else:
                print('您的输入不合法，请重新输入！')
                continue


def maintainStory():
    while True:
        inputType = input("请选择想要维护的字段: 1:时间,2:人物,3:地点4:事件,输入quit退出")
        if inputType != '1' and inputType != '2' and inputType != '3' and inputType != '4' and inputType != 'quit':
            print("输入有误!!")
            continue
        if inputType == 'quit':
            break
        while True:
            inputStr = input("请输入要维护字段,返回上层输入quit")
            if inputStr == 'quit':
                break
            else:
                maintainColumn(inputType, inputStr)
                print("维护成功")

main_function()