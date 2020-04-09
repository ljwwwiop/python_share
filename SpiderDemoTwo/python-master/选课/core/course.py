#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'caoy'

import sys
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASEDIR)
sys.path.append(CORE_DIR)


class Course(object):
    # 创建课程
    def __init__(self,course,period,price):
        self.course = course
        self.period = period
        self.price = price

    def show_course(self):
        # 查看课程信息
        print("\033[31;1m课程:【%s】\t价格:【￥%s】\t周期:【%s个月】\033[0m"
              %(self.course,self.price,self.period))
