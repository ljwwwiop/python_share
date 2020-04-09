import re
import requests
import json
import pymongo
from config import *
from multiprocessing import Pool

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
# 知道url

# 解析url
# 提取数据
# 保存数据


def get_page(num):
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'+str(num*20)

    r=requests.get(url)
    html=r.content.decode()   #content 二进制内容
    #print(html)
    d = json.loads(html)
    for i in d['subjects']:
        b = {
            'num':i['rate'],
            'title':i['title'],
            'url':i['url'],
        }
        print(b)
        #go_save(b)

def go_save(a):
    try:
        if db[MONGO_TABLE].insert(a):
            print("存储成功")
    except Exception:
        print("存储错误")

def main():
    for i in range(0,15):
        get_page(i)

if __name__ == '__main__':
    main()