import json
import os

m_dataFilePath = "dataBase.json"
DB_KEY_Time = "时间"
DB_KEY_Person = "人物"
DB_Key_Place = "地点"
DB_Key_Event = "事件"


def get_input_number():
    """获取玩家输入的数字，并检查"""
    cn = 0
    numbs = []
    while cn < 4:
        print("请输入第%d个数字：" % (cn + 1))
        num = input()
        if len(num) > 3:
            print("别整那么大的数据啊！")
            continue
        mark = False  # 是否需要再循环
        for i in num:
            # if ord(i) < ord('0') or ord(i) > ord('9'):
            if i < '0' or i > '9':
                print("不要调皮，只能输数字！")
                mark = True
                break
        if mark:
            continue
        numbs.append(num)
        cn += 1
    return numbs  # 返回输入的内容


def show_dict(dic):
    print("当前数据库内容如下：")
    for key in dic:
        print("%s   %s" % (key, dic[key]))


def add_data():
    dic = load_Data()
    print("请根据提示添加项,或输入“完成”结束")
    wrin = False
    while True:
        show_dict(dic)
        if wrin:  # 最后写入
            f = open(m_dataFilePath, 'w')
            f.write(json.dumps(dic))
            f.close()
            return
        inn = input("输入对应的序号(1.时间；2.人物；3.地点；4.事件)，或输入“完成”结束：\n")
        if inn == "完成":
            wrin = True
            continue
        if inn < '0' or inn > '4':
            print("没有该项，请重新输入：")
            continue

        intxt = input("请输入要添加的内容,或输入“完成”结束：\n")
        if intxt == "完成":
            wrin = True
            continue
        elif intxt.strip() == "":
            print("输入不能为空或全空格！请重新输入！")
            continue

        if inn == '1':
            dic[DB_KEY_Time].append(intxt)
        elif inn == '2':
            dic[DB_KEY_Person].append(intxt)
        elif inn == '3':
            dic[DB_Key_Place].append(intxt)
        elif inn == '4':
            dic[DB_Key_Event].append(intxt)


def load_Data():
    """加载数据文件"""
    if os.path.exists(m_dataFilePath):  # 读取内容
        dbf = open(m_dataFilePath, 'r')
        txt = dbf.read()
        dbf.close()
        dict1 = json.loads(txt)
        return dict1
    else:  # 写入内容
        dbf = open(m_dataFilePath, 'w')
        dict2 = {DB_KEY_Time: ['早上', '中午', '半夜'],
                 DB_KEY_Person: ['小明', '小李', '小白', '小黑'],
                 DB_Key_Place: ['在房上', '在地下', '在电梯里', '在厕所里'],
                 DB_Key_Event: ['吃饭', '遛狗', '飞翔', '看书']}
        txt = json.dumps(dict2)
        dbf.write(txt)
        dbf.close()
        return dict2


def get_txt(dic, DB_KEY_Type, number):
    """
    获取字典中的值
    :param dic: 字典
    :param DB_KEY_Type:字典中的Key
    :param number:  计算字典中要取的值value的下标
    :return: 取出来的文本
    """
    alist = dic[DB_KEY_Type]
    length = len(alist)
    result = alist[number % length]  # 取余数
    # print(result)
    return result


def get_result(num):
    """
    根据输入的参数计算出文本
    :param num: 玩家输入的指令 (str)
    :return: 生成的结果文本串
    """
    dic = load_Data()
    timeTxt = get_txt(dic, DB_KEY_Time, int(num[0]))
    personTxt = get_txt(dic, DB_KEY_Person, int(num[1]))
    placeTxt = get_txt(dic, DB_Key_Place, int(num[2]))
    eventTxt = get_txt(dic, DB_Key_Event, int(num[3]))
    result = timeTxt + personTxt + placeTxt + eventTxt
    return result


print("==================【游戏说明】==================")
print("输入随机数字，系统将根据你输入的数字生成一段文字")
print("=========【游戏开始】请根据提示进行操作=========")
while True:
    ins = input("输入对应序号选择操作(1.开始游戏； 2.添加游戏内容； 3.退出):\n")
    if ins < '1' or ins > '3':
        print("【无效操作】")
        continue
    elif ins == '1':
        innum = get_input_number()
        story = get_result(innum)
        print(story)
    elif ins == '2':
        add_data()
    else:
        exit()
