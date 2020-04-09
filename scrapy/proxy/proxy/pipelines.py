# -*- coding: utf-8 -*-

# Define your item pipelines here

# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProxyPipeline(object):
    '''
    还有 别的spider 传入 通过 name 判断 进行对应的操作
    直接将item 传入到pipeline中
    在pipeline 中提取和解析数据
    在保存数据
    '''
    def process_item(self, item, spider):
        open('kdl_proxy_one.txt','a').write(item['addr']+'\n')
        print('完成下载')
        return item