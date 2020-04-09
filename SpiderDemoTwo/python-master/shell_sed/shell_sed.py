#!/usr/bin/env python
# -*- coding: utf-8 -*-
 #__author__ = 'caoy'

import os
import sys
import datetime

now_time = datetime.datetime.now()
bak_time = now_time.strftime("%Y-%m-%d_%H:%M:%S")
path_file = os.path.dirname(os.path.abspath("__file__"))

if len(sys.argv) == 3:
    OldStr = sys.argv[1].strip()
    NewStr = sys.argv[2].strip()

    with open('Sing','r+',encoding='utf-8') as f ,\
            open('NewSing','w+') as fp:
        for line in f:
            if OldStr in line:
                line = line.replace(OldStr, NewStr)
                fp.write(line)
                continue
            fp.write(line)

    os.rename(os.path.join(path_file,'Sing'),os.path.join(path_file,'Sing_bak%s') % bak_time)
    os.rename(os.path.join(path_file,'NewSing'),os.path.join(path_file,'Sing'))

else:
    print("py用法: python %s [oldstr] [newstr]" %sys.argv[0])


