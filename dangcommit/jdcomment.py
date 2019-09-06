# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import json
import csv

headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

head = ['time', 'score','content','id', 'bookName']

p = open('1.csv', 'a+', encoding='utf-8')
swrite = csv.writer(p, dialect='excel')
swrite.writerow(['时间', '分数', '评论', 'id', '书名'])
def get_page(i):
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv16024&productId=11993134&score=0&sortType=5&page='+str(i)+'&pageSize=10&isShadowS=0&fold=1'
    r = requests.get(url,headers=headers)
    html = r.content.decode('gbk')
    html=html.replace('fetchJSON_comment98vv16024(','')
    html=html.replace(');','')
    b=json.loads(html)
    f=[]
    for i in b['comments']:
        produce = [
            i['creationTime'],
            i['score'],
            i["content"],
            i['id'],
            i['referenceName'],
        ]
        print(produce)
        f.append(produce)

        for item in f:
            swrite.writerow(item)
def main():
    for i in range(0,5):
        get_page(i)

if __name__ =='__main__':
    main()
