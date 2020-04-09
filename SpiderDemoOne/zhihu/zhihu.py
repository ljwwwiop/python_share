import requests
import re
import json

# 父类基类object
class zhihu(object):
    # 获取知乎粉丝信息

    #私有方法 直接调用了
    def __init__(self,page):
        #反爬
        self.header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

        self.url = 'https://www.zhihu.com/api/v4/topics/19550517/followers?include=data%5B%2A%5D.gender%2Canswer_count%2Carticles_count%2Cfollower_count%2Cis_following%2Cis_followed&limit=20&offset={}'.format(page)

    def get(self):
        # self 对象 实例化
        html = requests.get(self.url,headers = self.header)
        for item in html.json()['data']:

            print(item['id'])
            zhihu.saveFile(item['id'])
            print('写入完毕')

    #保存  装饰器  静态方法
    @staticmethod
    def saveFile(data):
        with open('id.txt','a') as f:
            f.write(data + '\n')

if __name__ =='__main__':
    for page in range(10):
        #类实例化
        zh = zhihu(page*20)
        zh.get()