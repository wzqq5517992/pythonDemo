# coding:utf8
import requests

import mysql.connector as mysql

cnx = mysql.connect(user='root', password='Wzq5517992@', host='47.93.37.94', database='movie', port=3306)
# 获得游标
cursor = cnx.cursor()

rs = requests.get(
    "http://pcw-api.iqiyi.com/search/video/videolists?access_play_control_platform=14&channel_id=1&data_type=1&from=pcw_list&is_album_finished=&is_purchase=0&key=&market_release_date_level=&mode=11&pageNum=3&pageSize=58&site=iqiyi&source_type=&three_category_id=&without_qipu=1")
# 直接对他进行解析
jsonobj = rs.json()['data']['list']
# 读取jsonobj是列表
print(len(jsonobj))

# 遍历这个列表
for i in jsonobj:
    abc = i['name']
    sql_select = "select * from movie where name = '%s'" % abc
    cursor.execute(sql_select)
    # 获取查询结果
    result = cursor.fetchall()
    if len(result) == 0:
        # i是什么类型？字典类型
        print(i['name'], i['playUrl'], i['score'], i['description'], i['duration'])
        # 持久化保存 mysql
        str1 = "insert into movie (name,playUrl,score,description,duration) values('{}','{}',{},'{}','{}')".format(i['name'], i['playUrl'],
                                                                                               i['score'],
                                                                                               i['description'],
                                                                                               i['duration'])
        cursor.execute(str1)
    else:
        continue
cnx.commit()
