#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Auth: caoy

import json,getpass

err_dict = {}


with open("passwd","r+") as f:
    pwd_dict = json.loads(f.read())

with open("lockfile",'r+') as fp:
    lock_user = fp.read().split('\n')


while True:
    user = input("username:")
    if user == '':
        print("Username can not be empty, please re-enter")
        continue
    # pwd = getpass.getpass("password:")
    pwd = input("password:")

    if user in lock_user:
        print("%s has been locked" %user)
        break
    #判断用户名密码是否正确
    if user in pwd_dict and pwd_dict[user] == pwd:
        print("Welcom to Python...")
        break
    else:
        if user in err_dict:
            err_dict[user] += 1
            if err_dict[user] > 2:
                print("%s is prohibited...." %user)
                with open("lockfile",'a+') as fp:
                    fp.write(user)
                    fp.write('\n')
                    break
            else:
                print("username or password is error...")
        else:
            err_dict[user] = 1
            print("username or password is error...")


