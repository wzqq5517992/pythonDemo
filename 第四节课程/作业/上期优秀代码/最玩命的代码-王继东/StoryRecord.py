#coding:utf8
import json
def Story_record(sto):
    w = open("story.txt", 'a')
    sto_rec = "1." + sto
    w.write(sto_rec)
    w.close()