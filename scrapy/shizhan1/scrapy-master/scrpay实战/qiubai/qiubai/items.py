# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 保存头像链接
    image_url = scrapy.Field()
    # 保存名字
    name = scrapy.Field()
    # 保存年龄
    age = scrapy.Field()
    # 保存内容
    content = scrapy.Field()
    # 好笑个数
    hh_count = scrapy.Field()