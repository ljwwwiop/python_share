#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
import socket
import subprocess


class Client(object):
    """
    ftp客户端登录、上传、下载文件
    """
    def __init__(self,address):
        self.address = address    # 包括ip和port的元组
        self.conn = socket.socket()   # socket实例
        self.conn.connect(self.address)  # socket实例要连接的地址

    @staticmethod
    def read_file(filename):    # 读取文件内容
        with open(filename,'r') as fp:
            file_data = fp.read()
        return file_data

    def login(self,message):
        """
        客户端登录认证
        :param message: str形式的用户名，密码
        :return: 返回验证后的状态码
        """
        self.conn.send(message.encode("utf-8"))
        return self.conn.recv(1024).decode()

    def get_data(self,filesize,filename):
        """
        ftp下载文件
        :param filesize: 文件大小
        :param filename: 文件名
        :return: None
        """
        with open(filename,'w+') as fb:
            while filesize > 1024:  # 判断文件大小
                data = self.conn.recv(1024)   # 接收文件内容
                filesize -= len(data)
                fb.write(data.decode())
            if filesize != 0:  # 文件内容没有接收完成
                data = self.conn.recv(1024)
                fb.write(data.decode())

    def put_data(self,filename):
        """
        ftp 上传文件
        :param filename: 文件名
        :return:
        """
        data = self.read_file(filename)   # 读取文件内容
        data_len = len(data)    # 统计文件大小
        print(self.conn.recv(1024).decode())   # 接收命令是否传输成功
        self.conn.send(str(data_len).encode())  # 发送文件大小
        print(self.conn.recv(1024).decode())    # 接收文件大小是否传输成功
        self.conn.sendall(data.encode())    # 传输文件内容
        print(self.conn.recv(1024).decode())   # 接收传输结果

    def cmd_data(self,cmd):
        """
        查询命令，只允许执行lcd、lls、ls命令
        :param cmd: 要执行的命令语句
        :return:
        """
        if "lcd" in cmd:
            dirname = cmd.replace("lcd",'',1).strip()  # 获取文件路径
            os.chdir(dirname)   # 切换至dirname路径
        elif "lls" in cmd:
            subprocess.run(["ls", "-l"])   # 查看本地路径下的文件
        elif "ls" in cmd:    # 查看服务端路径下的文件
            self.conn.send(cmd.encode("utf-8"))   # 发送执行命令
            buffer = self.conn.recv(1024).decode()   #　接收执行结果大小
            self.conn.send("传入字节数成功".encode("utf-8"))
            while int(buffer) > 1024:
                data = self.conn.recv(1024)
                buffer -= len(data)
                print(data)
            data = self.conn.recv(1024).decode()
            print(data)
        else:
            print("\033[41;1m【%s】权限拒绝\033[0m" %cmd)

def main(address):
    """
    主执行函数，调用Client类
    :param address: socket地址
    :return:
    """
    while True:  # 用户认证循环
        ck = Client(address)
        user_pwd = input("用户名,密码:").strip()
        status = ck.login(user_pwd)
        if status == "0":
            print("\033[41;1m用户名或密码错误\033[0m")
            ck.conn.close()
        elif status == "1":
            print("\033[32;1m用户【%s】登录成功\033[0m" %user_pwd.split(",")[0])
            break
    while True: # 循环数据交互
        msg = input(">>>: ").strip()
        if msg == "q": break
        if msg.startswith("put"):  # 判断上传文件
            filename = re.sub(r"[a-z]+",'',msg,count=1).strip()  # 获取文件名
            if not os.path.isfile(filename):   # 判断文件是否存在
                print("\033[41;1m文件不存在\033[0m")   #
                continue
            ck.conn.send(msg.encode("utf-8"))   # 发送执行命令
            ck.put_data(filename)   # 调用put_data函数处理
        elif msg.startswith("get"):   # 判断下载文件
            ck.conn.send(msg.encode("utf-8"))  # 发送执行命令
            buffer_size = ck.conn.recv(1024).decode()  # 执行结果文件大小
            ck.conn.send("传入字节数成功".encode("utf-8"))
            filename = re.sub(r"[a-z]+","",msg,count=1).strip()   # 获取文件名
            if buffer_size == "0":   # 判断是否没有返回值
                print(ck.conn.recv(1024).decode())
                continue
            ck.get_data(int(buffer_size),filename)  # 调用get_data处理下载文件
        else:
            # if msg.startswith("cd ") or msg.startswith("rm "): continue
            ck.cmd_data(msg)  # 命令执行


if __name__ == '__main__':
    args = sys.argv
    if len(args) >= 3:
        IP = args[1]
        port = int(args[2])
        main((IP,port))
    else:
        print("\033[41;1m[Usage]:python %s %s %s\033[0m" %(args[0],args[1],args[2]))

