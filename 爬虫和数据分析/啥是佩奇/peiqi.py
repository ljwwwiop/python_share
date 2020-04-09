'''
    爬取 B站 啥是佩奇弹幕 cid: 71986702
    https://api.bilibili.com/x/v2/dm/history?type=1&oid=71986702&date=2019-01-25
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'http://comment.bilibili.com/71986702.xml'
r = requests.get(url)
html = r.content.decode('utf-8')
soup = BeautifulSoup(html, 'lxml')
results = soup.find_all('d')

comments = [comment.text for comment in results]
comments_dict = {'comments': comments}


df = pd.DataFrame(comments_dict)
df.to_csv('danmu.csv', encoding='utf-8')
print("写入完成")
a = 1
for i in comments:
    print(a,' ',i)
    a+=1







