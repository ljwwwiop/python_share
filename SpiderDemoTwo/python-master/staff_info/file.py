#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def file_read(filename):
    """
    文件转为列表
    :param filename: 读取的文件
    :return: 列表： 1.文件标题  2. 文件数据
    """
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            data = []
            count = 0
            for line in f:
                count += 1
                if count == 1:
                    title = line.strip().split("\t")
                    continue
                line = line.strip().split("\t")
                data.append(line)
        return title, data
    else:
        exit("%s文件不存在" % filename)


def file_write(table, tablename):
    title = table[0]
    context = table[1]
    context.insert(0,title)
    with open(tablename, "w+") as fp:
        for line in context:
            for name in line:
                fp.write("%s\t" % name)
            fp.write("\n")













