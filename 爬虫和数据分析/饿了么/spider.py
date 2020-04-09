'''
    爬取武生院饿了么商户信息
'''
import requests
import json
import time

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
     'Cookie':'ubt_ssid=razji1rykobwlhv6ns9c7nev1i46jh8k_2019-01-08; _utrace=ab1ca8b617ea2fe2e086212564f487dc_2019-01-08; cna=uJxLFMaH4xkCAT231kJeXVuo; track_id=1546959091|6305e8a7ae77db2d22cf3fd4c2adde03c59f6cdd53a0800900|53683ac60bdadce5775e5eb0e52f459e; USERID=164806008; UTUSER=164806008; SID=zd0GxwmyVzo1gKf1S6YedihCfeJgnVH230GQ; isg=BISEdncrhEOiQDCP9sy-P3xEVQK2NakCYiTZ3J4lmM8SySCT06_fljFoDWERVOBf; pizza73686f7070696e67=aKonJFn5Q5TBxydFSWJGpq3kAR0hSwYUvq5uEqqXw3R10tFhujoqK9Xk4zfekd8U'
}
def get_url(i):
    url = "https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&latitude=30.71245&longitude=114.52593&offset={i}&restaurant_category_ids%5B%5D=-100&terminal=web".format(i=i)
    r = requests.get(url,headers = headers)
    html = r.content.decode()
# 去除数组结构
    html[1:][:-1]
# print(html[1:][:-1])
    json_obj = json.loads(html)
    for i in json_obj:
    # print(i.get("act_tag"),i.get("address"))
        produce = {
            "名字":i.get("name"),
            "配送费":i.get("float_delivery_fee"),
            "评分":i.get("rating"),
            "营业时间":i.get("next_business_time"),
            "今日活动":i.get("piecewise_agent_fee").get("description"),
            "评价等待时间":i.get("order_lead_time"),
            "最高月销量":i.get("recent_order_num"),
            "今日订单量":i.get("rating_count"),

    }
        print(produce)
    print("--"*30)
    time.sleep(2)

def main():
    for i in range(0,96,24):
        get_url(i)

if __name__=='__main__':
    main()


