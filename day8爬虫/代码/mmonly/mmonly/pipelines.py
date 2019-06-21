# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector as mysql

from mmonly.items import TagItem


class MmonlyPipeline(object):
    def open_spider(self,spider):
        print("固定的，管道开始时候打开")
        self.cnx = mysql.connect(user='root', password='MyNewPass4!', host='47.93.248.15', database='mmonlytest', port=20010)
        # 获得游标
        self.cursor = self.cnx.cursor()

    def process_item(self, item, spider):
        print(item)
        if isinstance(item,TagItem):

            #如果不进行返回，下一个管道，是不执行的
            str1="insert into tag values('{}','{}')".format(item['title'],item['tag'])
            self.cursor.execute(str1)
        else:
            return item
    def close_spider(self,spider):
        print("固定的，管道完成时候，关闭")
        self.cnx.commit()

class ZCPipline(object):
    def process_item(self, item, spider):
        print("自定义管道")
        if item !=None:
            print(item)

