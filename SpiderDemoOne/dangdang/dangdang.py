from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import re
from bs4 import BeautifulSoup
import time
from config import  *
import pymongo

client =pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

def get_page():
    try:
        browser.get('http://book.dangdang.com')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#key_S'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#form_search_new > input.button')))
        input.send_keys('python')
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#go_sort > div > div.data > span:nth-child(3)')))
        return total.text
    except TimeoutException:
        return get_page()


def next_page():
    try:
        parse_page()
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#go_sort > div > div.data > a.arrow_r.arrow_r_on')))
        submit.click()
        time.sleep(5)
    except TimeoutException:
        browser.refresh()

def parse_page():
    #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#\31 2810 > div:nth-child(1) > div.con.shoplist')))
    html = browser.page_source
    #print(html)
    #bs4 核心算法
    soup = BeautifulSoup(html, "html.parser")
    lis = soup('li', {'class': re.compile(r'line'), 'id': re.compile(r'p')})
    for li in lis:

        a= li.find_all('a', {'name': 'itemlist-title', 'dd_name': '单品标题'})
        b= li.find_all('span', {'class': 'search_now_price'})
        c= li.find_all('span', {'class': 'search_pre_price'})
        d= li.find_all('a', {'class': 'search_comment_num'})
        e= li.find_all('a', {'name': 'itemlist-author','dd_name':'单品作者'})
        if not len(d)==0:
            dd=d[0].text
        else:
            dd='null'

        if not len(e)==0:
            write=e[0].attrs['title']
        else:
            write='null'
        if not len(a) == 0:
            link = a[0].attrs['href']
            title =a[0].attrs['title']
        else:
            link='null'
            title='null'

        if not len(b) ==0:
            prnow = b[0].string
        else:
            prnow= 'null'

        if not len(c) ==0:
            prpre = c[0].string
        else:
            prpre= 'null'
        produce={
            'link':link,
            'title':title,
            'write':write,
            'prnow':prnow,
            'prpre':prpre,
            'commit':dd,
        }
        print(produce)
        go_db(produce)

def go_db(a):
    try:
        if db[MONGO_TABLE].insert(a):
            print("存储成功")
    except Exception:
        print("存储错误")


def main():
    total=get_page()
    total = int(re.compile('(\d+)').search(total).group(1))
    for i in range(50,total):
        next_page()

    browser.close()
    print('爬取当当网结束！')
if __name__ == '__main__':
    main()
