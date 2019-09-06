# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

url = 'http://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=lol%E5%A3%81%E7%BA%B8&oriquery=LOL&ofr=LOL&sensitive=0'
r = requests.get(url)
html = r.content.decode('utf8')
req = re.findall('"objURL":"(.*?)"',html)
print(req)