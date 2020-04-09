import requests

headers={
    'Cookie': 'SINAGLOBAL=4955113080777.212.1541779260756; SCF=AtVY6nop_PnCNRe-KD-dhECpqs8KTRtLqtpbOwnAVEN29mmxFi18ez3HLs1By19g6nxX4lAjjNJwIVxAzs9biNo.; SUHB=0sqBafC42Mn-a7; UOR=www.zhongshikaoyan.com,widget.weibo.com,www.baidu.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhpcXm4MJ0eO88fdSfO.a6y5JpX5oz75NHD95Qfe0qXe0.4So.XWs4Dqcj6i--fiKyWi-27i--ciKLhi-8Wi--fiK.7iKLFi--Xi-iWiKnci--ciKyFiKn4i--ciKyFiKLhi--ciKn4iK.R; ALF=1547803896; SUB=_2A25xHn-mDeRhGeNN7VYS-SfKwjiIHXVS4QHurDV8PUJbkNAKLUTEkW1NSbUguplNBGNqmv7OVRcOuJsGvy_21mOK; Ugrow-G0=56862bac2f6bf97368b95873bc687eef; wvr=6; YF-V5-G0=c948c7abbe2dbb5da556924587966312; YF-Page-G0=091b90e49b7b3ab2860004fba404a078; wb_view_log_5364399694=1366*7681; _s_tentry=-; Apache=571248322355.1001.1545840566811; ULV=1545840566865:10:8:1:571248322355.1001.1545840566811:1545142803281',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

url='https://weibo.com/p/1004061537790411/follow?relate=fans&page=1#Pl_Official_HisRelation__58'
r = requests.get(url,headers=headers)
html = r.content.decode('utf-8')
print(html)