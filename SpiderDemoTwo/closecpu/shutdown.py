'''
    python 远程关机  2个邮箱
    远程密码 xmjnlglbjbiogbee
'''
import smtplib
import poplib
import email
from email.mime.text import MIMEText
from email.header import decode_header
import os
import time

'''
    函数重置邮箱,不然下次打开立马关机
'''
def Rest():
    sent = smtplib.SMTP('smtp.qq.com')
    sent.login('1206957838@qq.com','aiyxf1314')
    content = MIMEText('')
    to = '1206957838@qq.com'
    content['Subject'] = 'reset'
    content['To'] = '1206957838@qq.com'
    content['from'] = '1206957838@qq.com'
    sent.sendmail('1206957838@qq.com',to,content.as_string())
    sent.close()

'''
pop3来读取远程邮箱内容操作
'''
while True:
    host = 'pop.qq.com'
    duyoujian = poplib.POP3_SSL(host)
    duyoujian.user('1206957838@qq.com')
    a = 'xmjnlglbjbiogbee'
    duyoujian.pass_(a)
    total = duyoujian.stat()

    str = duyoujian.top(total[0], 0)
    #    print str
    strr = []
    for x in str[1]:
        try:
            strr.append(x.decode())
        except:
            try:
                strr.append(x.decode('gbk'))
            except:
                strr.append(x.decode('big5'))
    msg = email.message_from_string('\n'.join(strr))
    Titt = email.header.decode_header(msg['subject'])
    # 	 content=decode_header(msg[''])
    #    print Titt

    if Titt[0][1]:
        ttle = Titt[0][0].decode(Titt[0][1])

    else:
        ttle = Titt[0][0]

    #    print ttle
    if ttle == '关机':
        Reset()
        os.system('shutdown -s -t 60')
        print("关机中")



