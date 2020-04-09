# coding = utf -8
import requests
import json
from pyquery import PyQuery as pq
import pandas
import csv
import time
# coding= utf-8
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'cookies':'_T_WM=e97e0ff8d8ca0b8db1d1b44259a322ff; SUB=_2A25xHIC6DeRhGeNN7VYS-SfKwjiIHXVS_iDyrDV6PUJbkdAKLU_nkW1NSbUgupQJgdc6kiMCZvzxt1PaPRuL2N3R; SUHB=0y0ZjdTLs_kGAY; SCF=Al0ww0UF7vuGoeTQPLU05-0gkGu80qB4mlazwxVvWRXSW8i2CtT9A-aLYGJXmsbZRHmdgpvlO_WwwGyXHGmb80E.; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4317977308328828%26luicode%3D20000061%26lfid%3D4317977308328828'
}

#'https://m.weibo.cn/comments/hotflow?id=4317977308328828&mid=4317977308328828&max_id_type=0'
def get_url():
    url ='https://m.weibo.cn/comments/hotflow?id=4317977308328828&mid=4317977308328828&max_id_type=0'
    #.format(str(i)) for i in range(0,200)]
    head = ['id','time','zan','comment','text','user','fans','follow']

    r = requests.get(url,headers=headers)
    html = r.content.decode()

    d = json.loads(html)
   # d = json.dumps(d, ensure_ascii=False)
    for i in d.get('data').get('data'):
        # 新一种构建字典方法
        # produce = [(
        #     i.get('id'),
        #     i.get('created_at'),
        #     i.get('like_count'),
        #     i.get('total_number'),
        #     str(pq(i.get('text')).text()),
        #     # 将评论修改好
        #     str(i.get('user').get('screen_name')),
        #     i.get('user').get('followers_count'),
        #     i.get('user').get('follow_count'),
        #     # 内层提取user name
        # )]
        produce = {
            'id':[i.get('id')],
            'time':[i.get('created_at')],
            'zan':[i.get('like_count')],
            'comment':[i.get('total_number')],
            'text':[str(pq(i.get('text')).text())],
            # 将评论修改好
            'name':[str(i.get('user').get('screen_name'))],
            'fans':[i.get('user').get('followers_count')],
            'follow':[i.get('user').get('follow_count')]
            # 内层提取user name
        }
        time.sleep(1)
        print(produce)
        data = pandas.DataFrame(produce)

         # 解决存储问题 的编码 utf-8_sig
        data.to_csv('csvFile3.csv',index=False,mode='a+',encoding='utf-8_sig')
        # a+ 模式 追加模式写入 不会覆盖

    #print('over')

    # https://m.weibo.cn/api/comments/show?id=4173028302302955&page={}
    # 构造评论 url
    #https://m.weibo.cn/api/comments/hotflow?id=4317977308328828&page=1

def main():
    # for i in range(0,15):
    #     get_url(i)
    get_url()
if __name__=='__main__':
    main()

