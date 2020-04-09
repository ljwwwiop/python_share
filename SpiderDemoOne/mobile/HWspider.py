#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    爬取京东 商品评论  ... 淘宝实在不行啊
    对象 红米note7 华为畅想9
    最后分析比对
    这一页是 华为   decode参数错误 (errors = 'ignore')
'''
import requests
from urllib import request
import json
import time
import random
from multiprocessing import Pool
from pyquery import PyQuery as pq
import csv
import pandas as pd
from config1 import *
import pymongo

# https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv6728&productId=100000766433&score=0&sortType=5&page=0&pageSize=10
# https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv22711&productId=6600216&score=0&sortType=5&page=0&pageSize=10

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

client =pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
def get_url(i):
    NUM = i
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv6728&productId=100000766433&score=0&sortType=5&page='+str(i)+'&pageSize=10'
    # px = request.ProxyHandler({'http':'119.101.114.166:9999'})
    # opener = request.build_opener(px)

    # r = request.Request(url,headers=headers)
    r = requests.get(url,headers = headers)
    html = r.content.decode('gbk',errors = 'ignore')
    print(html)
    html = html.replace('fetchJSON_comment98vv6728(', '')
    html = html.replace(');', '')
    # print(html)
    data = json.loads(html)
    # 获取手机特点 总结数据
    Charcter = []
    if i ==0:
        for i in data['hotCommentTagStatistics']:
            produce = {
            '特点' : i.get("name"),
            '点赞人数' : i.get("count"),
            }
            # print(produce)
            Charcter.append(produce)
        # df = pd.DataFrame(Charcter)
        # df.to_csv('HuaWeiTedian.csv', index=False, mode='a+', encoding='utf-8_sig')
        # print("特点写入完成")
    # 总页数 100

    # print(MaxPage)
    # 总评论
    ID = []
    content_note = []
    for comments in data["comments"]:
        content_note.append(pq(comments.get("content")).text()),
        for a in content_note:
            save_txt(a)
        produce = {
        'id' : comments.get("id"),
        # ID.append(id),
        'nickname' : comments.get("nickname"),
        # Nickname.append(nickname),
        'content' : pq(comments.get("content")).text(),
        # content_note.append(content),
        'time' : comments.get("creationTime"),
        'productColor' : comments.get("productColor"),
        'productSize' : comments.get("productSize"),
        'num' : comments.get("status"),
        'score' : comments.get("score"),
        'replyCount' : comments.get("replyCount"),
        'useZAN' : comments.get("usefulVoteCount"),
        }
        go_db(produce)
    print(produce)
        # DaTa = [
        # comments.get("id"),
        # comments.get("nickname"),
        # pq(comments.get("content")).text(),
        # comments.get("creationTime"),
        # comments.get("productColor"),
        # comments.get("productSize"),
        # comments.get("status"),
        # comments.get("score"),
        # comments.get("replyCount"),
        # comments.get("usefulVoteCount") ,
        # ]
        # ID.append(DaTa)
        # with open('HuaWeitest.csv','a+',newline='',encoding='utf-8') as f:
        #     # fieldnames = ['id', 'name','评论']
        #     # 获得 writer对象 delimiter是分隔符 默认为 ","
        #     writer = csv.writer(f, delimiter=' ')
        #     # writer.writeheader()
        #     writer.writerow(["id","nickname","content","time","productColor","productSize","num","score","replyCount","useZAN"])
        #     for item in ID:
        #         writer.writerow(item)
        # id = comments.get("id")
        # nickname = comments.get("nickname")
        # content = pq(comments.get("content")).text()
        # content_note.append(content)
        # time = comments.get("creationTime")
        # productColor = comments.get("productColor")
        # productSize = comments.get("productSize")
        # num = comments.get("status")
        # score = comments.get("score")
        # replyCount = comments.get("replyCount")
        # useZAN = comments.get("usefulVoteCount")
        # print(id,nickname,content,time,productColor,productSize,num,score,replyCount,useZAN)
    print("第{}页".format(NUM))

def save_txt(a):
    pass
    # with open('HuaWei.txt','a+',encoding='utf-8') as f:
    #     f.write(a)
    #     f.close()
    # print("评论写入完成")

def main():
    # 已知maxpage = 100
    for i in range(0,100):
        time.sleep(2)
        get_url(i)
    print("抓取完毕")

def go_db(a):
    try:
        if db[MONGO_TABLE].insert(a):
            print("存储成功")
    except Exception:
        print("存储错误")

if __name__ =='__main__':
    main()
    # 进程池对象
    # pool = Pool()
    # pool.map(main, [i for i in range(0,100)])






