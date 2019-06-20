# 需要注意的是 requests  而不是request  他们区别多一个s和少一个s区别

# requests和我们之前使用的pyecharts是一样的，需要我们来进行安装的操作
# mac  pip3 install requests
# windows pip install requests

# 导入模块
import requests

response = requests.get("http://www.baidu.com")
response.encoding = 'utf-8'
print(response.text)  # 状态码 200
print(response.content)
# content和text有什么区别
print(type(response.text))
print(type(response.content))
