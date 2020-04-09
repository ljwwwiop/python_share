# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class Doubantop250Item(scrapy.Item):
    title = scrapy.Field()  # 电影名字
    star = scrapy.Field()  # 电影评分
    quote = scrapy.Field()  # 脍炙人口的一句话
    movieInfo = scrapy.Field()  # 电影的描述信息，包括导演、主演、电影类型
    pass












