'''
    构建一个测试 proxy 代理的一个测试脚本
    将抓取到的ip 导入进来进行测试
'''

import requests
# 导入进程池 开启多线程模式
from multiprocessing.dummy import Pool as ThreadPool

alive_ip = []

pool = ThreadPool()
# 设置进程池的数量
pool = ThreadPool(20)

def test_alive(proxy):
    '''
    通过请求百度，看是否能够得到反馈
    '''
    url= 'https://www.baidu.com/'
    global alive_ip
    proxies = {
        'http':proxy
    }
    print('正在测试：{}'.format(proxies))
    try:
        r = requests.get(url,proxies =proxies,timeout=3)
        if r.status_code ==200:
            print('代理，{}，存活'.format(proxy))
            alive_ip.append(proxy)
    except:
        print('失败！')

    def Save_file(alive_ip=[]):
        '''
        写入，保存下来

        '''
        with open('alive_ip.txt','a+') as f:
            for ip in alive_ip:
                f.write(ip+'\n')
            print('写入完成')
    def test(filename='kdl_proxy_one.txt'):
        #  打开 导入 测试文件
        with open(filename,'r') as f:
            lines = f.readlines()
            # 剔除掉 每一行得\n \r之类得
            # 生成一个新的了列表
            proxy = list(map(lambda x:x.strip(),[y for y in lines]))

            # 开启进程池
            pool.map(test_alive,proxy)

        Save_file(alive_ip)

