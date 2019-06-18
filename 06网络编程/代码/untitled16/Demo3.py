# coding:utf8
# https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E7%BE%8E%E5%A5%B3&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1560862258753

# 参数中是必须要用的
# https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E7%BE%8E%E5%A5%B3&count=20
# 修改过的
# https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=20&format=json&keyword=%E7%BE%8E%E5%A5%B3&autoload=true&count=20&en_qc=1&cur_tab=2&from=video&pd=video


# 1、请求地址  导入requests
# 2、获得内容  查看是否是乱码
# 3、解析数据  json
# 4、导入json模块
# import requests
# headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
#          }
# rs=requests.get("https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=美女&autoload=true&count=20&en_qc=1&cur_tab=2&from=video&pd=video",headers=headers)
# print(rs.text)

# 以上内容是被反扒了，对方网站规则改了

# 经过分析
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}

cookies = {
    "Cookie": "csrftoken=6e6ec19ead9f3be2060ef987ccf4a350;ga=GA1.2.2051716377.1560517828; tt_webid=6702372980922877448; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6702372980922877448; UM_distinctid=16b561ca2b699-032ab5101f38c4-37617e03-fa000-16b561ca2b8161; s_v_web_id=1d018a09e18eeaa9cc606986b6b66dfc; CNZZDATA1259612802=585423789-1560512688-https%253A%252F%252Fwww.baidu.com%252F%7C1560858289; __tasessionId=kjgi5ecvw1560861639434"
          }
for x in range(0, 1000, 20):
    url = "https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=%d&format=json&keyword=美女&autoload=true&count=20&en_qc=1&cur_tab=2&from=video&pd=video" % x
    rs = requests.get(url, headers=headers, cookies=cookies)
    print(rs.text)
    # 为什么可以删除cookie其中报错那段内容，我猜的
    # 爬虫很多是需要自己猜  比如字段名称  cookie的内容
    data = rs.json()['data']
    if data == None:
        break
    for i in data[0]["image_list"]:
        name = i['url'].split("/")[-1]
        urlstr = i['url']
        # 旧版是list->large  新版是large->list
        urlstr = urlstr.replace('large', 'list')
        rs = requests.get(urlstr, cookies=cookies)
        f = open('photo/' + name + '.jpg', 'wb')
        f.write(rs.content)
        f.close()
