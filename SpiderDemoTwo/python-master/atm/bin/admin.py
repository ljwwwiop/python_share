#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASEDIR)

from core import manage

if __name__ == '__main__':
    account_id = input("account id:").strip()
    if account_id.isdigit() and len(account_id) == 4:
        manage.run(account_id)
    else:
        print("\033[33;1mAccount [%s] format is error\033[0m" % account_id)
