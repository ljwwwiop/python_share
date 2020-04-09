#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def mul_div(match_express):

    before, after = re.split(r"[*/]+", match_express)
    operator = re.search(r"[*/]+", match_express).group()

    if operator == '/':
        compute_value = float(before) / float(after)
    elif operator == '*':
        compute_value = float(before) * float(after)
    else:
        exit("\033[31;1mIt could not be higher operation\033[0m")

    return str(compute_value)
