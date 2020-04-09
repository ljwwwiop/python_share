import requests
import json
import time

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'cookies':'_T_WM=e97e0ff8d8ca0b8db1d1b44259a322ff; SUB=_2A25xHIC6DeRhGeNN7VYS-SfKwjiIHXVS_iDyrDV6PUJbkdAKLU_nkW1NSbUgupQJgdc6kiMCZvzxt1PaPRuL2N3R; SUHB=0y0ZjdTLs_kGAY; SCF=Al0ww0UF7vuGoeTQPLU05-0gkGu80qB4mlazwxVvWRXSW8i2CtT9A-aLYGJXmsbZRHmdgpvlO_WwwGyXHGmb80E.; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4317977308328828%26luicode%3D20000061%26lfid%3D4317977308328828'
}

url = 'https://m.weibo.cn/api/comments/show?id=4317977308328828&page=2'
html = requests.get(url,headers = headers)
ii = 1
while html.status_code==200:
    ii = ii+1
    url_next='https://m.weibo.cn/api/comments/show?id=44317977308328828&page='+str(ii)

    try:
        for jj in range(1,len(html.json()['data'])):
            data1 = [(html.json()['data'][0]['id'],
            html.json()['data'][jj]['user']['screen_name'],
            html.json()['data'][jj]['created_at'],
            html.json()['data'][jj]['source'],
            html.json()['data'][jj]['user']['id'],
            html.json()['data'][jj]['user']['profile_url'],
            html.json()['data'][jj]['user']['profile_image_url'],
            html.json()['data'][jj]['text'])],
            print(data1)
    except:
        pass


