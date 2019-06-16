import random

def name(n):
    s= n[random.randrange(n.__len__())]
    return s

li =[]
i = 0
while i<10:
    i+=1
    times = ['早上','中午','半夜']
    figure =['小明','小李','小白','小黑']
    place =['在房上','在地下','在电梯里','在厕所里']
    event =['吃饭','遛狗','飞翔','看书']
    li.append(str(name(times)+name(figure)+name(place)+name(event)+'\n'))

with open("\\store.txt",'w',encoding='UTF-8') as store:
    for s in li:
        store.write(s)

with open("\\store.txt",'r',encoding='UTF-8') as s:
    for q in s:
        print(q,end='')