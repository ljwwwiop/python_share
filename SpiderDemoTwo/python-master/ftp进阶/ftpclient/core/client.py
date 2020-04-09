#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import os
import sys
import json
import hashlib
import subprocess
import getpass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings


class FtpClient(object):
    def __init__(self, ip, port):
        self.ck = socket.socket()
        self.ck.connect((ip, port))  
        self.status = 0              # 登陆状态

    def login(self):
        """
        用户登陆认证模块
        """
        if not self.status:   # 0为未登陆,1为登陆
            user = input("username: ").strip()    
            password = getpass.getpass("password: ").strip()
            m = hashlib.md5()  # md5加密
            m.update(password.encode())   #加密密码
            user_pwd = user + ',' + m.hexdigest()  #用户名,密码合并
            #print(user_pwd)
            self.ck.send(user_pwd.encode())   # 发送用户名密码
            return self.ck.recv(1024).decode()  # 返回认证状态值

    def help(self):
        """
        用法说明模块
        """ 
        message = """
            ls  # 查看服务端文件
            cd  # 切换服务端目录 
            get # 下载文件
            put # 上传文件
            lls # 查看本机客户端文件
            lcd # 切换客户端目录
        """
        print(message)

    def str_list(self, msg):
        """
        字符转为列表
        """
        msg_list = msg.split()  # 切割字符
        for i in msg_list:  
            if len(i) == 0: msg_list.remove(i) # 去除列表中的空字符
        return msg_list 

    def interactive(self):
        """
        用户交互模块
        """
        self.status = self.login() # 验证是否登陆
        print("\033[31;1m%s\033[0m" % settings.code_status[self.status])
        while self.status != "401":
            msg = input("ftp:> ").strip()
            if len(msg) == 0: continue
            if msg == "exit": break
            msg_list = self.str_list(msg)   # 转入命令转列表
            cmd = "cmd_" + msg_list[0]   # 字符拼接
            if hasattr(self, cmd):   # 查看是否有cmd方法
                func = getattr(self, cmd)  # 调用cmd方法
                func(msg_list)   # 执行cmd方法
            else:
                self.help()   # 调用说明
                print("\033[41;1m[%s]方法不存在\033[0m" % msg_list[0])

    def cmd_get(self, msg_list):
        """文件下载"""
        if len(msg_list) >= 2:     # 列表长度
            filename = msg_list[1]   # 文件名
            get_dic = {
                "action": "get",
                "filename": filename,
            }
            self.ck.send(json.dumps(get_dic).encode())   # 转为字符发送
            status,filesize = self.ck.recv(1024).decode().split(",")   # 接收服务端状态与文件大小

            if status != "404":   # 服务端有这样的文件
                recv_size = 0
                if status == "200":   # 没有断点记录
                    fp = open(filename, "wb+")
                elif status == "203" and os.path.isfile(filename):  # 有断点记录并且客户端文件存在
                    fp = open(filename,"ab")   # 断点续传
                    print("fp: ab")
                    recv_size = os.stat(filename).st_size  # 已接收文件大小
                    print("recv_size:",recv_size)
                    fp.seek(recv_size)   # 指针跳转
                    print("fp.tell:", fp.tell()) 

                elif status == "203" and not os.path.isfile(filename):  # 有断点记录,但客户端没有文件存在
                    fp = open(filename,"wb+")

                print("\033[32;1m\t\t[文件开始下载]\033[0m",end="\t")
                agv_value = int((int(filesize)-recv_size)/20)+1       # 文件大上分成20份
                generator = (agv_value * i for i in range(1,20))      # 把循环变成一个生成器
                iter_data = generator.__next__() # 初始化执行生成器一次

                self.ck.send(str(recv_size).encode())   # 把上次接收到的数据告诉服务端
                m2 = hashlib.md5()   # md5 验证
                while recv_size < int(filesize):   # 接收大小 < 总大小 
                    data = self.ck.recv(1024)     # 接收数据
                    fp.write(data)    # 写入文件
                    m2.update(data)  # md5值
                    recv_size += len(data)
                    iter_data = self.pro_bars(generator,iter_data,filesize,recv_size) # 进度条
                else:
                    print(m2.hexdigest())
                    print("【%s】文件下载完毕" % filename)
                    self.ck.send(m2.hexdigest().encode())  # 发送md5值
                    server_status = self.ck.recv(1024).decode()  # 接收服务端比对结果
                    print(settings.code_status[server_status])
            else:
                print(settings.code_status[status])  # 没有这个文件
        else:
            print("\033[41;1mget方法使用错误\033[0m")

    def cmd_put(self, msg_list):
        """上传文件"""
        if len(msg_list) >= 2:
            filename = msg_list[1]  # 文件名
            if os.path.isfile(filename):
                file_size = os.stat(filename).st_size  # 文件大小
                put_dic = {
                    "action": "put",
                    "size": file_size,
                    "filename": filename
                }
                self.ck.send(json.dumps(put_dic).encode())  # 发送put_dic
                recv_status,recv_size = self.ck.recv(1024).decode().split(",")  # 接收状态,已经接收的文件大小
                print(recv_status)

                if recv_status == "201":   # 服务端状态
                    file_size -= int(recv_size)   # 要传输的文件大小
                    print("\033[32;1m\t\t[文件开始上传]\033[0m",end="\t")
                    agv_value = int(int(file_size)/20) + 1  # 平均值,用于进度条计算
                    generator = (agv_value * i for i in range(1,20))  # 生成器
                    iter_data = generator.__next__()  # 执行一次
                    with open(filename, 'rb') as fp:  
                        send_size = 0
                        fp.seek(int(recv_size))  # 指针跳转
                        m = hashlib.md5()   # 加密
                        for line in fp:
                            self.ck.send(line)  # 发送数据
                            m.update(line)
                            send_size += len(line)
                            iter_data = self.pro_bars(generator,iter_data,file_size,send_size) # 进度条
                        else:
                            server_md5 = self.ck.recv(1024).decode()  # 接收md5
                            if m.hexdigest() == server_md5:
                                print(settings.code_status["205"])
                            else:
                                print(settings.code_status["603"])
                else:
                    print(settings.code_status[recv_status])
            else:
                print(settings.code_status["404"])
        else:
            print("\033[41;1mput方法使用错误\033[0m")

    def cmd_cd(self, msg_list):
        """服务端目录切换"""
        cd_dic = {
            "action": "cd",
            "cmd": msg_list
        }
        if len(msg_list) >= 2:
            self.ck.send(json.dumps(cd_dic).encode()) # 发送cd_dic
            status = self.ck.recv(1024).decode()  # 返回执行状态
            print(settings.code_status[status])
        else:
            pass

    def cmd_ls(self, msg_list):
        """服务端文件查看"""
        msg = ''
        for i in msg_list: msg = msg + ' ' + i
        ls_dic = {
            "action": "ls",
            "cmd": msg,
        }
        self.ck.send(json.dumps(ls_dic).encode())  # 发送ls_dic
        cmd_status, cmd_size = self.ck.recv(1024).decode().split(',')  # 执行状态,与结果大小
        self.ck.send("准备接收数据...".encode())
        if cmd_status == "200":
            recv_size = 0
            while recv_size < int(cmd_size): # 接收数据大小 < 结果大小
                data = self.ck.recv(1024).decode()  # 接收数据
                recv_size += len(data)
                print(data)
        else:
            print(settings.code_status[cmd_status])

    def cmd_lls(self,msg_list):
        """
        本地文件查看
        """
        action = msg_list[0].replace("l","",1).strip() # 本地lls命令--> ls
        msg_list[0] = action  # 列表第一个值替换
        subprocess.run(msg_list)  # 执行结果
        
    def cmd_lcd(self,msg_list):  
        """
        本地文件目录切换
        """
        if len(msg_list) == 1:  
            pass
        elif len(msg_list) >= 2:
            current_dir = os.getcwd()  # 当前目录
            chang_dir = os.path.join(current_dir,msg_list[1])  # 拼接要切换的目录
            if os.path.isdir(chang_dir):  # 判断目录是否存在
                os.chdir(chang_dir)  # 切换目录
                print("\033[32;1m目录切换成功\033[0m")
            else:
                print("\033[41;1m目录不存在\033[0m")

    def pro_bars(self, generator,iter_data,file_size,send_size):
        """
        进度条函数
        generator: 生成器
        iter_data: 生成器生成的值
        file_size: 总文件大小
        send_size: 发送/接收的文件大小
        """
        if send_size > iter_data: # 发送或接收的数据大小 > 生成器当前值
            try:
                iter_data = generator.__next__()  # 执行生成器
                sys.stdout.write("# ")
            except StopIteration as e:
                iter_data = int(file_size)    # 生成器执行结束,最后一次 
                sys.stdout.write("\033[32;1m   [success] \033[0m")
                print()
            finally:
                sys.stdout.flush()

        return iter_data
            


#if __name__ == '__main__':
def main(ip,port):
    FtpClient(ip,port).interactive()

