def printInfo():
    list = [['早晨', '中午', '晚上', '半夜'], ['小名', '小兰', '小白', '小黑'], ['在放上', '在厨房', '在电梯里', '咋厕所里'],['吃饭', '飞翔', '遛狗', '看书']]
    num = input()
    i = 0
    content = ""
    for n in num:
        content = content + list[i][int(n)]
        i = i + 1
    with open("test1.txt","w") as f:
        f.write(content)

