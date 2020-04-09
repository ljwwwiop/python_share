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

class Student(object):
    def __init__(self,name,school,address):
        self.name = name
        self.school = school
        self.address = address
        self.grade = []
        self.amount = 0

    def enroll(self):
        #注册
        student_data = File(setting.student_file).file_load()  # 读取student_file数据
        if self.name not in student_data:
            student_data[self.name] = self.__dict__  # 进行注册
            File(setting.student_file).file_dump(student_data)  # 写入student_file文件
        print("\033[32;1m学员【%s】在【%s】学校【%s】分校注册成功\033[0m" %(self.name,self.school,self.address))

    def pay(self):
        # 交费
        amount = input("交费金额:").strip()
        student_data = File(setting.student_file).file_load()  # 读取student_file数据
        if not student_data.get(self.name): student_data[self.name] = self.__dict__  # 如果self.name没有注册，初始化数据
        sum_amount = student_data[self.name]["amount"]   # 以前交费总额
        if amount.isdigit():
            sum_amount += int(amount)   # 加上这次交费，算总额
            student_data[self.name]["amount"] = sum_amount # 加入总额传入student_data中
            File(setting.student_file).file_dump(student_data)  # 写入student_file文件
            self.amount = sum_amount   # 总额数赋值给self.amount
            print("\033[32;1m【%s】总缴费【￥%s】\033[0m" % (self.name, self.amount))
        else:
            print("\033[41;1m【%s】格式错误\033[0m" % amount)

    def select_grade(self):
        # 选择班级
        grade = input("班级:").strip()
        grade_data = File(setting.grade_file).file_load()  # 读取班级数据
        if grade in grade_data:   # 判断班级是否存在
            course = grade_data[grade]["course"]   # 班级对应的课程
            teacher = grade_data[grade]["teacher"]   # 班级对应的讲师
            Grade(grade,teacher,course).add_student(self.name,grade_data)  # 在班级文件内添加学生
            school_data = File(setting.school_file).file_load()  # 读取学校文件内容
            price = school_data[self.school][self.address]["course"][course]["price"]  # 课程对应的价格
            period = school_data[self.school][self.address]["course"][course]["period"]  # 课程对应的周期
            Grade(grade,teacher,course).show_grade()  # 展示班级信息
            Course(course,period,price).show_course()  # 展示课程信息
            student_data = File(setting.student_file).file_load()  # 读取学生文件内容
            student_data[self.name]["grade"].append(grade)   # 学生信息中加入所选班级
            self.grade = student_data[self.name]["grade"]   # 学生加入的班级列表
            File(setting.student_file).file_dump(student_data)  # 学生信息写入文件
            print("\033[32;1m学员【%s】加入了【%s】班级" %(self.name,self.grade))
        else:
            print("\033[41;1m班级【%s】不存在\033[0m" % grade)