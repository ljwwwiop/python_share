# -*- coding: utf-8 -*-
import scrapy
from demo1.items import Demo1Item

class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        table_list = response.xpath('//div [@class="co_content8"]/ul//table')
        # 取出所有的table
        for table in table_list:
            # 创建Item对象
            item = Demo1Item()
            item['name'] = table.xpath('.//a[@class="ulink"]/text()').extract_first()
            item['movies'] = table.xpath('.//tr[last()]/td/text()').extract_first()
           # movie_url = 'http://www.ygdy8.net' + table.xpath('.//a[@class="ulink"]/@href').extract_first()
            move_url = 'http://www.ygdy8.net'+table.xpath('.//a[@class="ulink"]/@href').extract_first()

            yield scrapy.Request(url=move_url, callback=self.parse_info,meta={'item': item})

    def parse_info(self,response):
        # 传递item对象
        item = response.meta['item']
        # 进行内部解析 进入网站后解析方式
        item['image'] = response.xpath('//div[@id="Zoom"]//img[1]/@src').extract_first()
        item['download'] = response.xpath('//td[@bgcolor="#fdfddf"]/a/text()').extract_first()
        yield item

    print('OK')
