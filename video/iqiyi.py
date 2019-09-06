# 爬取电影
# 拼接电影的每个片段
import requests
from multiprocessing import Pool

def get_page(i):
    url = '%03d.ts'%i
    print(url)
    headers = {

    }
    r = requests.get(url,headers=headers)

    with open('mp4/%04d.mp4'%i,'ab') as f:
        # ab追加二进制数据写入
        f.write(r.content)

if __name__ == '__main__':
    #get_page()
    pool = Pool(20) #开启20个进程
    for i in range(1661):
        pool.apply_async(get_page,(i,)) #执行我们的进程  任务名是get_page 参数i

    pool.close()
    pool.join()

#拼接
# cmd 拼接 切换到存储文件  文件夹
# copy /b *.mp4 123456.mp4  把所有mp4文件拼接为123456.mp4文件
