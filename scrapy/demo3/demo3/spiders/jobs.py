# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

# yield协程原理
#类型
types = ['major','finance','ent']

class NewsSpider(scrapy.Spider):
    name = 'jobs'
    #这个域名下得才能爬取  可以添加多个域名
    #allowed 限定域名范围
    allowed_domains = ['qq.com']
    # 如果没有start_requests 爬虫从这第一个开始
    start_urls = ['https://news.qq.com/']


    def parse(self, response):
        if response.url == 'https://news.qq.com/':
            for type in types:
                for href in response.xpath('//div[@class="item {0}"]//a[@class="linkto"]/@href'.format(type)).extract():
                    yield Request(href)
        else:

            #print(response.url)
            title = response.xpath('//div[@class="qq_conent clearfix"]//h1/text()').extract_first()
            contents = response.xpath('//div[@class="content-article"]/p[@class="one-p"]/text()').extract()
            img = response.xpath('//img[@class="content-picture"]/@src').extract()
            if title:
                # print(title)
                # print(contents)
                # print(img)

                yield {
                    'source':response.url +'\n' ,
                    'title':title + '\n',
                    'content':contents
                }
