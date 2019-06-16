#coding:utf8
#json格式  只有2种格式  列表、字典<->str
import json
t=json.dumps({"a":1,"b":2})
print(t)
print(type(t))

#t转换为字典
jsonobj=json.loads(t)
print(jsonobj)
print(type(jsonobj))

