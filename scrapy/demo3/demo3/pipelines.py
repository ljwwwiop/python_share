# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#处理数据  排版混乱 或者  排序  strip()去除空格, split()切片
#将所有数据处理方法放在这里面写
#数据持久化
#写入 保存
#写入setting 配置好

class Demo3Pipeline(object):
    def process_item(self, item, spider):
        return item
