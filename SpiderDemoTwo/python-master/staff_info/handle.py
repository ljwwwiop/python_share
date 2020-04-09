#!/usr/bin/env python
# -*- coding: utf-8 -*-

from file import file_read
import re


def handle(table, con_key):
    message = file_read(table)
    title = message[0]
    context = message[1]
    suit_list = []
    if con_key:
        for var_value in ["age","staff_id","phone"]:
            if var_value in con_key:   # var_value 是否在con_key中
                var_index = title.index(var_value)  # var_value的位置
                key = var_value
                for line in context:  # line 文件内容循环
                    re_index = re.search(key, con_key).span()  # 查key在con_key中的位置
                    con_key_last = con_key[re_index[1]:].strip()   # 排除key后剩余值
                    key = line[var_index]  # key在line中的值
                    if "=" in con_key_last:
                        new_key_last = con_key_last.replace("=", "").strip()
                        con_key = "%s==%s" % (key, new_key_last)
                    else:
                        con_key = "%s%s" % (key, con_key_last)

                    if eval(con_key):
                        suit_list.append(line)
                break
        else:
            if "=" in con_key and "!" in con_key:
                contrast = "!="
            elif "=" in con_key and "!" not in con_key:
                contrast = "="
            elif "like" in con_key:
                contrast = "like"
            else:
                exit("条件无法判断")

            con_list = con_key.split(contrast)

            if len(con_list) == 2:
                key_index = title.index(con_list[0].strip())
                for line in context:
                    con_list[0] = line[key_index]
                    key = con_list[0].strip()
                    con_key_last = con_list[1].strip("\",\', ,\n")
                    if contrast == "like":
                        if con_key_last in key:
                            suit_list.append(line)
                    elif contrast == "=":
                        if key == con_key_last:
                            suit_list.append(line)
                    else:
                        if key != con_key_last:
                            suit_list.append(line)
            else:
                print("语句错误")

    else:
        suit_list = context

    return suit_list
