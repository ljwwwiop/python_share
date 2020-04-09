#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys

# BASEDIR = os.path.dirname(os.path.dirname(__file__))
# print(BASEDIR)
# sys.path.append(BASEDIR)

from mul_div import mul_div
from add_sub import add_sub


def calum(express):
    express = '(%s)' % express

    while re.search(r'\([^()]+\)', express):
        inner_express = re.search(r'\([^()]+\)', express).group()  # 匹配最里层的括号

        while re.search(r'[-]?\d+(\.\d+)?[*/]+[-]?\d+(\.\d+)?', inner_express):   # 匹配乘除运算
            match_express = re.search(r'[-]?\d+(\.\d+)?[*/]+[-]?\d+(\.\d+)?', inner_express).group()   # 匹配乘除运算式

            match_value = mul_div(match_express)     # 乘除运算

            if re.search(r'[-]\d+(\.\d+)?[*/]+[-]?\d+(\.\d+)?', match_express):  # match_express中第一个[-]

                # 匹配字符默认在替换字符前加[+]
                inner_express = re.sub(r'[-]?\d+(\.\d+)?[*/]+[-]?\d+(\.\d+)?', '+%s' % match_value,
                                       inner_express, count=1)

            else:
                # 替换运算结果到inner_express
                inner_express = re.sub(r'[-]?\d+(\.\d+)?[*/]+[-]?\d+(\.\d+)?', match_value,
                                       inner_express, count=1)
            inner_express = re.sub(r"[+]+", '+', inner_express)
            inner_express = re.sub(r'[+][-]|[-][+]', '-', inner_express)

        while re.search(r'[-]?\d+(\.\d+)?[+-]+[-]?\d+(\.\d+)?', inner_express):  # 匹配加减运算
            match_express = re.search(r'[-]?\d+(\.\d+)?[+-]+[-]?\d+(\.\d+)?', inner_express).group()  # 匹配加减运算式

            match_value = add_sub(match_express)    # 加减运算

            if not match_value: exit("\033[31;1m运算出现错误,退出\033[0m")

            # 替换匹配字符得到的运算结果
            inner_express = re.sub(r'[-]?\d+(\.\d+)?[+-]+[-]?\d+(\.\d+)?', match_value, inner_express,
                                   count=1)
        inner_express = inner_express.strip("(,)")  # 去掉匹配字符的()
        express = re.sub(r'\([^()]+\)', inner_express, express, count=1)  # 把去掉()的结果替换到express中

    # 无法循环后返回express
    return express


def run():
    print("\033[33;1m========== 计算器 =============\033[0m")
    expression = input(">>> ").strip()
    print("\033[33;1m========== 开始 =============\n\033[0m")

    expression = re.sub(r'\s+', '', expression)  # 去掉空格

    expression_list = set(re.split(r'[()*/+-]', expression))   # 取数值生成集合（去重）

    for value in expression_list:    # 循环结果
        if not re.search(r'^\d+([.]\d+)?$', value) and value != '':   # 不匹配整数或浮点数的 并且 value不为空
            exit("\033[31;1mExpression [%s] is error\033[0m" % expression)

    result = calum(expression)   # 调用calum函数

    if re.search(r'[+]', result):
        result = re.sub(r'[+]', '', result)

    print(result)

