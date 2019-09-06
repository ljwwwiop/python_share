#cording=utf-8
#猫眼top 100信息
#正则匹配 一定要写结束标签
from multiprocessing import Pool  #开启线程  进程池   做到秒抓取文件
import json
import requests
import re
from requests.exceptions import RequestException
import pymongo
from config import *
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

def get_one_page(url):
	try:
		r=requests.get(url,headers=header)
		if r.status_code == 200:
			return r.text
	except RequestException:
		return none

def parse_one_page(html):
	req = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
	items = re.findall(req,html)
	for item in items:
		yield{
			'index':item[0],
			'title':item[2],
			'actor':item[3].strip()[3:], #strip()[3:]前三个字符切掉   切掉空格
			'time':item[4].strip()[5:],#切掉前面5个字符
			'score':item[5]+item[6],#拼接
			'image':item[1]
		}
		#yield 创建一个字典格式

def save_to_mongo(item):
	if db[MONGO_TABLE].insert(item):
		print('成功',item)
		return True
	return False


def write(content):
	with open('maoyan.txt','a',encoding='utf-8') as f:#encoding 防止编码  ensure_ascii=False一起使用将汉字转化
		f.write(json.dumps(content,ensure_ascii=False)+'\n')  #json.dumps写入(content)文件  json 将字典格式的文本写入  
		f.close()#必须要导入 json包

def main(offset):
	url = 'http://maoyan.com/board/4?offset='+str(offset)
	html = get_one_page(url)
	for item in parse_one_page(html):
		write(item)
		if item:save_to_mongo(item)



if __name__ == '__main__':
	# for i in range(10):
	# 	main(10)

	pool = Pool()  #调用线程池  创建对象
	pool.map(main,[i*10 for i in range(10)]) #pool.map()方法  提高抓取效率
	print("全部写入完成!")


# url = 'http://maoyan.com/board/4?'
# url='http://maoyan.com/board/4?offset=0'
# r = requests.get(url,headers=header)
# html = r.content.decode()
# print(html)
# 						<dd>
#                          <i class="board-index board-index-10">10</i>
#     <a href="/films/7431" title="乱世佳人" class="image-link" data-act="boarditem-click" data-val="{movieId:7431}">
#       <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
#       <img data-src="http://p0.meituan.net/movie/230e71d398e0c54730d58dc4bb6e4cca51662.jpg@160w_220h_1e_1c" alt="乱世佳 人" class="board-img" />
#     </a>
#     <div class="board-item-main">
#       <div class="board-item-content">
#               <div class="movie-item-info">
#         <p class="name"><a href="/films/7431" title="乱世佳人" data-act="boarditem-click" data-val="{movieId:7431}">乱世佳人</a></p>
#         <p class="star">
#                 主演：费雯·丽,克拉克·盖博,奥利维娅·德哈维兰
#         </p>
# <p class="releasetime">上映时间：1939-12-15(美国)</p>
