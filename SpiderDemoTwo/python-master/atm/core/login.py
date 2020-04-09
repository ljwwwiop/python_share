#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'caoy'

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import setting
import json
import time


def acc_auth(user, password):
    db_path = setting.DATABASE["path"]
    account_file = "%s/%s.json"  % (db_path, user)
    if os.path.isfile(account_file):
        with open(account_file, 'r') as f:
            account_data = json.load(f)
            if account_data["password"] == password:
                expire_date = time.mktime(time.strptime(account_data["expire_date"],"%Y-%m-%d"))
                if expire_date > time.time() and account_data['status'] == 0:
                    return account_data
                print("\033[1;41mAccount [%s] Can not be used, please contact the administrator\033[0m" % user)
            else:
                print("\033[31mAccount ID or Password is incorrent\033[0m")
    else:
        print("\033[31mAccount %s is not exist\033[0m" % user)


def acc_login(user_data,log_obj):
    """
    account login mode
    :param user_data: {"account_id": None, "is_auth": False, "acc_data": None}
    :param log_obj: log mode
    :return: auth：db中记录的数据
    """
    retry_count = 0
    while not user_data["is_authenticated"] and retry_count < 3:
        username = input("\033[31musername:\033[0m").strip()
        password = input("\033[31mpassword:\033[0m").strip()
        auth = acc_auth(username, password)
        if auth:
            user_data['account_id'] = username
            user_data['is_authenticated'] = True
            return auth
        else:
            retry_count += 1
    else:
        log_obj.error("account [%s] too many login attempts" % username)
        exit()
