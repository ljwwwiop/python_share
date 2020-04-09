import itchat
import requests
from threading import Timer
import random

# 微信脚本工具


# 获取金山词霸每日一句，英文和翻译

def get_news():
    url = "http://open.iciba.com/dsapi"

    r = requests.get(url)

    contents = r.json()['content']

    translation = r.json()['translation']

    return contents, translation


# 发送消息

def send_news():
    try:

        itchat.auto_login()  # 会弹出网页二维码，扫描即可，登入你的微信账号，True保持登入状态

        my_girfriend = itchat.search_friends(name='刘莉莉')  # name改成你心爱的人在你微信的备注

        mylover = my_girfriend[0]["UserName"]

        message1 = str(get_news()[0])  # 获取金山字典的内容

        content = str(get_news()[1][17:])

        message2 = str(content)

        message3 = "小宝贝儿，晚上好啊"

        itchat.send(message1, toUserName=mylover)

        itchat.send(message2, toUserName=mylover)

        itchat.send(message3, toUserName=mylover)

        Timer(10, send_news).start()  # 每隔86400秒发送一次，也就是每天发一次

    except:

        message4 = "每天一次的问候!~~"
        message5 = "随机第"+random.randint(1,99)+"条消息给你"
        itchat.send(message4,message5, toUserName=mylover)


if __name__ == "__main__":
    send_news()
