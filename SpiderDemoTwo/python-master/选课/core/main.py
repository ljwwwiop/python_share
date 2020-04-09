#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
from school import School
from student import Student
from teacher import Teacher



#初始化school_file文件
if not os.path.isfile(setting.school_file):
    School("老男孩","北京").initializ()
    School("老男孩","上海").initializ()


while True:
    print("""\033[32;1m
    ===== 选课系统 =====
    1. 管理员视图 
    2. 学生视图
    3. 讲师视图
    4. 退出\033[0m""")
    choice = input(">>> ").strip()
    if choice == "1":
        school_name = input("学校:").strip()
        addr = input("地址:").strip()
        S = "School(school_name, addr)"
        while True:
            print("""\033[32;1m
            ===== 管理视图 =====
            \t招聘讲师 add_teacher
            \t创建课程 add_course
            \t创建班级 add_grade
            \t退出 b\033[0m""")
            choice2 = input(">>> ").strip()
            if choice2 == 'b': break
            func = S + '.' + ''.join(choice2) + '()'
            exec(func)
    elif choice == "2":
        name = input("学员:").strip()
        school = input("学校:").strip()
        addr = input("地址:").strip()

        school_data = File(setting.school_file).file_load()
        if school in school_data and addr in school_data[school]:
            print("\033[32;1m【%s】学员进入了【%s】学校【%s】分校\033[0m" % (name, school, addr))
        else:
            print("\033[41;1m学校【%s】或【%s】地址不存在\033[0m" % (school,addr))
            continue

        S = "Student(name,school,addr)"
        while True:
            print("""\033[32;1m
            ===== 学员视图 =====
            \t注册 enroll
            \t交学费 pay
            \t选择班级 select_grade
            \t退出 b\033[0m""")
            choice2 = input(">>> ").strip()
            if choice2 == 'b': break
            func = S + '.' + ''.join(choice2) + '()'
            exec(func)
    elif choice == "3":

        name = input("讲师:").strip()
        school = input("学校:").strip()
        addr = input("地址:").strip()

        school_data = File(setting.school_file).file_load()
        if school not in school_data \
                or addr not in school_data[school] \
                or name not in school_data[school][addr]["teacher"]:
            print("\033[41;1m学校【%s】、地址【%s】或讲师【%s】不存在\033[0m"
                 % (school, addr, name))
            continue
        else:
            grade_list = []
            grade_data = File(setting.grade_file).file_load()
            for k, v in grade_data.items():
                if v["teacher"] == name:
                    grade_list.append(k)
            # print("\033[31;1m【%s】管理的班级:%s\033[0m" % (name, grade_list))

        T = "Teacher(name,school,addr)"
        while True:
            print("""\033[32;1m
                   ===== 讲师视图 =====
                   \t管理班级 manage_grade
                   \t查看学员列表 view_student
                   \t查看学员成绩 get_score
                   \t修改学员成绩 set_score
                   \t退出 b\033[0m""")
            choice2 = input(">>> ").strip()
            if choice2 == 'b': break
            print("\033[31;1m【%s】管理的班级:%s\033[0m" % (name, grade_list))
            grade = input("班级:").strip()
            if grade not in grade_list:
                print("\033[41;1m班级【%s】不在【%s】管理班级内\033[0m" % (grade, name))
                continue
            func = T + '.' + ''.join(choice2) + '(grade)'
            exec(func)

    elif choice == '4':break

    else:
        print("\033[41;1m输入有误,请重新输入\033[0m")
