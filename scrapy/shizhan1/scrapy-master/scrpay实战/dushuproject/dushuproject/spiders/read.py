# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from dushuproject.items import DushuprojectItem


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1163.html']

    # 如果不加follow参数，follow是有默认值的
    # 如果callback处理，follow就是False
    # 如果没有callback处理，follow就是true

    rules = (
        Rule(LinkExtractor(allow=r'/book/1163_\d+\.html'), callback='parse_item', follow=False),
    )

    # def parse(self, response):
    #     pass

    def parse_item(self, response):
        # 首先查找到所有的书籍
        book_list = response.xpath('//div[@class="bookslist"]/ul/li')
#         遍历所有的书籍，获取每本书详细的内容
        for book in book_list:
            item = DushuprojectItem()
            item['image_url'] = book.xpath('./div[@class="book-info"]/div/a/img/@data-original').extract_first()
            item['book_name'] = book.xpath('./div[@class="book-info"]/h3/a/text()').extract_first()
            item['author'] = book.xpath('./div[@class="book-info"]/p/a/text()').extract_first()
            item['info'] = book.xpath('./div[@class="book-info"]/p[@class="disc eps"]/text()').extract_first()

            yield item


