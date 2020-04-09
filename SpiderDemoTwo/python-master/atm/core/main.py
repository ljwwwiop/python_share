#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'caoy'


'''
main program handle module , handle all the user interaction stuff

'''

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import login
from core import logger
from core import account
from core import trans
from conf import setting
from core import shoping
import os
import re

#transaction logger
trans_logger = logger.logger('transaction')   # transaction = transaction.log
#access logger
access_logger = logger.logger('access')    # access = access.log


#temp account data ,only saves the data in memory
user_data = {
    'account_id':None,     # 账户
    'is_authenticated':False,   # 认证状态
    'account_data':None    # 账户数据
}


def auth(func):
    def wapper(*args, **kwargs):
        if not user_data["is_authenticated"]:
            acc_data = login.acc_login(user_data, access_logger)
            if user_data['is_authenticated']:
                user_data['account_data'] = acc_data
        return func(*args, **kwargs)
    return wapper


@auth
def repay(acc_data):
    '''
    print current balance and let user repay the bill
    :return:
    '''
    account_data = account.load_account(acc_data['account_id'])

    current_balance= ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' % (account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
        if len(repay_amount) >0 and repay_amount.isdigit():
            new_balance = trans.trans(trans_logger,account_data,'repay', repay_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
                back_flag = True
        elif repay_amount == 'b':
            back_flag = True
        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)


@auth
def withdraw(acc_data):
    '''
    print current balance and let user do the withdraw action
    :param acc_data:
    :return:
    '''
    account_data = account.load_account(acc_data['account_id'])
    current_balance= ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
        if len(withdraw_amount) >0 and withdraw_amount.isdigit():
            new_balance = trans.trans(trans_logger,account_data,'withdraw', withdraw_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' %(new_balance['balance']))
                back_flag = True
        elif withdraw_amount == 'b':
            back_flag = True
        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)


@auth
def transfer(acc_data):
    account_data = account.load_account(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        trans_account = input("\033[33;1mInput trans account:\033[0m").strip()
        trans_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
        if len(trans_amount) > 0 and trans_amount.isdigit() \
                and len(trans_account) == 4 and trans_account.isdigit():
            db_file = "%s/%s.json" % (setting.DATABASE['path'], trans_account)
            if os.path.isfile(db_file):
                new_balance = trans.trans(trans_logger, account_data, 'transfer', trans_amount)
                if new_balance:
                    trans_account_data = account.load_account(trans_account)
                    trans_account_balance = trans.trans(trans_logger, trans_account_data, 'repay', trans_amount)
                    print("\033[31m [%s] Transfer successful\033[0m" % trans_account)
                    print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
                    back_flag = True
        elif trans_amount == 'b' or trans_account == 'b':
            back_flag = True
        else:
            print('\033[31;1mA valid amount[%s] or account[%s], only accept integer!\033[0m' % (trans_amount, trans_account))


@auth
def account_info(acc_data):
    print(acc_data)


@auth
def pay_check(acc_data):
    log_file = "%s/log/%s" % (BASE_DIR, "transactions.log")
    while True:
        pay_check_date = input("Check pay date(2017-01):").strip()
        if not re.match('[0-9]{4}-(0[0-9]|1[0-2])', pay_check_date): continue

        with open(log_file) as f:
            for line in f:
                log_account = "account:%s"  %acc_data["account_id"]
                if log_account in line and pay_check_date in line:
                    print(line)
        break

@auth
def shopping(acc_data):
    account_data = account.load_account(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    while True:
        goods_amount = shoping.shop(setting.goods)
        new_balance = trans.trans(trans_logger, account_data, 'consumer', goods_amount)
        if new_balance:
            print('''\033[42;1mShopping Success, New balance:%s\033[0m''' % (new_balance['balance']))
            break


def logout(acc_data):
    exit("Bye Bye!")


@auth
def interactive(acc_data):
    '''
    interact with user
    :return:
    '''
    menu = u'''
    ------- Oldboy Bank ---------
    \033[32;1m1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  购物
    7.  退出
    \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': shopping,
        '7': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)

        else:
            print("\033[31;1mOption does not exist!\033[0m")


def run():
    interactive(user_data)
