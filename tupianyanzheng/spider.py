'''
    爬取武汉大学 验证码
'''
import requests
import re

url = 'http://210.42.121.241/'
r = requests.get(url)
html = r.content.decode('gbk')
req = re.findall('.*src="(.*?GenImg)"',html,re.S)
print(req)
# <img id="captcha-img" alt="验证码" src="/servlet/GenImg">
