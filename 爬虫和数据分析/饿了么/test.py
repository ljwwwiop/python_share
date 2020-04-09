'''
    爬取武生院饿了么商户信息
    一共 192 个店铺
    采用的是h5流式爬取
'''
import requests
import json
import time
import csv

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
     'Cookie':'ubt_ssid=razji1rykobwlhv6ns9c7nev1i46jh8k_2019-01-08; _utrace=ab1ca8b617ea2fe2e086212564f487dc_2019-01-08; perf_ssid=rb2dli6o5m7cted0hk3u35kiegcz2nsw_2019-01-08; cna=uJxLFMaH4xkCAT231kJeXVuo; track_id=1546959091|6305e8a7ae77db2d22cf3fd4c2adde03c59f6cdd53a0800900|53683ac60bdadce5775e5eb0e52f459e; USERID=164806008; UTUSER=164806008; SID=zd0GxwmyVzo1gKf1S6YedihCfeJgnVH230GQ; isg=BLu7TCazY_Sr_V9CJXH5an_BSp_luM4XwcF2Ua141brRDNvuN-BfYtkNIqxCLCcK'}

def get_url(i):
    url = 'https://h5.ele.me/restapi/shopping/v3/restaurants?latitude=30.71245&longitude=114.52593&keyword=&offset={i}&limit=8&extras[]=activities&extras[]=tags&terminal=h5'.format(i=i*8)

    re = json.loads(requests.get(url, headers=headers).text)
    # print(html)
    # html[1:][:-1]
    # encoding='utf-8-sig' 防止中文写入乱码
    with open('restaurant.csv','a+',newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=['名称', '月销售量','配送费', '起送价', '风味','评分', '配送时长', '评分统计', '距离', '地址'])
        writer.writeheader()
        for i in re.get("items"):
            # print(i)
            info = dict()
            restaurant = i.get('restaurant')
            info['地址'] = restaurant.get('address')
            info['配送费'] = restaurant.get('float_delivery_fee')
            info['名称'] = restaurant.get('name')
            info['配送时长'] = restaurant.get('order_lead_time')
            info['距离'] = restaurant.get('distance')
            info['起送价'] = restaurant.get('float_minimum_order_amount')
            info['评分'] = restaurant.get('rating')
            info['月销售量'] = restaurant.get('recent_order_num')
            info['评分统计'] = restaurant.get('rating_count')
            info['风味'] = restaurant.get('flavors')[0].get('name')
            writer.writerow(info)
        print(info)
        print('***'*40)


def main():
    for i in range(0,25):
        get_url(i)
    print("结束")

if __name__=='__main__':
    main()

