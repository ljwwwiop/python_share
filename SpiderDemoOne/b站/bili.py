import requests
import pprint
import json
from urllib.parse import urlencode
import random
import time


headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}


def parse_url(url):
    response = requests.get(url)
    # pprint.pprint(response.json())
    html = response.content.decode()
    a = json.loads(html)
    for i in a.get('data').get('items'):
        # for b in i['items']:
            name = i.get('user').get('name')
            url = i.get('item').get('video_playurl')
            num = i.get('item').get('watched_num')
            time = i.get('item').get('upload_time')
            print('ID: ',name,' ',url,'播放量: ',num,'时间：',time)
            # response_mp4 = requests.get(url,headers=headers,stream=True)  # 数据流的方式 写入
            # # 分段写入 定义每一次读取数据量
            #
            # if response_mp4.status_code == 200:
            #     #迭代段点 写入 分段写入
            #     for data in response_mp4.iter_content(chunk_size=1024):
            #         with open(name+".mp4",mode="ab") as f:  # ab  a是写入方式 b是写入2进制
            #             f.write(data)
            #     print('good')

            response_mp4 = requests.get(url, headers=headers, stream=True)  # 数据流的方式 写入
            # 分段写入 定义每一次读取数据量
            if response_mp4.status_code == 200:
                 with open(name+".mp4", mode="ab") as f:  # ab  a是写入方式 b是写入2进制
                    f.write(response_mp4.content)
                    print('完成')

time.sleep(random.randint(2,6))




def get_url():
    url = 'http://api.vc.bilibili.com/board/v1/ranking/top?'
    for i in range(10):
        parms = {
            "page_size":"10",
            "next_offset":i*10+1 ,
            "tag": "今日热门",
            "platform": "pc"
        }
        # 拼接url
        url_1 = url+urlencode(parms)
        parse_url(url_1)


    
def main():
    get_url()

if __name__ == '__main__':
    main()