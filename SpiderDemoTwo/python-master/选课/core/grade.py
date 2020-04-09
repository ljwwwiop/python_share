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



class Grade(object):
    # 创建班级
    def __init__(self,grade,teacher,course):
        self.grade = grade
        self.teacher = teacher
        self.course = course
        self.student = []
        self.score = {}
        self.manager = None

    def add_student(self,student_name,grade_dict):   # 添加学生进入对应班级
        if not grade_dict.get(self.grade): grade_dict[self.grade] = self.__dict__   # 不存在，初始化self.grade班级
        if student_name not in grade_dict[self.grade]["student"]:  # 判断 student_name 不在没有加入过该班级
            self.student = grade_dict[self.grade]["student"].append(student_name)  # 添加student_name学生
            File(setting.grade_file).file_dump(grade_dict)   # 写入grade_file文件
            print("\033[32;1m【%s】添加成功\033[0m" % student_name)
        else:
            print("\033[41;1m【%s】已存在\033[0m" % student_name)

    def show_grade(self):
        print("\033[31;1m班级:【%s】\t课程:【%s】\t讲师:【%s】\033[0m"
              % (self.grade, self.course, self.teacher))