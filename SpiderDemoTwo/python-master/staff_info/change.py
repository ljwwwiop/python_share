#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'caoy'


def change(user_info, arg1, arg2, arg3="where"):
    filed = user_info.replace(arg1, "\n").replace(arg1.upper(), "\n")
    if arg2 in filed.lower():
        arg2_pos = filed.lower().find(arg2)
        key1 = filed[:arg2_pos].strip()
        filed = filed[arg2_pos:].replace(arg2, "\n").replace(arg2.upper(), "\n").strip()
        if arg3 in filed:
            where_pos = filed.lower().find(arg3)
            key2 = filed[:where_pos].strip()
            key3 = filed[where_pos:].replace(arg3, "\n").replace(arg3.upper(), "\n").strip()
        else:
            key2 = filed
            key3 = None

        return key1, key2, key3
    else:
        print("%s语法错误" % arg1)
