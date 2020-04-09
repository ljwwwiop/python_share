#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from select import select
from update import update
from change import change
from addition import addition
from uninstall import uninstall

BasePath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BasePath)

while True:
    print("选择方式".center(20, "="))
    print("1.查找、添加\n2.添加\n3.删除")
    choice = input(">>>").strip()
    if choice.isdigit() and 0<int(choice)<=3:
        if int(choice) == 1:
            user_info = input("请输入语句：").strip()
            if user_info.lower().startswith("select "):
                con_info = change(user_info, "select", "from")
                select(con_info[0], con_info[1], con_info[2])
            elif user_info.lower().startswith("update "):
                con_info = change(user_info, "update", "set")
                update(con_info[1], con_info[0], con_info[2])
            else:
                print("语法错误")
        elif int(choice) == 2:
            addition("staff_table")
        else:
            uninstall("staff_table")
    elif choice == "q":
        print("Bye Bye")
        break
    else:
        print("重新选择")

