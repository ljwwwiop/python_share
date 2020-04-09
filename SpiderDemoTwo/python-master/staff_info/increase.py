#!/usr/bin/env python
# -*- coding: utf-8 -*-


def add(table, values):
    """
    添加一列数据
    :param table: 文件读出来的内容（元组）
    :param values: 要添加的值（字符串）
    :return: 返回table
    """
    title = table[0]
    content = table[1]
    phone_index = title["phone"]
    phone_position = phone_index - 1

    value = list(eval(values))       #字符串转列表
    if len(value) == 5:
        phone = value[phone_position]
        if phone.isdigit():
            if len(phone) == 11:
                for con in content:
                    if con[phone_index] == phone:
                        print("\033[31mPhone 值冲突\033[0m")
                        break
                    else:
                        last_id = str(len(content))
                        value.insert(0, last_id)
                        table[1].append(value)
            else:
                print("\033[31mPhone格式错误\033[0m")
        else:
            print("\033[31mPhone类型错误\033[0m")
    else:
        print("\033[31m输入格式错误\033[0m")

    return table







