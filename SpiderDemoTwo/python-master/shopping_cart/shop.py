#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: caoy

import json
import time
import os
import getpass

now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

goods = [
    ('Apple', 7),
    ('Coke', 20),
    ('Milk Tea', 18),
    ('Iphon', 4800),
    ('Mac Proc', 8800)
]

ShopList = []

if not os.path.isfile('RecordLog'):
    os.mknod('RecordLog')	

for i in range(3):
    user = input("Username:")
    pwd = getpass.getpass("Password:")

    with open('RecordLog', 'r+') as f:
        record_file = f.read()
        if record_file:
            record_log = json.loads(record_file)
        else:
            record_log = {}

    if user not in record_log:
        while True:
            salary = input("输入你的工资:")
            if salary.isdigit():
                salary = int(salary)
                record_log[user] = {
                    'password': pwd,
                    'balance': salary,
                    'record': []
                }
                break
            else:
                print("\033[41m工资只能为数字,请重新输入\033[0m")
        break
    else:
        if pwd == record_log[user]['password']:
            index_last = len(record_log[user]['record']) - 1
            recently = record_log[user]['record'][index_last]
            salary = record_log[user]['balance']
            print("\033[32m最后一次购买商品记录[%s],所剩余额[%s]\033[0m" % (recently, salary))
            break
        else:
            print("\033[41m用户名或密码错误\033[0m")
else:
    print("错误次数太多。。退出程序")
    exit(0)



while True:
    for index,product in enumerate(goods):
        print(index, goods[index])

    choice = input("请输入你选择的商品:")
    if choice.isdigit() and int(choice) < len(goods):
        choice = int(choice)
        if salary > goods[choice][1]:
            salary -= goods[choice][1]
            print("\033[41m添加[%s]进入购物车\033[0m" % goods[choice][0])
            ShopList.append(goods[choice])
        else:
            print("\033[31m当前余额不足\033[0m")
    elif choice == 'q':
        print("当前购物车商品\033[34m%s\033[0m,当前余额\033[34m[%s]\033[0m" % (ShopList, salary))
        if ShopList:
            record_last = '%s %s'  % (now_time, ShopList)
            record_log[user]['balance'] = salary
            record_log[user]['record'].append(record_last)

            with open('RecordLog', 'w+') as fp:
                fp.write(json.dumps(record_log))
        break

    elif choice == 's':
        old_record = record_log[user]['record']
        for record in old_record:
            print("\033[33m%s\033[0m" % record)

    else:
        print("\033[41m输入的商品[%s]不存在\033[0m" % choice)













