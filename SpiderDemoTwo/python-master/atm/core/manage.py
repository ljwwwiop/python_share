#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from conf import setting
from core import account
from core import logger
import random
import datetime

access = logger.logger('access')


def add_account(account_id, log_obj=access, high_limit=15000, status=0, password="abc", pay_day=22):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    expire_date = (datetime.datetime.now() + datetime.timedelta(days=365*5)).strftime("%Y-%m-%d")
    file_list = os.listdir(setting.DATABASE['path'])
    user_list = []
    for file in file_list:
        if file.endswith(".json"):
            user = file.strip(".json")
            user_list.append(user)
    # while True:
    #     user_id = ''
    #     for i in range(0, 4):
    #         str_id = random.randint(0, 9)
    #         user_id += str(str_id)
    #     if user_id in user_list: continue
    #     break
    if account_id in user_list:
        print("\033[33mAccount [%s] has exist\033[0m" % account_id)
    else:
        user_info = {
            "password": password,
            "id": account_id,
            "expire_date": expire_date,
            "balance": high_limit,
            "enroll_date": today,
            "status": status,
            "credit": high_limit,
            "pay_day": pay_day
        }
        user_status = account.dump_account(user_info)

        if user_status:
            log_obj.info("\033[31m [%s] credit card is Success\033[0m" % account_id)
        else:
            log_obj.error("\033[31m [%s] credit card is Failed\033[0m" % account_id)
    print()


def limit(account_id, log_obj=access):
    account_file = "%s/%s.json" % (setting.DATABASE['path'], account_id)
    if os.path.isfile(account_file):
        account_data = account.load_account(account_id)
        current_account_limit = account_data['credit']
        current_account_balance = account_data['balance']
        while True:
            change_account_limit = input("\033[32;1m[%s] current credit limit [%s], change credit limit:\033[0m"
                                         % (account_id, current_account_limit))
            if change_account_limit.isdigit() and len(change_account_limit) > 0:
                account_data['credit'] = change_account_limit
                plus_account_limit = float(change_account_limit) - float(current_account_limit)
                current_account_balance = float(current_account_balance) + float(plus_account_limit)
                account_data['balance'] = current_account_balance

                user_status = account.dump_account(account_data)
                if user_status:
                    log_obj.info("[%s] credit card limit [%s]" % (account_id, change_account_limit))
                    break
            elif change_account_limit == 'b': break
    else:
        print("\033[41mUnable to change,[%s] is not exist\033[0m")

    print()


def freeze(account_id, log_obj=access):
    account_file = "%s/%s.json" % (setting.DATABASE['path'], account_id)
    if os.path.isfile(account_file):
        account_data = account.load_account(account_id)
        account_data['status'] = 1
        account.dump_account(account_data)
        log_obj.info("[%s] credit card is locked, please contact administrator" % account_id)
    else:
        print("\033[41mUnable to lock,[%s] is not exist\033[0m")

    print()


def unfreeze(account_id, log_obj=access):
    account_file = "%s/%s.json" % (setting.DATABASE['path'], account_id)
    if os.path.isfile(account_file):
        account_data = account.load_account(account_id)
        if account_data['status'] == 2:
            print("\033[33;1mCan not unfreeze,account [%s] is disable\033[0m" % account_id)
        else:
            account_data['status'] = 0
            account.dump_account(account_data)
            log_obj.info("Unfreeze success,account [%s] can be used normally" % account_id)
    else:
        print("\033[41mUnable to unfreeze,[%s] is not exist\033[0m")

    print()


def run(account_id):
    menu = u'''
       ------- Administrator ---------
       \033[32;1m1.  添加账户
       2.  用户额度
       3.  冻结账户
       4.  解冻账户
       \033[0m'''
    menu_dic = {
        '1': add_account,
        '2': limit,
        '3': freeze,
        '4': unfreeze
    }
    flag = True
    while flag:
        print(menu)
        choice = input(">>> ").strip()
        if choice.isdigit() and choice in menu_dic:
            menu_dic[choice](account_id)
        elif choice == 'b':
            flag = False
