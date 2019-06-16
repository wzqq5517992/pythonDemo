#coding=utf-8
import _myutils, _mydb
print("*****************************************")
print("******* 请选择 1、2、3、4、5 **************")
print("*****************************************")
_fileName = "玄记.md"
_indexName = 'index.txt'
encode = "utf-8"
line = _myutils._read(_indexName, 'r', encode)[-1]
while("张老师牌老司机福利"):
    sj = input("时间>>> ")
    rw = input("人物>>> ")
    dd = input("地点>>> ")
    et = input("事件>>> ")
    # 判断省略
    text = _mydb.鸡森["时间"][int(sj) - 1] + _mydb.鸡森["人物"][int(rw) - 1] + _mydb.鸡森["地点"][int(dd) - 1] + _mydb.鸡森["事件"][int(et) - 1]
    _myutils._write( _fileName, "a", "\n >" + str(line) + "、" +  text + "\n ------------------------", encode)
    line = int(line) + 1
    _myutils._write(_indexName, "a", str(line), encode)
    rd = _myutils._read(_fileName, 'r', encode)
    print(rd)