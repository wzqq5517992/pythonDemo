# coding:utf8
import requests

"""头条爬虫  循环请求"""

# 反扒的处理
# cookie
# header

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
cookies = {
    "Cookie": "csrftoken=6e6ec19ead9f3be2060ef987ccf4a350; tt_webid=6703883280255632904; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6703883280255632904; UM_distinctid=16b6b11f38095-05205479d3da3e-37617e03-fa000-16b6b11f381414; s_v_web_id=1d018a09e18eeaa9cc606986b6b66dfc; CNZZDATA1259612802=127341380-1560869089-https%253A%252F%252Fwww.baidu.com%252F%7C1560944689; __tasessionId=qyspr5ckn1560945725732"}

for x in range(0, 1000, 20):

    url = "https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset={}&format=json&keyword=%E7%BE%8E%E5%A5%B3&autoload=true&count=20&en_qc=1&cur_tab=2&from=video&pd=video&timestamp=1560945746064".format(
        x)
    rs = requests.get(url, headers=headers, cookies=cookies)
    # print(rs)
    print(rs.text)

    # 自带json解析
    data = rs.json()['data']
    if data == None:
        print("数据没有了")
        break

    for i in data[0]["image_list"]:
        name = i['url'].split('/')[-1]
        urlstr = i['url']
        # 进行对图片的请求   需要携带cookie
        rs1 = requests.get(urlstr, cookies=cookies)
        print(urlstr)
        f = open('photo/' + name + '.jpg', 'wb')
        f.write(rs1.content)
        f.close()
