# -*- coding:utf8 -*-
# 抓取西刺网 代理并且 检测是否可用 最后保存
# 方法很好

import re
import time

import requests
from lxml import etree

# 请求路径，西刺代理网站
for i in range(1,30):
    url = 'http://www.xicidaili.com/nn/'+str(i)
    # 请求响应头
    headers = header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    # 通过requests的get方法访问目标网站，获得响应对象
    response = requests.get(url=url, headers=headers)

    #创建一个etree对象，response.text为访问后的到的整个西刺代理页面
    etree_obj = etree.HTML(response.text)
    #通过筛选response.text，得到包含ip信息的列表
    ip_list = etree_obj.xpath("//tr[@class='odd']")
    item = []
    #遍历得到的集合，将ip，和端口信息进行拼接，添加到item列表
    for ip in ip_list:
        ip_num = ip.xpath('./td[2]/text()')[0]
        port_num = ip.xpath('./td[3]/text()')[0]
        http = ip_num + ':' +port_num
        item.append(http)


    #遍历访问，检测IP活性
    court=0
    for it in item:
        #因为并不是每个IP都是能用，所以要进行异常处理
        try:
            proxy = {
                'http':it
            }
            url1 = 'https://www.baidu.com/'
            #遍历时，利用访问百度，设定timeout=1,即在1秒内，未送到响应就断开连接
            res = requests.get(url=url1,proxies=proxy,headers=headers,timeout=1)
            #打印检测信息，elapsed.total_seconds()获取响应的时间
            print(it +'--',res.elapsed.total_seconds())
            court+=1
            if res.elapsed.total_seconds()<1:
                with open('proxy_two.txt','a+') as f:
                    f.write(it+'\n')
                print(it+'，写入完成!')
            print('总共',court,'个代理')
        except BaseException as e:
            print(e)

