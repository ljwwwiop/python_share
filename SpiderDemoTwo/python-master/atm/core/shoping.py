#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'caoy'


import json
import time
import os
import getpass


def shop(goods):
    ShopList = []
    goods_amount = 0
    while True:
        for index,product in enumerate(goods):
            print(index, goods[index])

        choice = input("请输入你选择的商品:")
        if choice.isdigit() and int(choice) < len(goods):
            choice = int(choice)
            goods_amount += goods[choice][1]
            print("\033[41m添加[%s]进入购物车\033[0m" % goods[choice][0])
            ShopList.append(goods[choice])
        elif choice == 'q':
            if ShopList:
                print("当前购物车商品\033[34m%s\033[0m,需支付\033[34m[%s]\033[0m" % (ShopList, goods_amount))
                return goods_amount
            break

        else:
            print("\033[41m输入的商品[%s]不存在\033[0m" % choice)

