#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'caoy'
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import setting
from core import account
from core import login
import json


def trans(log_obj, auth_data, tran_type, amount):
    amount = float(amount)

    if tran_type in setting.TRANSACTION_TYPE:
        interest = amount * setting.TRANSACTION_TYPE[tran_type]["interest"]
        old_balance = auth_data["balance"]

        if setting.TRANSACTION_TYPE[tran_type]["action"] == "plus":
            new_balance = old_balance + amount + interest

        elif setting.TRANSACTION_TYPE[tran_type]["action"] == "minus":
            new_balance = old_balance - amount - interest
            if new_balance < 0:
                print('''\033[31;1mYour credit [%s] is not enough for this transaction [-%s], your current balance is
                                [%s]''' % (auth_data['credit'], (amount + interest), old_balance))
                return

        auth_data["balance"] = new_balance
        account.dump_account(auth_data)
        log_obj.info("account:%s   action:%s    amount:%s   interest:%s" %
                     (auth_data['id'], tran_type, amount, interest))
        return auth_data

    else:
        print("\033[31;1mTransaction type [%s] is not exist!\033[0m" % tran_type)