import json
from typing import Dict, List

# 保存数据到本地
def saveData():
    dataJson = {"时间":{"1":"早上","2":"中午","3":"半夜"},
                "人物":{"1":"小明","2":"小李","3":"小白","4":"小黑"},
                "地点":{"1":"在房上","2":"在地下","3":"在地铁里","4":"在厕所里"},
                "事件":{"1":"吃饭","2":"遛狗","3":"飞翔","4":"看书"}}

    fp = open('dataJson.json','w')
    dataStr = json.dump(dataJson,fp)

    # print(type(dataStr))

# 从本地读取数据
def readData():
    fp = open('dataJson.json','r')
    dataDic = json.load(fp)
    # print(type(dataDic))
    # print(dataDic)
    return dataDic

# 保存文章到本地
def saveArticle(fileName, article):
    fil = open(fileName,'a')
    fil.write(article + "\n")
    fil.close()

# 这个是编辑文章的入口
def editArticle():

    print("故事生成器,请按照提示输入相应的数字:")
    article = "您生成的故事:"
    count = 1
    while True:
        tupFlag = chooseCondition(count)

        # 只有当输入无误的时候才拼接
        if tupFlag[0]:
           count += 1
           article = article + tupFlag[1]
        else:
            print(tupFlag[1])

        if count < 5 :
            continue
        else:
            print(article)
            # 保存文章到本地
            saveArticle("article.text",article)
            break


    isNeedCreatArticle()


# 是否需要重新输入文章
def isNeedCreatArticle():
    flag = input("是否需要继续生成新的故事,请输入 y 或 n:")
    if flag == 'y':
        editArticle()
    elif flag == 'n':
        print("再见!~")
        exit()
    else:
        print("输入有误,结束")
        exit()

# 选择的条件类型
def chooseCondition(count):

    key = ""
    if count == 1:
        key = "时间"
    elif count == 2:
        key = "人物"
    elif count == 3:
        key = "地点"
    else:
        key = "事件"

    # 读取数据
    data = readData()
    dic = {}
    for condition in sorted(data.keys()):
        if key == condition:
            dic = data[condition]

    visibleStr = ""
    strBlist  = []
    for num in range(len(dic.keys())):
        if num != len(dic.keys()) - 1:
            visibleStr = visibleStr + "{}:{}\t".format(dic[str(num + 1)],num+1)
        else:
            visibleStr = visibleStr + "{}:{}".format(dic[str(num + 1)], num + 1)

    chooseNum = input("请选择故事的%s:\"%s\",请输入:" % (key,visibleStr))

    # 定义元组返回数据
    flagTup = ()

    # 判断避免输入错误
    if chooseNum.strip().isdigit() and ( 0 < int(chooseNum.strip()) <= len(dic.keys())) :
        return (True , dic[chooseNum])
    else:
        return (False, "您输入有误请重新输入")

# 先把文章的类型数据存储到本地
saveData()
# 编辑文章
editArticle()