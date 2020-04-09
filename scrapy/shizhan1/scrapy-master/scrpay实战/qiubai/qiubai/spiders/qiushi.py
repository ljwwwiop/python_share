# -*- coding: utf-8 -*-
import scrapy


class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    # parse函数就是文件解析函数，response就是响应对象
    def parse(self, response):
        div_list = response.xpath('//div[starts-with(@id,"qiushi_tag_")]')
        items = []
        for div in div_list:
            # 获取图像链接  要先通过extract转化为Unicode字符串类型，在获取里面的指定内容
            item = {}
            image_url = div.xpath('./div[@class="author clearfix"]//img/@src').extract()[0]
            name_url = div.xpath('./div[@class="author clearfix"]//img/@alt').extract()[0]
            age_url = div.xpath('./div[@class="author clearfix"]/div/text()').extract_first()
            content = div.xpath('./a/div[@class="content"]/span/text()').extract()[0]
            hh_count = div.xpath('./div[@class="stats"]/span/i[@class="number"]/text()').extract()[0]
            item = {
                'image_url':image_url,
                'name':name_url,
                'age':age_url,
                'content':content,
                'hh_count':hh_count,
            }
            # 将数据保存到列表中
            items.append(item)

        return items