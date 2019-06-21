# coding:utf8

import requests

# rs=requests.get("http://api.tianapi.com/meinv/?key=1771947e1e6608e48f1cd21a1021ab2e&num=50")
# rs = requests.get("http://api.tianapi.com/social/?key=1771947e1e6608e48f1cd21a1021ab2e&num=50")
rs = requests.get("http://api.tianapi.com/huabian/?key=1771947e1e6608e48f1cd21a1021ab2e&num=50&page=2")
# print(rs.text)
# print(rs.json()['newslist'])
print(type(rs.json()['newslist']))
print(rs.json()['newslist'])
for i in rs.json()['newslist']:
    print(i['picUrl'])
    rs1=requests.get(i['picUrl'])
    print(i['picUrl'].split('/')[-1])
    f=open(i['picUrl'].split('/')[-1],'wb')
    f.write(rs1.content)
    f.close()
