# -*- coding: utf-8 -*-
# import scrapy
import json

from scrapy import Spider, Request

from zhihuuser.items import UserItem


class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    start_user = 'chexiaopang'

    user_url = 'https://www.zhihu.com/api/v4/members/{user}'
    # user_query = ''

    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    follower_url = "https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}"
    follower_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    def start_requests(self):
        yield Request(self.user_url.format(user=self.start_user), callback=self.parse_user)
        yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, offset=0, limit=20),
                      callback=self.parse_follows)
        yield Request(self.follower_url.format(user=self.start_user, include=self.follower_query, offset=0, limit=20),
                      callback=self.parse_follower)

    def parse_user(self, response):
        result = json.loads(response.text)
        item = UserItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item

        yield Request(
            self.follows_url.format(user=result.get('url_token'), include=self.follows_query, limit=20, offset=0),
            self.parse_follows)

        yield Request(
            self.follower_url.format(user=result.get('url_token'), include=self.follower_query, limit=20, offset=0),
            self.parse_follower)

    def parse_follows(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token')), self.parse_user)
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_follows)

    def parse_follower(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token')), self.parse_user)
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_follower)
