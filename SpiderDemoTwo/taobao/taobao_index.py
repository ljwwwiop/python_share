# coding:utf-8
'''
    selenium模拟登录套   在一开始做这个脚本时经常出现运行到滑块就不动了，
    即使手动拉动滑块也会报错从而无法登录。
    经小伙伴提醒，是因为浏览器版本过低导致，还以为是腾讯的机器人识别捣的鬼
'''
import selenium
from selenium import webdriver
import time
import lxml
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException


driver = selenium.webdriver.Firefox()
driver.get('https://login.taobao.com/member/login.jhtml')
time.sleep(5)
# elem = driver.find_element_by_class_name("iconfont static")
# elem.click()
# time.sleep(3)

# user = driver.find_element_by_id("TPL_username_1")
# pwd = driver.find_element_by_id("TPL_password_1")
# submit = driver.find_element_by_id("J_SubmitStatic")

# 防止账户框本来就有账号
# user.clear()
# pwd.clear()
# time.sleep(1)
'''

'''

# user.send_keys("15671124100")
# time.sleep(3)
# pwd.send_keys("ljwiop1996")
# time.sleep(3)

# dragger=driver.find_element_by_id('nc_1_n1z')#.滑块定位
# action=ActionChains(driver)
#
# for index in range(500):
#     try:
#         action.drag_and_drop_by_offset(dragger, 500, 0).perform()#平行移动鼠标，此处直接设一个超出范围的值，这样拉到头后会报错从而结束这个动作
#     except UnexpectedAlertPresentException:
#         break
#     time.sleep(12)  #等待停顿时间

# submit.click()
time.sleep(2)

#需要滑块，再次登录，先输入密码，再滑动滑块

# pwd.click()
# pwd.send_keys('ljwiop1996')
# time.sleep(1)

print("进入了")
req = requests.session()
cookies = driver.get_cookies()
for cookie in cookies:
    # print(cookie)
    req.cookies.set(cookie['name'],cookie['value'])
req.headers.clear()# 清空头
newpage = req.get('https://cart.taobao.com/cart.htm?')
time.sleep(2)

print(html)

print("会话完成")

time.sleep(10)



driver.close()

