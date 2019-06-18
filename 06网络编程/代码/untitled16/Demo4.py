#coding:utf8

import requests
rs=requests.get("http://api.tianapi.com/meinv/?key=68c42f9baf78d084cfc3cc29f8c4e569&num=10")
print(rs.text)
print(rs.json()['newslist'])
for i in rs.json()['newslist']:
    print(i['picUrl'])
    rs1=requests.get(i['picUrl'])
    f=open(i['picUrl'].split('/')[-1],'wb')
    f.write(rs1.content)
    f.close()

