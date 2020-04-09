# IP check，将可用的IP重新保存到IP
import requests
def IPCheck():
    IP = []
    SuccessIP = []
    # 读取文件
    with open('kdl_proxy_one.txt','r') as f:
        for line in f:
            IP.append(line[:-1])
    # request模块使用代理
    for ip in IP:
        http = 'http://'+str(ip)
        proxies = {
            "http": http
        }
        time.sleep(10)
        try:
            r = requests.get("http://www.baidu.com", proxies=proxies,timeout=3)
        except:
            print(str(ip)+'---connect failed')
        else:
            SuccessIP.append(ip)
            print(str(ip)+'---success')
    # 重新保存
    n=0
    f=open('IP.txt','w')
    for ip in SuccessIP:
        f.write(ip+'\n')
        n+=1
    f.close()
    print('Total are '+str(n)+' successful IP')
