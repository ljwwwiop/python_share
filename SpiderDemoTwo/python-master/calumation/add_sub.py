#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def add_sub(match_express):
    flag = False
    match_express_find = re.findall(r"[+-]+", match_express)
    if len(match_express_find) == 2:
        match_express = re.sub(r'-', '', match_express, count=1)
        flag = True

    before, after = re.split(r"[+-]+", match_express)

    if flag:
        before = - float(before)

    operator = re.search(r"[+-]+", match_express).group()

    if operator == '+' or operator == '++' or operator == '--':
        compute_value = float(before) + float(after)
    elif operator == '-' or operator == '+-' or operator == '-+':
        compute_value = float(before) - float(after)
    else:
        return

    return str(compute_value)
