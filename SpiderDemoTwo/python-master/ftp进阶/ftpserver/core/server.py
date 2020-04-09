#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import socketserver
import json
import subprocess
import hashlib


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = "%s/db" % BASE_DIR


class FtpServer(socketserver.BaseRequestHandler):
    def __init__(self,request, client_address, server):
        super(FtpServer,self).__init__(request, client_address, server)
        self.user = None
        self.home = None
        self.current_dir = None
        self.user_dic = None
        self.user_file = None

    def login(self):
        """用户认证"""
        try:
            status = "401"
            self.user,pwd = self.request.recv(1024).decode().split(",") # 接收用户名密码
            self.home = "%s/data/%s" %(DB_DIR,self.user)  # 家目录
            self.current_dir = self.home   # 当前目录
            self.user_file = "%s/%s.json" %(DB_DIR,self.user) # 用户验证文件
            if os.path.isfile(self.user_file):
                with open(self.user_file,"r") as f:
                    self.user_dic = json.load(f)
                    if pwd == self.user_dic["password"]:
                        status = "200"
        except Exception as e:
            print("出错了:",e)
        finally:
            print("status:",status)
            self.request.send(status.encode())
            return status

    def handle(self):
        """服务端交互函数"""
        status = self.login()  # login
        print(self.current_dir)
        while status != "401":  # 验证通过
            msg_dic = json.loads(self.request.recv(1024)) # 接收命令dict
            action = msg_dic["action"]  # 执行的方法
            if hasattr(self,action):  # 判断是否存在
                func = getattr(self,action)  # 调用方法
                func(msg_dic)
            else:
                self.request.send("503".encode())

    def put(self,msg_dic):
        """上传文件"""
        filename = os.path.join(self.current_dir,msg_dic["filename"]) # 文件路径拼接
        size = msg_dic["size"]  # 文件大小
        quota = self.user_dic["quota"]   # 默认以M为单位
        quota_size = int(quota.replace("M","")) * 1024 *1024  # 配额大小
        use_size = self.dir_size()  # 已经使用的磁盘大小
        quota_size -= use_size  # 剩下的配额大小

        recv_size = 0
        if filename in self.user_dic["freeze"]["put"] and os.path.isfile(filename): # 有断点记录,并且文件存在
            recv_size = os.stat(filename).st_size # 已接收的文件大小
            fp = open(filename,"ab")  # 文件为追加模式
        else:
            fp = open(filename,"wb+")  # 文件为直接写
        if quota_size > size-recv_size:  # 配额大小 > 文件需要传输的大小
            status_size = "201" + "," + str(recv_size) # 状态 + 接收的文件大小
            self.request.send(status_size.encode())  # 发送
            print("【%s】开始上传文件" % filename)
            fp.seek(recv_size)    # 指针跳转
            print("seek:",fp.tell())  # 指针位置
            m = hashlib.md5()  # 加密
            while recv_size < int(size): # 接收的文件大小 < 文件总大小
                data = self.request.recv(1024)  # 接收数据
                m.update(data)  # 加密数据
                if not data:  # 客户端中断
                    self.user_dic["freeze"]["put"].append(filename) # 加入断点记录
                    self.user_dic["freeze"]["put"] = list(set(self.user_dic["freeze"]["put"])) # 去重
                    print("user_dic:",self.user_dic)
                    fp.close()
                    break
                recv_size += len(data)
                fp.write(data)
            else: # 正常结束
                fp.close()
                #print(m.hexdigest())
                if filename in self.user_dic["freeze"]["put"]: # filename在断点记录中
                    self.user_dic["freeze"]["put"].remove(filename)  # 删除filename文件
                print("\033[32;1m文件上传成功\033[0m")
                self.request.send(m.hexdigest().encode())  # 发送md5值与客户端比对

            print(self.user_dic)
            with open(self.user_file, "w") as f:  # 写入文件
                json.dump(self.user_dic, f)
        else:  # 超出配额大小
            status_size = "503" + "," + "0"
            self.request.send(status_size.encode())

    def get(self,msg_dic):
        """下载文件"""
        status = "404"
        filename = os.path.join(self.current_dir,msg_dic["filename"]) #路径拼接
        if os.path.isfile(filename):  # 文件存在
            if filename in self.user_dic["freeze"]["get"]: # 文件在断点中
                status = "203"
            else:  # 文件不在断点中
                status = "200"
            filesize = os.stat(filename).st_size   # 文件大小
            status_filesize = status + "," + str(filesize)
            self.request.send(status_filesize.encode())  # 发送状态与文件大小
            client_recv_size = self.request.recv(1024).decode() # 接收客户端返回的已接收大小

            m2 = hashlib.md5()  # 加密
            with open(filename,"rb") as fp:
                fp.seek(int(client_recv_size))  # 指针跳转
                for line in fp:
                    try:
                        self.request.send(line)  # 发送数据
                        m2.update(line) # 加密数据
                    except Exception as e:  # 判断是否断掉
                        print("下载中断:",e)
                        self.user_dic["freeze"]["get"].append(filename) # 添加断点纪录
                        self.user_dic["freeze"]["get"] = list(set(self.user_dic["freeze"]["get"]))  # 去重
                        fp.close()
                        break
                else:
                    print(m2.hexdigest())
                    if filename in self.user_dic["freeze"]["get"]:   # 判断filename是否存在
                        self.user_dic["freeze"]["get"].remove(filename) # 去除filename
                    print("【%s】文件传送完成" % filename)
                    client_md5 = self.request.recv(1024).decode()  # 接收客户端md5值
                    if m2.hexdigest() == client_md5:
                        server_status = "204"
                    else:
                        server_status = "603"
                    self.request.send(server_status.encode())  # 返回比对结果

            print(self.user_dic)
            with open(self.user_file, "w") as f:  # 写入文件
                json.dump(self.user_dic, f)

        else:
            status_filesize = status + "," + "0"  # 文件不存在
            self.request.send(status_filesize.encode())

    def ls(self,msg_dic):
        """查看文件"""
        status = "404"
        msg = "cd %s &&" % self.current_dir + msg_dic["cmd"]  # 路径拼接
        result = subprocess.getstatusoutput(msg)  # 执行
        if result[0] == 0: status = "200"  # 执行状态
        result_msg = status + ',' + str(len(result[1])) # 执行状态与返回结果大小
        self.request.send(result_msg.encode())  # 发送
        print(self.request.recv(1024).decode())  # 确认客户端是否收到
        self.request.send(result[1].encode())  # 返回执行结果

    def cd(self,msg_dic):
        """切换目录"""
        cd_dir = msg_dic["cmd"][1]  # 要切换的目录
        status = "403"
        if not cd_dir.startswith("/"):  # 不是以/开头
            cd_dir_list = cd_dir.split("/")  # 转列表
            for i in cd_dir_list: # 循环列表中的目录
                if i == "..":
                    current_dir_temp = os.path.dirname(self.current_dir) # 切换到上一级
                elif i == '.':
                    current_dir_temp = self.current_dir  # 当前目录不动
                else:
                    current_dir_temp = os.path.join(self.current_dir,i) # 路径拼接
                
                if self.home in current_dir_temp and os.path.isdir(current_dir_temp): # 判断未超出家目录并且切换的目录存在
                    self.current_dir = current_dir_temp
                    status = "200"
                elif self.home in current_dir_temp and not os.path.isdir(current_dir_temp): # 切换的目录不存大
                    status = "404"
                    break
                else:
                    break
        print("\033[32;1mcurrent_dir: %s\033[0m" % self.current_dir)  # 当前目录
        self.request.send(status.encode()) # 发送执行状态

    def dir_size(self):
        """统计目录下的使用大小"""
        size = 0
        for root, dirs, files in os.walk(self.home):  # 循环目录下的所有子目录和文件
            size += sum([os.path.getsize(os.path.join(root,name)) for name in files]) # 大小值垒加 
        return size


#if __name__ == '__main__':
def main(ip,port):
    sk = socketserver.ThreadingTCPServer((ip,port),FtpServer)
    #sk = socketserver.TCPServer(("0.0.0.0",9999),FtpServer)
    sk.serve_forever()

