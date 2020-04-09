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

class School(object):
    # 学校地址
    def __init__(self,school,address):
        self.school = school
        self.address = address
        self.grade = []
        self.teacher = []
        self.course = {}

    def initializ(self):
        school_data = File(setting.school_file).file_load()
        if not school_data.get(self.school): school_data[self.school] = {}
        school_data[self.school][self.address] = self.__dict__
        File(setting.school_file).file_dump(school_data)

    def add_teacher(self):
        teacher = input("讲师:").strip()
        school_data = File(setting.school_file).file_load()  # 读取 school_file 文件内容
        if teacher not in school_data[self.school][self.address]["teacher"]:
            school_data[self.school][self.address]["teacher"].append(teacher)
            self.teacher = school_data[self.school][self.address]["teacher"]
            File(setting.school_file).file_dump(school_data)
            print("\033[32;1m讲师【%s】加入【%s】学校【%s】分校\033[0m" %(teacher,self.school,self.address))
        else:
            print("\033[41;1m讲师【%s】已经存在【%s】学校【%s】分校\033[0m" %(teacher,self.school,self.address))

    def add_course(self):
        course = input("课程:").strip()
        period = input("周期:").strip()
        price = input("价格:").strip()
        school_data = File(setting.school_file).file_load()  # 读取school_file文件
        course_data = school_data[self.school][self.address]["course"]   # 读取课程数据
        if course not in course_data:  # 判断course不存在
            course_data[course] = Course(course,period,price).__dict__ # 添加cours信息
            # self.course = course_data  # 添加到self.course中
            File(setting.school_file).file_dump(school_data)  # 写入school_file文件
            print("\033[32;1m课程【%s】在【%s】学校【%s】分校创建成功\033[0m"
                  %(course,self.school,self.address))
        else:
            print("\033[41;1m【%s】课程已经存在\033[0m" %course)

    def add_grade(self):
        grade = input("班级:").strip()
        teacher = input("讲师:").strip()
        course = input("课程:").strip()

        school_data = File(setting.school_file).file_load()   #读取school_file文件内容
        #判断grade不存在，并且course与teacher都存在
        if grade not in school_data[self.school][self.address]["grade"] \
                and course in school_data[self.school][self.address]["course"] \
                and teacher in school_data[self.school][self.address]["teacher"]:
            school_data[self.school][self.address]["grade"].append(grade)   # 新建grade班级
            # self.grade = school_data[self.school][self.address]["grade"]   # 添加到self.grade
            grade_data = File(setting.grade_file).file_load()   # 读取grade_file文件
            grade_data[grade] = Grade(grade,teacher,course).__dict__    # 初始化grade在grade_file中的值
            File(setting.grade_file).file_dump(grade_data)   # 写入grade_file文件
            File(setting.school_file).file_dump(school_data)    # 写入school_file文件
            print("\033[32;1m【%s】学校【%s】分校成功创建【%s】班级\033[0m" %(self.school,self.address,grade))
        else:
            print("\033[41;1m班级【%s】已经存在或课程【%s】不存在\033[0m" %(grade,course))