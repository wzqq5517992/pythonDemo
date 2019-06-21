import requests
import mysql.connector as mysql

cnx = mysql.connect(user='root', password='Wzq5517992@', host='47.93.37.94', database='movie', port=3306)
# 获得游标
cursor = cnx.cursor()


def reptile(page, pageSize):
    """
    爬取数据方法
    :param page:
    :param num:
    """
    num = pageSize if pageSize <= 50 else '50'  # 三元表达式
    rs = requests.get(
        "http://api.tianapi.com/huabian/?key=1771947e1e6608e48f1cd21a1021ab2e&num={}&page={}".format(num, page))
    add_list = []
    add_list.extend(rs.json()['newslist'])
    # while len(add_list) < 101:
    #     page += page + 1
    #     rst = requests.get(
    #         "http://api.tianapi.com/huabian/?key=1771947e1e6608e48f1cd21a1021ab2e&num={}&page={}".format(num, page))
    #     add_list.extend(rst.json()['newslist'])

    return add_list


def query_database_title(dict):
    """
     查询数据库对应的记录
    :rtype: object
    """
    sql_select = "select * from Entertainment where title='%s'" % dict['title']
    cursor.execute(sql_select)
    # 获取查询结果
    return len(cursor.fetchall())


def insert_database(resource_list):
    """
    批量插入数据库记录
    :rtype: object
    """
    total = 0
    for i in resource_list:
        if query_database_title(i) == 0:
            print(i['title'], i['picUrl'], i['url'], i['description'], i['ctime'])
            # 持久化保存 mysql
            str1 = "insert into Entertainment (title,picUrl,url,description,ctime) values('{}','{}','{}','{}','{}')".format(
                i['title'], i['picUrl'],
                i['url'], i['description'],
                i['ctime'])
            cursor.execute(str1)
            total += 1
        else:
            print("记录已存在")
            continue

    cnx.commit()
    print("此次一共插入 %s 条记录" % str(total))


while True:
    pageNum = input("请输入你要爬取网页的页数 pageNum：")
    pageSize = input("请输入你每页要爬取得数量 pageSize：")
    if pageNum.isdecimal() and pageSize.isdecimal():
        resource_list = reptile(int(pageNum), int(pageSize))
        print(len(resource_list))
        insert_database(resource_list)
        end = int(input("数据操作已结束，是否继续(YES:1,NO:2):"))
        if end == 1:
            continue
        else:
            break
    else:
        print("你输入的内容不是数字， 请重新输入")
