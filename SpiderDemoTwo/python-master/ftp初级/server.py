#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import socket
import json
import subprocess
import sys


BASEDIR = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(BASEDIR,'db','auth')


class Ftp(object):
    """
    ftp服务端
    """
    def __init__(self):
        self.conn = None
        self.home = None
        self.status = 0

    @staticmethod
    def read_file(filename):
        """
        获取文件内容
        :param filename:
        :return:
        """
        with open(filename, 'r') as fp:
            file_data = json.load(fp)
        return file_data

    def login(self,conn,username,password):
        """
        服务端登录认证接口
        :param conn: socket连接
        :param username: 用户名
        :param password: 命令
        :return: 状态码
        """
        self.conn = conn
        db = self.read_file(db_file)   # auth文件读取出的数据
        if username in db and password == db[username]:
            self.home = "%s/db/%s" %(BASEDIR,username)   # self.home目录路径
            if not os.path.isdir(self.home): os.mkdir(self.home)    # 如果没有self.home目录,创建
            os.chdir(self.home)   # 切换到对应的home目录
            self.status = 1  # 成功设置status = 1
        return self.status

    def recv_data(self,filesize,filename):
        """
        处理put命令
        :param filesize:
        :param filename:
        :return:
        """
        with open(filename,'w+') as fb:
            while filesize > 1024:
                data = self.conn.recv(1024)
                filesize -= len(data)
                fb.write(data.decode())
            if filesize != 0:
                data = self.conn.recv(1024)
                fb.write(data.decode())

    def send_data(self,cmd):
        """
        处理查询命令与get命令
        :param cmd: 要执行的命令
        :return:
        """
        data_local = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE, shell=True)
        server_data = data_local.stdout.read()   # 正常输出
        server_stderr = data_local.stderr.read()  # 错误输出
        #if not server_data and not server_stderr:
        #    server_data = "返回值为空".encode("utf-8")
        if not server_data and server_stderr:   # 执行出错时
            server_data = server_stderr   # 将错误发送给客户端
            data_len = 0   # 设置字节数为0，避免get命令时将错误写入文件中
        else:
            data_len = len(server_data)

        self.conn.send(str(data_len).encode("utf-8"))   # 发送字节长度
        print("\033[32;1m%s\033[0m" % self.conn.recv(1024).decode())
        self.conn.sendall(server_data)  # 发送执行结果


def main(address):
    """
    ftp服务端主执行函数，调用Ftp类
    :param address: bind的地址
    :return:
    """
    ftp = Ftp()
    sk = socket.socket()
    sk.bind(address)
    sk.listen(5)

    while True:
        print("等待连接....")
        ftp.conn = None  # 断开连接后重新初始化
        ftp.status = 0
        conn,addr = sk.accept()
        print("新连接",addr)
        if ftp.status == 0:   # 判断是否登录
            user,pwd = tuple(conn.recv(1024).decode().split(","))  # 用户名，密码
            status = ftp.login(conn,user,pwd)  # 登录状态
            conn.send(str(status).encode("utf-8"))  # 发送验证后的状态码
        while ftp.status:  # 如果验证通过进入循环
            cmd = conn.recv(1024).decode()  # 接收命令行数据
            if not cmd: break  # cmd为空，退出循环，等待新的连接
            if cmd.startswith("get"):  # 判断是否为下载文件
                cmd = re.sub(r"[a-z]+",'cat',cmd,count=1).strip()  # 将get转为cat执行
            if cmd.startswith("put"):  # 是否为上传文件
                conn.send("准备上传文件".encode('utf-8'))  # 发送消息
                buffersize = conn.recv(1024).decode()   # 接收文件内容大小
                conn.send("字节数传送成功".encode("utf-8"))
                filename = re.sub(r"[a-z]+",'',cmd,count=1).strip()  # 文件名
                ftp.recv_data(int(buffersize),filename)  # 调用recv_data函数处理
                conn.send("文件接收成功".encode("utf-8"))
            else:
                ftp.send_data(cmd)    # get/命令查询


if __name__ == "__main__":
    main(address=("localhost",21))
