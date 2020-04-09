#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'caoy'

from file import file_read
from file import file_write


def create(tablename):
    userdate = []
    message = file_read(tablename)
    title = message[0]
    context = message[1]
    staff_id = len(context) + 1
    userdate.append(staff_id)
    for titlename in title[1:]:
        while True:
            info = input("%s:" % titlename).strip()
            if info:
                if titlename == "age" and not info.isdigit():
                    print("%s值不符，请重新输入" % titlename)
                    continue
                elif titlename == "phone":
                    if info.isdigit() and len(info) == 11:
                        if [True for line in context if info in line]:    # info是否存在line中
                            print("phone值冲突")
                            continue
                        else:
                            pass
                    else:
                        print("%s值不符，请重新输入" % titlename)
                        continue

                userdate.append(info)
                break
            else:
                print("\033[31m%s is NULL\033[0m" % titlename)

    context.append(userdate)

    file_write(message, tablename)

    print("用户添加成功")
