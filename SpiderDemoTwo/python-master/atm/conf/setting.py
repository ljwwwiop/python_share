#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'caoy'

import os,sys
import logging



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
goods = [
    ('Apple', 7),
    ('Coke', 20),
    ('Milk Tea', 18),
    ('Iphon', 4800),
    ('Mac Proc', 8800)
]

DATABASE = {
    'engine': 'file_storage',
    'name':'accounts',
    'path': "%s/db" % BASE_DIR
}


LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}


TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consumer':{'action':'minus', 'interest':0},
}