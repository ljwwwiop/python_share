import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.set_window_size(1000,800)

    driver.get('https://weibo.com')
    time.sleep(5)
    print(driver.title)
    #账号
    email = [x,x,x]
    #密码
    pwd = ['x','x','x','x']
    loginname = driver.find_element_by_id('loginname')
    for i in email:
        loginname.send_keys(i)
    time.sleep(0.1)
    loginname.send_keys(Keys.TAB)
    time.sleep(0.1)
    password = driver.find_element_by_xpath('//input[@name="password"]')
    for i in pwd:
        password.send_keys(i)
        # time.sleep(0.1)
    time.sleep(10)

    btn = driver.find_element_by_xpath('//a[@action-type="btn_submit"]')
    btn.click()

    print(driver.title)

    username = driver.find_element_by_xpath('//div[@class="nameBox"]/a')

    driver.close()
    driver.quit()




