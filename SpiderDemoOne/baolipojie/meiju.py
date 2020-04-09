'''
    枚举法 -- 暴力破解
    zipfile 库
'''
import zipfile
import random
import time
import sys
from threading import Thread
from multiprocessing import Process

# 创建一个密码类
class MyIterator():
    '''
        生成一个密码
        2 最大值 最小值 +1
    '''
    # 创建一个单位字符
    lettrt = '012345'

    min_dig = 0
    max_dig = 0

    # 类的魔法方法
    # 初始化
    def __init__(self,min_dig,max_dig):
        '''
        密码的位数 是几位
        :param min_dig: 最小值
        :param max_dig: 最大值
        '''
        if min_dig<max_dig:
            self.min_dig = min_dig
            self.max_dig = max_dig
        else:
            self.min_dig = max_dig
            self.max_dig = min_dig

    # 迭代器
    def __iter__(self):
        # 返回本身
        return self

    def __next__(self):
        '''
        生成密码  随机密码匹配  按照上面定义的规则进行密码匹配
        :return: 匹配的密码
        '''
        rst = str()
        # 生成随机数  +1 防止重复
        for item in range(0,random.randrange(self.min_dig,self.max_dig+1)):

            # 匹配字符规则
            rst+=random.choice(MyIterator.lettrt)
        return rst
# for p in MyIterator(5,6):
#     print('密码 ',p)


# 定义一个解压缩包的函数
def extact():
    # 开始时间
    start_time = time.time()
    # 导入文件
    zfile = zipfile.ZipFile(r'test.zip')

    for p in MyIterator(5,6):
    # for p in range(30000,100000):
        print('推算 ', p)
        # 捕获异常
        try:
            # path -》 指定解压后文件的存储位置
            # pwd  -》 使用密码去 提取文件   members 默认解压出来的文件 默认全部
            zfile.extractall(path='.',pwd=str(p).encode('utf-8'))
            print("密码是 ：{}".format(p))

            # 结束时间
            now_time = time.time()
            print("耗时:{}".format(now_time-start_time))
            # 文件退出
            sys.exit()

        except Exception as e:
            print(e)

if __name__ == '__main__':
    # t1 = Thread(target=extact(),args=10)

    t1 = Process(target=extact())
    t1.start()
    t1.join()
