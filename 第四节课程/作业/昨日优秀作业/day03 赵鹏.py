import random
time={1:"早上",2:"中午",3:"午夜"}
people={1:"小明",2:"小李",3:"小黑",4:"小白"}
site={1:"在房上",2:"在地下",3:"在电梯里",4:"在厕所里"}
event={1:"吃饭",2:"遛狗",3:"飞翔",4:"看书"}

while True:
    try:
        a=int(input("什么时间请输入1到3之间的数字:"))
        b=int(input("哪个人请输入1到4之间的数字："))
        c=int(input("在什么地方请输入1到4之间的数字："))
        d=int(input("在干嘛请输入1到4之间的数字："))
        if 1<=a and a<4:
            n=time.get(a)
        else:
            print("什么时间错误请重新输入")
            continue
        if b>=1 and b<5:
            m=people.get(b)
        else:
            print("哪个人输入错误请重新输入")
            continue
        if c>=1 and c<5:
            p=site.get(c)
        else:
            print("在什么地方输入错误请重新输入")
            continue
        if d>=1 and d<5:
            o=event.get(d)
        else:
            print("在干嘛输入错误请重新输入")
            continue


        j=n+m+p+o
        print(j)
        f=open("joke.txt","a")
        f.write(j+"\r\n")
        f.close()
        print("任意键继续,q退出")
        Esc=input("还想在继续玩么：")
        if Esc =="q":
            break
    except :
        print("输入有误")
        continue




