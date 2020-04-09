'''
    获取 B站用户 用户信息
'''

import requests
import json
import random
import time
import re

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Cookie':'LIVE_BUVID=AUTO3315396110060035; sid=7lteikm9; buvid3=0C5D35EA-9166-4812-85BC-2F4A29719C0816733infoc; rpdid=owkspsqoopdosklxsqqxw; fts=1539742910; CURRENT_FNVAL=16; UM_distinctid=1669b6b4c6c117-0fd8a3783c371a-514d2f1f-13c680-1669b6b4c6d62b; im_notify_type_87043740=0; im_local_unread_87043740=0; im_seqno_87043740=18; DedeUserID=87043740; DedeUserID__ckMd5=780d257b728497b8; SESSDATA=ab27f9c1%2C1547800928%2C987014c1; bili_jct=15eb23041346adac8deba054f743fc16; finger=17c9e5f5; CURRENT_QUALITY=32; stardustvideo=1; bp_t_offset_87043740=208518166850816134; _dfcaptcha=9e4984bf14e0a4c15cde1a6538f7815e'
}

proxies = {
        'http': 'http://119.101.114.166:9999',
        'http': 'http://119.101.113.217:9999',
        'http': 'http://119.101.112.24:9999',
        'http': 'http://27.42.168.46:48919',
        'http': 'http://119.101.113.96:9999',
        'http': 'http://119.101.115.86:9999',
        'http': 'http://119.101.115.132:9999',
        'http': 'http://119.101.117.83:9999',
}
for i in range(1,6):
    url = 'http://api.bilibili.com/x/relation/followers?vmid=346139605&pn='+str(i)
    r = requests.get(url,headers=headers).text
    #print(r)
    data = json.loads(r)
    if 'data' in data.keys():
        jsdata = data['data']
        jsData = jsdata['list']
        for a in jsData:
            mid = a['mid']
            name = a['uname']
            face = a['face']
            mtime = a['mtime']
            sign = a['sign']
            type = a["official_verify"]["type"]
            # desc = a["official_verify"]["desc"]
            vip = a["vip"]["vipType"]
            print(mid,name,face,mtime,sign,type,vip)
# jsDict = json.loads(r)
# if 'data' in jsDict.keys():
#     jsData = jsDict['data']
#     mid = jsData['mid']
#     name = jsData['name']
#     sex = jsData['sex']
#     rank = jsData['rank']
#     face = jsData['face']
#    print(mid,name,sex,rank,face)















