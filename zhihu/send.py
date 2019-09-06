import requests

class SendM(object):
    # 发送信息  self 全局变量
    def __init__(self):
        self.url = 'https://www.zhihu.com/api/v4/messages'
        self.data = {
            'content':"hello"
        }
    def Send(self):
        # 查看请求头
        try:
            requests.post(self.url,json=self.data )

            print('ok')
        except:
            pass

