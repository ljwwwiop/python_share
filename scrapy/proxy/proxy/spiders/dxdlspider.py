# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem


class DxdlspiderSpider(scrapy.Spider):
    name = 'dxdlspider'
    allowed_domains = ['kuaidaili.com']
    start_urls = []

    for i in range(1,15):
        start_urls.append('http://www.kuaidaili.com/free/inha/' + str(i) + '/')

    def parse(self, response):
        # 实例化
        item = ProxyItem()
        main = response.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
        for li in main:
            # Ip
            ip = li.xpath('td/text()').extract()[0]
            # 端口号
            port = li.xpath('td/text()').extract()[1]
            # 连接后传给Item
            item['addr'] = ip + ':'+port
            yield item


