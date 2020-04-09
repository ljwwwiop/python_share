# -*- coding: utf-8 -*-
from scrapy import Spider, Request
import json
from zh.items import UserItem
import time

users = []
followers_url = "https://www.zhihu.com/api/v4/members/"
need_url = "/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20"


class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    start_user = 'lu-yi-90-79'

    user_url = 'https://www.zhihu.com/api/v4/members/{user}'

    follower_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follower_query = 'data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'

    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follows_query = 'data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'

    def start_requests(self):
        yield Request(self.user_url.format(user=self.start_user), callback=self.parse_user)
        yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, offset=0, limit=20),
                      callback=self.parse_follows)
        yield Request(self.follower_url.format(user=self.start_user, include=self.follower_query, offset=0, limit=20),
                      callback=self.parse_follower)

    def parse_user(self, response):
        result = json.loads(response.text)
        # print(result)
        item = UserItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item

        time.sleep(1)
        yield Request(
            self.follows_url.format(user=result.get('url_token'), include=self.follows_query, limit=20, offset=0),
            self.parse_follows)

        time.sleep(1)
        yield Request(
            self.follower_url.format(user=result.get('url_token'), include=self.follower_query, limit=20,
                                     offset=0),
            self.parse_follower)


    def parse_follows(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                print(result.get("name"))
                time.sleep(0.5)
                yield Request(self.user_url.format(user=result.get('url_token')), self.parse_user)
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            print("实现了 追随者的下一页")

            yield Request(next_page, self.parse_follows)

    def parse_follower(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                time.sleep(0.5)
                print(result.get("name"))
                yield Request(self.user_url.format(user=result.get('url_token')), self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            print('实现了下一个url:',results.get('paging').get('totals'))

            yield Request(next_page, self.parse_follower)



