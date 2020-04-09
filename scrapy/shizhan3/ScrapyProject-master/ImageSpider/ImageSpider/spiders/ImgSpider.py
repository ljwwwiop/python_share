# -*- coding: utf-8 -*-
"""
功能：本项目主要演示Scrapy下载图片；
运行环境：win7 64 + python3.6 + scrapy1.4 +  mongodb3.4 + pymongo-3.6.0
运行方式：进入ImageSpider目录（scrapy.cfg所在目录)输入：

scrapy crawl ImgSpider

"""

import scrapy
from ImageSpider.items import ImagespiderItem


class ImgspiderSpider(scrapy.Spider):
    name = 'ImgSpider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        # 实例化item
        item = ImagespiderItem()
        # 注意imgurls是一个集合也就是多张图片
        imgurls = response.css(".post img::attr(src)").extract()
        item['imgurl'] = imgurls
        yield item