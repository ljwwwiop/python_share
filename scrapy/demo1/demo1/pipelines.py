# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 处理下载

import json

class Demo1Pipeline(object):
    def __init__(self):
        self.f =  open('2.json','w',encoding='utf-8')


    def process_item(self, item, spider):
        obj = dict(item)
        string = json.dumps(obj, ensure_ascii=False)
        self.f.write(string+ '\n')

        return item

    def close_spider(self,spider):
        self.f.close()
