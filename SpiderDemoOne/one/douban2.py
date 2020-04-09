#cording=utf-8
#豆瓣电影

import re
import requests
import time
# header={
# 	'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
# }

with open('movies.txt','a',encoding='utf-8') as f:
#https://movie.douban.com/top250?start=75
	for a in range(4,5):
		url='https://movie.douban.com/top250?start='+str(a*25)
		r=requests.get(url)
		html=r.content.decode()
		names=re.findall('<em class="">(.*?)</em>.*?<li.*?hd.*?title">(.*?)</span>.*?<p.*?>(.*?);&nbsp;&nbsp;(.*?)<br>(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)</p>.*?average">(.*?)</span>.*?inq">(.*?)</span>.*?</li>',
		html,re.S)
		for i in names:
			print(i)
			i=re.sub('&nbsp','',i)
	# 		f.write(i[0]+'\n'+i[1].strip()+'\n'+i[2]+'\n'+i[3].strip()+'\n'+i[4]+'\n'+i[5].strip()+'\n'+'评分：'+i[6]+'\n--*---*---*---\n')
	# print("下载完成！")
	# f.close()


#'<li.*?hd.*?title">(.*?)</span>.*?<p.*?>(.*?);&nbsp;&nbsp;(.*?)<br>(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)</p>.*?average">(.*?)</span>.*?inq">(.*?)</span>.*?</li>',re.S
