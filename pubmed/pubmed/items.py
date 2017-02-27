# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AuthorItem(scrapy.Item):
    FullTextLink =scrapy.Field()     #全文链接
    TitleName = scrapy.Field()       #文章标题
    AuthorsName = scrapy.Field()     #文章作者
    Citation = scrapy.Field()        #引用
    AuthorInformation = scrapy.Field() #作者信息
    Abstract = scrapy.Field()        #摘要
    pmid = scrapy.Field()            #PMID
    AI = scrapy.Field()
    email = scrapy.Field()
