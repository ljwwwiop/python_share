import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
from pyquery import PyQuery as pq
import pymongo
from config import *
#启动
client =pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

browser = webdriver.Chrome()
def get_url(i):
    url = 'https://sh.fang.lianjia.com/loupan/pg'+str(i)+'/'
    browser.get(url)
    parse_url()
    print("第{}页".format(i))
    a = "window.scrollTo(0,800);"
    b = "window.scrollTo(0,1600);"
    c = "window.scrollTo(0,3200);"
    browser.execute_script(a)
    time.sleep(2)
    browser.execute_script(b)
    time.sleep(2)
    browser.execute_script(c)
    time.sleep(2)



def go_next_page(i):
    parse_url()
    print("wait")
    a = "window.scrollTo(0,800);"
    b = "window.scrollTo(0,1600);"
    c = "window.scrollTo(0,3200);"
    browser.execute_script(a)
    time.sleep(3)
    browser.execute_script(b)
    time.sleep(3)
    browser.execute_script(c)
    time.sleep(3)
    # 跳转按钮
    # next_page = browser.find_element_by_class_name('next')
    # next_page.click()
    # print(browser.page_source)
    get_url(i)




def parse_url():
    html = browser.page_source
    doc = pq(html)
    # print(html)
    house = doc('.resblock-list-wrapper li').items()
    # 直接提取自己需要的 . 表示 class
    for i in house:
        house_data = {
            "小区名称":i.find('.name').text(),
            "房类":i.find('.resblock-type').text(),
            "售卖状态":i.find('.sale-status').text(),
            "顾问":i.find('.agent').text().strip('新房顾问：'),
            "地址":i.find('.resblock-location').text(),
            "内室种类":i.find('.resblock-room').text(),
            "面积":i.find('.resblock-area').text().strip('建面 '),
            "房价":i.find('.number').text(),
            "总价":i.find('.second').text(),
            "特色":i.find('resblock-tag').text(),
        }
        print(house_data)
        save_to_mongo(house_data)


def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print("存储成功")
    except Exception:
        print("存储错误")

def main():
    get_url(1)
    for i in range(2,76):
        get_url(i)
    browser.close()

if __name__ =='__main__':
    main()





