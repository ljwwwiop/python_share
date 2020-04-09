# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import json
import jsonpath


headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

url='http://product.dangdang.com/index.php?r=comment%2Flist&productId=24003310&categoryPath=01.54.06.19.00.00&mainProductId=24003310&mediumId=0&pageIndex=1&sortType=1&filterType=1&isSystem=1&tagId=0&tagFilterCount=0&template=publish'
r = requests.get(url,headers=headers)
html= r.content.decode('gbk')
old = json.loads(html)
d = json.dumps(old,ensure_ascii=False)
# for i in d['data']:
#     print(i)
e = jsonpath.jsonpath(d,"html")
print(e)