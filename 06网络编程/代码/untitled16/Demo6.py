#coding:utf8
import requests
from bs4 import BeautifulSoup
import os

all_url='http://www.mzitu.com/all'
Hostreferer={
    "User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Referer":"http://www.mzitu.com"
}



#请求数据
start_html=requests.get(all_url,headers=Hostreferer)
# print(start_html.text)

#白天和晚上策略是不一样的，白天各种反扒
#路径
path=''
#请求开始页面
soup =BeautifulSoup(start_html.text,'html.parser')
peles=soup.find_all('p',class_='url')
for n in peles:
    #读取每一个p分组内的a标签
    aeles=n.find_all('a')
    for a in aeles:
        title =a.get_text()
        if title !='':
            print("准备爬取"+title)

        if os.path.exists(path+title.strip().replace('?','')):
            print("目录已存在")
            flag=1
        else:
            #创建目录
            os.makedirs(path+title.strip().replace('?',''))
            flag=0
        #进行请求获得最大页面
        html=requests.get(a['href'],headers=Hostreferer)
        mess=BeautifulSoup(html.text,'html.parser')
        try:
            pic_max=mess.find('div',class_='pagenavi').find_all('span')[-2]
            pic_max=pic_max.text
        except:
            continue
        if (flag==1and len(os.listdir(path+title.strip().replace('?','')))>=int(pic_max)):
            print("已经保存完毕，跳过")
            continue
        else:
            print("11111")

            for num in range(1,int(pic_max)+1):
                pic=a['href']+'/'+str(num)
                html=requests.get(pic,headers=Hostreferer)
                mess=BeautifulSoup(html.text,'html.parser')
                pic_url=mess.find('img',alt=title)
                if pic_url==None:
                    continue
                print(pic_url['src'])
                html =requests.get(pic_url['src'],headers=Hostreferer)
                #生成名称
                filename=pic_url['src'].split('/')[-1]
                f=open(title+'/'+filename,'wb')
                f.write(html.content)
                f.close()
print("完成")













