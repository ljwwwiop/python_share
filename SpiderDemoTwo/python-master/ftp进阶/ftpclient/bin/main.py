#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
sys.path.append(BASE_DIR)

from core import client

if __name__ == "__main__":
    client.main("localhost",9999)
