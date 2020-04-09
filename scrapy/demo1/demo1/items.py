# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Demo1Item(scrapy.Item):
    # define the fields for your item here like:
    # 电影名字
    name = scrapy.Field()

    #简介
    movies = scrapy.Field()
    #海报
    image = scrapy.Field()
    #故事简介
    story = scrapy.Field()
    #download
    download = scrapy.Field()


