#coding:utf8
#读取到a.txt
f=open('a.txt')
content=f.read()
f.close()
print(content)
print(type(content))#str->dict
import json
dict1=json.loads(content)
print(type(dict1))
print(dict1['data'][0]['emphasized']['title'])

f=open('b.txt','w')
f.write(dict1['data'][0]['emphasized']['title'])
f.close()




