import random

time = ['早上', '中午', '晚上', '半夜']
person = ['小明', '小红', '小刚', '小杨']
place = ["在马桶上", '在地下', '在电梯里', '在马路上']
doing = ['吃饭', '遛狗', '运动', '看书']

def getword(words):
    return random.choice(words)

for i in range(10):
    story = getword(time) + getword(person) + getword(place) + getword(doing)
    print(story)

