# -*- coding: utf-8 -*-
import scrapy

from mmonly.items import TagItem, MmonlyItem


class Mmonly1Spider(scrapy.Spider):
    name = 'mmonly1'
    allowed_domains = ['mmonly.cc']
    start_urls = ['http://www.mmonly.cc/tag/']

    def parse(self, response):
        #print(response.text)
        #使用xpath
        category=response.xpath("//div[@class='Clbc_Game TagBox']//h2/text()").extract()
        #print(category)
        #获得其中的子标签
        childtag=response.xpath("//div[@class='TagList']")
        # index = 0
        # for item in childtag:
        #     index += 1
        for index,item in enumerate(childtag):
            #遍历子标签
            childtagel =item.xpath('a')
            for atag in childtagel:
                #获得其中的小标
                tag=atag.xpath('@href').extract_first()[1:-1].split('/')[1]
                title=atag.xpath('text()').extract_first()
                #print(tag,title)
                #建立模型
                tagitem=TagItem()
                tagitem['tag']=tag
                tagitem['title']=title

                yield tagitem

                item1=MmonlyItem()
                item1['name']='zhangcheng'
                yield item1






