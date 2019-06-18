#coding:utf8
import hashlib


def makeMD5(str1):
    h1=hashlib.md5()
    h1.update(str1.encode(encoding='utf8'))
    print("md5"+str1)
    print("md5后"+h1.hexdigest())
makeMD5("hahaha")