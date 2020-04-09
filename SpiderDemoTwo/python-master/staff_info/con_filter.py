#!/usr/bin/env python
# -*- coding: utf-8 -*-


def con_content(table, match_variable):
    """
    查找出匹配条件的内容
    :param table: 列表形式的内容
    :param match_variable: 匹配条件
    :return: 返回匹配到的内容
    """
    title = table[0]    # 目录行
    content = table[1]   # 内容
    if match_variable:   # 匹配传入的条件
        operator = ["<", ">", "=", "like"]
        for index, ope in enumerate(operator):
            if ope in match_variable:   # 查找匹配的条件
                staff = []
                match_variable_list = match_variable.split(ope)  # 将条件转为列表
                variable = match_variable_list[0].strip()   # 提取条件中的变量1
                value = match_variable_list[1].strip()     # 提取条件中的变量2
                staff_index = title.index(variable)   # 通过变量1找出所在列表的位置

                for staff_info in content:    # 内容进行循环
                    if index == 3 and value in staff_info[staff_index]:  # like 语句
                        staff.append(staff_info)
                    else:
                        con_result = "%s %s %s" % (staff_info[staff_index], ope, value)  # 将变量1中的数据取出形成字符串
                        if eval(con_result):  # 转为可执行语句
                            staff.append(staff_info)
                break

    else:
        staff = content

    return staff
