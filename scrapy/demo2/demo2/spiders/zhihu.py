# -*- coding: utf-8 -*-
from scrapy import Spider,Request
import json
from demo2.items import UserItem

class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    start_user = 'lu-yi-90-79'

    # user 用户关注
    user_url = "https://www.zhihu.com/api/v4/members/{user}"

    # 关注人
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    # 粉丝
    follower_url = "https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}"
    follower_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    # 获取url
    def start_requests(self):
        yield Request(self.user_url.format(user=self.start_user), callback=self.parse_user)
        yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, offset=0, limit=20),
                      callback=self.parse_follows)
        yield Request(self.follower_url.format(user=self.start_user, include=self.follower_query, offset=0, limit=20),
                      callback=self.parse_follower)
    # 解析用户信息
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






















    # user_query = "locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,avatar_hue,answer_count,articles_count,pins_count,question_count,columns_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_bind_phone,is_force_renamed,is_bind_sina,is_privacy_protected,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics"
    # start_user = "excited-vczh"

    # 粉丝
    # follows_url = "https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}"
    # follows_query = "data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics"

    #获取评论和用户信息
    # def start_requests(self):
    #     # 关注url
    #     # url = 'https://www.zhihu.com/api/v4/members/he-ming-ke/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20'
    #     # 粉丝url
    #     # url = 'https://www.zhihu.com/api/v4/members/he-ming-ke/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
    #     yield Request(self.user_url.format(user=self.start_user,include=self.user_query),callback=self.parse_user)
    #     yield Request(self.follows_url.format(user=self.start_user,include=self.follows_query,offset=0,limit=20),callback=self.parse_follows)
    # #回调
    # def parse_user(self,response):
    #     result = json.loads(response.text)
    #     item = UserItem()
    #     # 这里循环判断获取的字段是否在自己定义的字段中，然后进行赋值
    #     for field in item.fields:
    #         if field in result.keys():
    #             item[field] = result.get(field)
    #
    #     # 这里在返回item的同时返回Request请求，继续递归拿关注用户信息的用户获取他们的关注列表
    #     yield item
    #
    # def parse_follows(self,response):
    #     results = json.loads(response.text)
    #
    #     if 'data' in results.keys():
    #         for result in results.get('data'):
    #             yield Request(self.user_url.format(user=result.get("url_token"), include=self.user_query),callback=self.parse_user)
    #
    #     if 'page' in results.keys() and results.get('is_end')  == False:
    #         next_page = results.get('paging').get('next')
    #         yield Request(next_page,self.parse_follows)
            # Request 之后回调

    # def parse_follow(self,response):
    #     print(response.text)