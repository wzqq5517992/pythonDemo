#请求地址
#https://www.toutiao.com/search/?keyword=美女

#1、导入头文件
#2、get
#3、打印内容

import requests

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}


rs=requests.get("https://www.toutiao.com/search/?keyword=美女" , headers=headers)


print(rs.text)


#为什么要带上header
#主要用于模拟浏览器  欺骗服务器，来获得和浏览器一致的内容