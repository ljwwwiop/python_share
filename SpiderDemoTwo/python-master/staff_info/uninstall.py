#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'caoy'

from file import file_read
from file import file_write


def uninstall(tablename):
    message = file_read(tablename)
    context = message[1]
    staff_id = input("输入staff_id值：").strip()
    if staff_id.isdigit():
        if 0 < int(staff_id) <= len(context):
            del_info = context[int(staff_id) - 1]
            context.remove(del_info)
            file_write(message, tablename)
            print("\033[31m staff_id: %s删除成功\033[0m" % staff_id)
        else:
            print("\033[41m staff_id超出范围\033[0m")
    else:
        print("\033[41m staff_id字符类型错误\033[0m")