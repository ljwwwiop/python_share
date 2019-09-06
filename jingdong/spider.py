#cording = utf-8
#selenium 爬取 天猫
# 1 搜索关键词
# 2 分析页码翻页
# 3 提取内容pyquery
# 4 存储到Mongodb
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from config import  *
import pymongo
#可以安装phantomjs 无浏览器运行
#启动
client =pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

browser = webdriver.Chrome()

wait = WebDriverWait(browser, 10)

def search():
    try:
        browser.get('https://www.jd.com/')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#key'))
        )
        #点击按钮事件
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#search > div > div.form > button')))
        #输入文字
        input.send_keys('surface pro')
        submit.click()
        total=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_bottomPage > span.p-skip > em:nth-child(1) > b')))
        parse_get()
        return total.text
    except TimeoutException:
        return search()

def next_page(number):

    try:
        # input = wait.until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > input'))
        # )
        parse_get()
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.pn-next')))
        submit.click()
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(15)

    except selenium.common.exceptions.NosuchElementException:
        # 点击按钮事件
        return True
    except selenium.common.exceptions.TimeoutException:
        print('turn_page:timeout')
        next_page(number)
        #清空输入
        # input.clear()
        # input.send_keys(number)
        #点击按钮

        #页面是否到达判定
        #wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#J_bottomPage > span.p-num > a:nth-child()'),str(number)))
    except selenium.common.exceptions.StaleElementReferenceException:
        print('Exception')
        browser.refresh()
    else:
        return False

def parse_get():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_goodsList > ul')))
    html=browser.page_source
    #print(html)
    soup = BeautifulSoup(html,"lxml")
    goods_info = soup.select(".gl-item")
    for info in goods_info:
        produce = {
            'title': info.select(".p-name.p-name-type-2 a")[0].text.strip(),
            'name':info.select(".J_im_icon")[0].text.strip(),
            'price':info.select(".p-price")[0].text.strip(),
            'commit':info.select(".p-commit")[0].text.strip(),
        }
        print(produce)
        save_to_mongo(produce)
        # title = info.select(".p-name.p-name-type-2 a")[0].text.strip()
        # price = info.select(".p-price")[0].text.strip()
        # print(title)
        # print(price)

def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print("存储成功")
    except Exception:
        print("存储错误")


def main():
    total = int(search())

    # total = int(re.compile('(\d+)').search(total).group(1)) #提取出80页
    #循环遍历
    for i in range(2,total+1):
        next_page(i)
    browser.close()

if __name__ == '__main__':
    main()
