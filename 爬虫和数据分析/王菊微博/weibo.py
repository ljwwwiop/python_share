'''
    抓取王菊的微博评论
    并且进行数据可视化分析
'''
import requests
import json
import pandas as pd
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
           "cookies":"_T_WM=e97e0ff8d8ca0b8db1d1b44259a322ff; SCF=Al0ww0UF7vuGoeTQPLU05-0gkGu80qB4mlazwxVvWRXShGY6gH3ZqCeP45A801npCKWch9_W1yPwFrGesRRN-oU.; SUB=_2A25xHlTaDeRhGeNN7VYS-SfKwjiIHXVS4XySrDV6PUJbkdAKLVOhkW1NSbUgun6WuXa84HnNlNa7rd_vuCdZfHH3; SUHB=0BLoNIQNOQL_Hp; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E7%258E%258B%25E8%258F%258A%26uicode%3D10000011%26fid%3D1076031773294041%26oid%3D4325175199813394"
           }


# 存放 weibo_id的
comment_parameter = []
# 存放weibo_url的
comment_url = []

url = 'https://m.weibo.cn/api/container/getIndex?uid=1773294041&luicode=10000011&lfid=100103type%3D1%26q%3D%E7%8E%8B%E8%8F%8A&\featurecode=20000320&type=uid&value=1773294041&containerid=1076031773294041'
c_r = requests.get(url)
for i in range(2,11):
    c_parameter = (json.loads(c_r.text)["data"]["cards"][i]["mblog"]["id"])
    # 提取出来后，每个存入链表
    comment_parameter.append(c_parameter)

# 获取每个评论的url
c_url_base = 'https://m.weibo.cn/api/comments/show?id='
for parameter in comment_parameter:
    for page in range(1,101): # 知道总页数 直接抓取到总页数结束时候
        c_url = c_url_base+str(parameter)+"&page=" + str(page)
        comment_url.append(c_url)


# 存放评论
comment = []
# 存放用户id
user_id = []
for url in comment_url:
    u_c_r = requests.get(url)
    try:
        for m in range(0,9): # 每个url 包含了9条用户信息
            one_id = json.loads(u_c_r.text)["data"]["data"][m]["user"]["id"]
            user_id.append(one_id)
            print(one_id)
            one_comment = json.loads(u_c_r.text)["data"]["data"][m]["text"]
            comment.append(one_comment)
            print(one_comment)
    except:
        pass

# 获取用户信息
containerid = []
user_base_url = "https://m.weibo.cn/api/container/getIndex?type=uid&value="
for id in set(user_id):#需要对user_id去重
    containerid_url = user_base_url + str(id)
    try:
        con_r = requests.get(containerid_url)
        one_containerid = json.loads(con_r.text)["data"]['tabsInfo']['tabs'][0]["containerid"]
        containerid.append(one_containerid)
    except:
        containerid.append(0)
print("全部获取完成，正在写入文件")

#这里需要设置headers以及cookie模拟登陆
feature = []#存放用户基本信息
id_lose = []#存放请求失败id
headers={
    'Cookie': 'SINAGLOBAL=4955113080777.212.1541779260756; SCF=AtVY6nop_PnCNRe-KD-dhECpqs8KTRtLqtpbOwnAVEN29mmxFi18ez3HLs1By19g6nxX4lAjjNJwIVxAzs9biNo.; SUHB=0sqBafC42Mn-a7; UOR=www.zhongshikaoyan.com,widget.weibo.com,www.baidu.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhpcXm4MJ0eO88fdSfO.a6y5JpX5oz75NHD95Qfe0qXe0.4So.XWs4Dqcj6i--fiKyWi-27i--ciKLhi-8Wi--fiK.7iKLFi--Xi-iWiKnci--ciKyFiKn4i--ciKyFiKLhi--ciKn4iK.R; ALF=1547803896; SUB=_2A25xHn-mDeRhGeNN7VYS-SfKwjiIHXVS4QHurDV8PUJbkNAKLUTEkW1NSbUguplNBGNqmv7OVRcOuJsGvy_21mOK; Ugrow-G0=56862bac2f6bf97368b95873bc687eef; wvr=6; YF-V5-G0=c948c7abbe2dbb5da556924587966312; YF-Page-G0=091b90e49b7b3ab2860004fba404a078; wb_view_log_5364399694=1366*7681; _s_tentry=-; Apache=571248322355.1001.1545840566811; ULV=1545840566865:10:8:1:571248322355.1001.1545840566811:1545142803281',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
m = 1
for num in zip(user_id,containerid):
    url = "https://m.weibo.cn/api/container/getIndex?uid="+str(num[0])+"&luicode=10000011&lfid=100103type%3D1%26q%3D&featurecode=20000320&type=uid&value="+str(num[0])+"&containerid="+str(num[1])
    print(url)
    try:
        r = requests.get(url,headers = headers)
        feature.append(json.loads(r.text)["data"]["cards"][1]["card_group"][1]["item_content"].split("  "))
        # print(json.loads(r.text)["data"]["cards"][1]["card_group"][1]["item_content"].split("  "))
        print("成功第{}条".format(m))
        m = m + 1
        time.sleep(1)#设置睡眠一秒钟，防止被封
    except:
        id_lose.append(num[0])

#将featrue建立成DataFrame结构便于后续分析
fans = pd.DataFrame(comment,columns=['评论'])
fans.to_csv('comments.csv',index=False,mode='a+',encoding='utf-8_sig')
user_info = pd.DataFrame(feature,columns = ["性别","年龄","星座","国家城市"])
user_info.to_csv('userInfo.csv',index=False,mode='a+',encoding='utf-8_sig')
print("保存写入完成")


