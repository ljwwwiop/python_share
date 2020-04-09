# -*- coding: utf-8 -*-
import scrapy


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    start_urls = ['http://weibo.cn/']

    def parse(self, response):
        pass
