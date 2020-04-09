# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class ZhihuuserPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):
    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url=crawler.settings.get('MONGO_URL'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        # name = item.__class__.__name__
        # # 执行插入操作
        # self.db[name].insert(dict(item))
        # 执行更新操作  true如果查到了就更新，否则就插入  去重操作
        self.db['user'].update({'url_token': item['url_token']}, {'$set': item}, True)
        return item

    def close_spider(self, spoder):
        self.client.close()
