'''
    简单的视频抓取
    2020/2/5
    好几年没写爬虫了...
'''
import requests, re
from lxml import etree
from urllib.request import urlretrieve

'''
    # 获取视频ID
    # 拼接完整URL
    # 获取视频地址
    # 下载视频
'''

def GetVideo():
    url = "http://www.pearvideo.com/popular"
    html = requests.get(url).text
    html = etree.HTML(html)
    # video_id 保存视频的ID
    video_id = html.xpath('//li[@class ="popularem clearfix"]/a/@href')
    # 构造一个新的url
    video_url = []
    starturl = 'http://www.pearvideo.com/'
    for i in video_id:
        new_url = starturl + i
        video_url.append(new_url)
    # 此时再进行一个新的页面爬去,重复上面过程
    for i in video_url:
        html = requests.get(i).text
        req = 'srcUrl="(.*?)"'
        # 找到真正的地址
        purl = re.findall(req, html)
        req = '<h1 class="video-tt">(.*?)</h1>'
        pname = re.findall(req, html)
        print("正在下载视频:%s" % pname[0])
        # 下载
        urlretrieve(purl[0], './梨视频/%s.mp4' % pname[0])

def main():
    GetVideo()

if __name__ == "__main__":
    main()

