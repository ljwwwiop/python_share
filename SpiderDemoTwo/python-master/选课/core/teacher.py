#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'caoy'


import sys
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASEDIR)
sys.path.append(CORE_DIR)

from conf import setting
from handle_file import File
from course import Course
from grade import Grade

class Teacher(object):
    def __init__(self, name,school,address):
        self.name = name
        self.address = address
        self.school = school

    def manage_grade(self,grade):
        # 管理班级
        grade_data = File(setting.grade_file).file_load()   # 读取grade_file数据
        grade_data[grade]["manager"] = self.name   # 设置管班级manager
        File(setting.grade_file).file_dump(grade_data)   # 写入grade_file
        print("\033[31;1m【%s】管理【%s】班\033[0m" % (self.name,grade))

    def view_student(self,grade):
        # 查看学员列表
        data = File(setting.grade_file).file_load()   # 读取grade_file内容
        print("\033[32;1m%s\033[0m" % data[grade]["student"])  #查看grade_file中的学员

    def get_score(self,grade):
        grade_data = File(setting.grade_file).file_load()  # 读取grade_file内容
        print("\033[33;1m%s\033[0m" % grade_data[grade]["score"])  # 查看grade班级学员成绩

    def set_score(self,grade):
        student_name = input("学员:").strip()
        score = input("成绩:").strip()
        if not 0 <= int(score) <= 100:
            print("\033[41;1mScore[%s]值超出范围\033[0m" % score)
        else:
            grade_data = File(setting.grade_file).file_load()   # 读取班级数据
            if student_name in grade_data[grade]["student"]:   # 查看学员是否在班级内
                grade_data[grade]["score"][student_name] = score  # 修改学员成绩
                File(setting.grade_file).file_dump(grade_data)    # 写入文件
                print("\033[32;1m【%s】班学员【%s】成绩修改为【%s】\033[0m" %(grade,student_name,score))
            else:
                print("\033[41;1m【%s】班学员【%s】不存在\033[0m" % (self.name,student_name))