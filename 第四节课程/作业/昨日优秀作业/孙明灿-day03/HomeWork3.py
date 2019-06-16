#encoding:utf8
#文字编故事
import random

while True:
    when=["早上","中午","半夜"]
    who=["小明","小李","小白","小黑"]
    where=["在房上","在地下","在电梯里","在厕所里"]
    what=["吃饭","遛狗","飞翔","看书"]
    print("请输入故事编号：(1111-3444之间的任意数，0表示退出)")
    n=int(input())
    if 1111<=n<=3444 :
        a=int(n/1000)#千位数字
        b=int(n/100%10)#百位数字
        c=int(n/10%10)#十位数字
        d=int(n%10)#个位数字
        #数组下标从0开始，输入的数比下标大1，故需减去1
        time=when[a-1]+who[b-1]+where[c-1]+what[d-1]
        print(time)

        # 创建文件并写入文件
        file = open('cxk.txt', 'a+',encoding="utf8")
        file.write(time+"\n")#换行
        file.close()
    elif n == 0 :
        print("退出成功！")
        break
    else :
        print("输入错误，请重新输入！")
