# -*- coding: utf-8 -*-
import scrapy
from demo4.items import Demo4Item
from scrapy.http import Request


class DoubanSpider(scrapy.Spider):

    name = 'douban'
    #  allowed_domains = ['www.douban.com']   翻页后超出范围我操
    start_urls = ["https://movie.douban.com/top250"]


    def parse(self, response):
        item = Demo4Item()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item['movie_name'] = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['score_num'] = movie.xpath('.//div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]

            yield item
            print(item)
            #// *[ @ id = "content"] / div / div[1] / ol / li[1] / div / div[2] / div[2] / p[1] / text()[2]
        next_url = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250'+next_url[0]
            #print(next_url)
            yield scrapy.http.Request(next_url,callback=self.parse)


# //*[@id="content"]/div/div[1]/div[2]/a[1]