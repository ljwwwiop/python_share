'''
    抓取《流浪地球》电影  豆瓣差评 2019/2/8 20：00 开始的
    8.0评分
    抓取《飞驰人数》电影   豆瓣差评  7.0       30163509
    抓取《疯狂外星人》     豆瓣差评  6.5  Car   25986662
'''
import requests
import re
from pyquery import PyQuery as pq
import time
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Cookie': 'bid=RA00DecNHdk; ll="118254"; __yadk_uid=qgxrmqI8clztszq51MjqLYeY8bJQYiyg; _vwo_uuid_v2=D5634E6D8AC7C2FD20A29A6264B832E35|64a06c11068bc04ccac46374bdecb1f0; gr_user_id=79568fff-b211-417c-b6c0-ddb6a73decc8; viewed="30225784_30279640_30193594_30346218_30240074"; douban-fav-remind=1; __utmv=30149280.16318; __utmz=30149280.1548915945.22.15.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1549625850%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E8%25B1%2586%25E7%2593%25A3%26rsv_spt%3D1%26rsv_iqid%3D0x9f98527a0004ce60%26issp%3D1%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_sug3%3D12%26rsv_sug1%3D10%26rsv_sug7%3D100%26rsv_t%3Dec8aGlmwIX81rwPBrWePim7JT55hvBbucLus%252FAxKAhKPEif5wM8guSY8nu5fNEUMXWEl%26rsv_sug2%3D0%26inputT%3D3537%26rsv_sug4%3D3884%26rsv_sug%3D1%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1620229716.1540213514.1548915945.1549625850.23; __utmc=30149280; __utma=223695111.1901402553.1541504503.1545839932.1549625850.18; __utmb=223695111.0.10.1549625850; __utmc=223695111; __utmz=223695111.1549625850.18.13.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3; __utmb=30149280.4.10.1549625850; dbcl2="163187763:OJGe3u9rNGA"; ck=QflB; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=273e977806a86f89.1541504504.14.1549627729.1545840084.',
}

Cookie = {

}

def get_url(i):
    url = 'https://movie.douban.com/subject/30163509/comments?start='+str(i*20)+'&limit=20&sort=new_score&status=P&percent_type=l'
    r= requests.get(url,headers)
    html = r.content.decode('utf-8',errors = 'ignore')
    doc = pq(html)
    data = doc('.mod-bd .comment-item').items()
    with open('Aliencomment.csv','a+',newline='',encoding='utf_8_sig') as f:
        writer = csv.DictWriter(f,fieldnames=['点赞数', '姓名','时间', '评论'])
        writer.writeheader()
        for i in data:
            comment = i.find('.short').text(),
            info = dict()
            info['时间'] = i.find('.comment-time ').text(),
            info['评论'] = i.find('.short').text(),
            info['点赞数'] = i.find('.votes').text(),
            info['姓名'] = i.find('a').text().strip(' 有用 '),
            to_save_text(str(comment))
            writer.writerow(info)
        print('good')


def to_save_text(t):
    with open('Aliencom.txt','a+',encoding='utf-8') as f:
        f.write(t+'\n')
    print("txt写入成功")
    f.close()

def main():
    for i in range(21):
        get_url(i)
        time.sleep(2)

if __name__ =='__main__':
    main()












