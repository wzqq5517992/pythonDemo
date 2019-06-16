#coding:utf8
import requests
headers={
    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"
}
rs=requests.get('https://www.douyin.com/share/user/63692754272/',headers=headers)
rs.encoding='utf-8'
print(rs.text)

import re
dytk=re.search("dytk: '(.*?)'",rs.text).group(1)
print(dytk)


"""
user_id: 63692754272
count: 21
max_cursor: 0
aid: 1128
dytk: 102f4e17eb7a0ff33c5500bb284aaeda
"""

#组装数据
params={
    'user_id':'63692754272',
    'count':'35',
    'max_cursor':'0',
    'aid':'1128',
    'dytk':dytk
}
aweme_list=[]

while True:
    url='https://www.douyin.com/aweme/v1/aweme/favorite/'
    jsonobj=requests.get(url,params=params,headers=headers).json()
    print(jsonobj)

    aweme_list=jsonobj.get('aweme_list')
    if len(aweme_list) !=0:
        break

print("数据已经有了")
print(aweme_list)

for item in aweme_list:
    video_uri=item['video']['play_addr']['uri']
    #拼接url
    video='https://aweme.snssdk.com/aweme/v1/playwm/?video_id='+video_uri
    print(video)

    title=item['share_info']['share_desc']
    mp4=requests.get(video,headers=headers,stream=True).content
    open('./video/'+title+'.mp4','wb').write(mp4)

print("下载完成")



