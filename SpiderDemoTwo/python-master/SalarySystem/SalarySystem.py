#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: Caoy


def file_format(file):
    """
    格式化处理工资文件
    :param file: 工资文件
    :return: 以字典的格式返回
    """
    staff_info = {}
    with open(file, "r") as f:
        for line in f:
            line = line.split(" ")
            staff_info[line[0]] = line[1].strip()
    return staff_info


def file_write(file, info):
    """
    退出之前将字典格式重新写入工资文件中
    :param file: 工资文件
    :param info: 工资文件的字典格式(修改后的)
    :return:
    """
    with open(file, 'w+') as fp:
        for name, salary in info.items():
            fp.write("%s %s\n" % (name, salary))


def select(info):
    """
    工资查询
    :param info: 工资文件的字典格式
    :return: 返回工资的字典格式
    """
    name = input("请输入要查询的员工姓名（例如：Alex）：").strip()
    if info.get(name):
        print("\033[33m%s\033[0m的工资是：\033[31m%s\033[0m" % (name, info[name]))
    else:
        print("\033[41m%s不存在,请确认后重新输入\033[0m" % name)
    return info


def change(info):
    """
    修改员工工资
    :param info: 工资字典格式
    :return: 返回工资(字典)
    """
    name_salary = input("请输入要修改的员工姓名和工资，用空格分隔（例如：Alex 10）：").strip()
    if len(name_salary.split(" ")) == 2:
        name = name_salary.split(" ")[0]
        salary = name_salary.split(" ")[1]
        if salary.isdigit() and info.get(name):
            info[name] = salary
            print("\033[32m修改成功\033[0m")
        else:
            print("\033[41m输入格式错误,请重新输入\033[0m")
    else:
        print("\033[41m输入格式有误,请重新输入\033[0m")
    return info


def add(info):
    """
    添加员工姓名与工资
    :param info: 工资字典格式
    :return: 返回工资(字典)
    """
    name_salary = input("请输入要增加的员工姓名和工资，用空格分割（例如：Eric 100000）：").strip()
    if len(name_salary.split(" ")) == 2:
        name = name_salary.split(" ")[0]
        salary = name_salary.split(" ")[1]
        if info.get(name):
            print("\033[41m%s用户已经存在,请确认是否修改工资\033[0m" % name)
        else:
            if salary.isdigit():
                info[name] = salary
                print("\033[32m添加成功\033[0m")
            else:
                print("\033[41m工资格式输入有误,添加失败\033[0m")
    else:
        print("\033[41m输入格式有误,请重新输入\033[0m")
    return info


filename = 'info.txt'
choices = [
    ("查询员工工资", select),
    ("修改员工工资", change),
    ("增加新员工记录", add),
    ("退出", file_write)
]
if __name__ == "__main__":
    FileContent = file_format(filename)
    while True:
        for sequence, choice in enumerate(choices):
            sequence += 1
            print(sequence, choice[0])

        UserChoice = input(">>:")

        if UserChoice.isdigit():
            index = int(UserChoice) - 1
            if UserChoice == "4":
                FileContent = choices[index][1](filename, FileContent)
                print("\033[33m再见\033[0m")
                break
            FileContent = choices[index][1](FileContent)
        else:
            print("\033[41m输入有误,请重新输入\033[0m")



