import requests
import lxml
import re

#  抓取豆瓣TOP250电影的信息

url = 'https://movie.douban.com/top250?start=0&filter='
r=requests.get(url)
html = r.content.decode()
req = re.findall('<em class="">(.*?)</em>.*?<li.*?hd.*?title">(.*?)</span>.*?<p.*?>(.*?);&nbsp;&nbsp;(.*?)<br>(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)</p>.*?average">(.*?)</span>.*?inq">(.*?)</span>.*?</li>',html,re.S)
for i in req:
    print(i)



