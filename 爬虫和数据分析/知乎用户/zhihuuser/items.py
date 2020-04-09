# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field



class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    name = Field()
    avatar_url = Field()
    type = Field()
    url = Field()
    url_token = Field()
    user_type = Field()
    vip_info = Field()
    is_advertiser = Field()
    is_org = Field()
    headline = Field()
    badge = Field()

