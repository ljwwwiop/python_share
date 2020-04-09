#!/usr/bin/env python
# -*- coding: utf-8 -*-


def delete_con(table, filter_con):
    if filter_con == table[1]:
        print("\033[31m禁止删除整张表格\033[0m")
    else:
        for con in filter_con:
            table[1].remove(con)
            print("%s 删除成功" % con)

    return table
