#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handle import handle
from file import file_read
import os


def select(show_key,table,con_key):

    if table == "" or show_key == "":
        print("select需要输入参数")
    else:
        title = file_read(table)[0]
        suit_list = handle(table, con_key)
        if show_key == "*":
            show_key = ''
            for key in title:
                if show_key == '':
                    show_key = key
                else:
                    show_key = '%s,%s' % (show_key, key)
        else:
            pass

        if suit_list:
            show_list = show_key.strip().split(",")
            for line in suit_list:
                for show_name in show_list:
                    name_index = title.index(show_name.strip())
                    print(line[name_index], end = "\t")
                print()
        print("查询到的条数：%s" % len(suit_list))

	
