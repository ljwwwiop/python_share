#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'caoy'

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import setting
import json


def load_account(account_id):
    account_file = "%s/%s.json" % (setting.DATABASE["path"], account_id)
    with open(account_file) as f:
        account_data = json.load(f)

    return account_data


def dump_account(account_data):
    account_file = "%s/%s.json" % (setting.DATABASE["path"], account_data["id"])
    with open(account_file, 'w') as f:
        json.dump(account_data, f)

    return True
