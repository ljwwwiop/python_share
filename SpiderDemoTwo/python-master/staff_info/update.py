#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handle import handle
from file import file_read
from file import file_write


def update(show_key, table, con_key):

    if table == "" or show_key == "":
        print("update需要输入参数")
    else:
        if "=" in show_key:
            show_list = show_key.strip().split("=")
            if show_list[0].strip() == "staff_id":
                exit("staff_id不允许改动")
            else:
                message = file_read(table)
                title = message[0]
                context = message[1]

                if show_list[0] == "phone":
                    if not show_list[1].isdigit() or len(show_list[1]) != 11 or [True for line in context if show_list[1] in line]:
                        exit("phone键值对冲突")
                    else:
                        pass
                else:
                    pass

                show_index = title.index(show_list[0].strip())
                suit_list = handle(table, con_key)

                for line in suit_list:
                    staff_index = int(line[0]) - 1
                    context[staff_index][show_index] = show_list[1].strip("\",\'")

                print("\033[32mupdate语句执行完成\033[0m")
                print("影响条数：\033[31m%s\033[0m" % len(suit_list))
                file_write(message, table)
        else:
            exit("update语句错误")