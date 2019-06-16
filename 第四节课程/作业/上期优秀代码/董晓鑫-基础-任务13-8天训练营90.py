list1 = [{1: '早上', 2: '中午', 3: '半夜'}, {1: '小明', 2: '小李', 3: '小白', 4: '小黑'}, {1: '在房上', 2: '在地下', 3: '在电梯里', 4: '在厕所里'},
         {1: '吃饭\n', 2: '遛狗\n', 3: '飞翔\n', 4: '飞翔\n'}]
while True:
    if input('是否开始游戏') == '否':
        break
    for list in list1:
        print(list)
        open("text.txt", 'a').write(list[int(input("请选择想要的故事选项"))])