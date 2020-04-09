#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

BASEDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASEDIR)

from calum import run


if __name__ == '__main__':
    while True:
            run()
