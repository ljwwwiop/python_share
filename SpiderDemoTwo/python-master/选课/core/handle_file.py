#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'caoy'

import pickle
import json
import os


class File(object):
    def __init__(self,filename):
        self.filename = filename

    def file_load(self,r_pro='rb'):
        if os.path.isfile(self.filename):
            with open(self.filename,r_pro) as fp:
                data = pickle.load(fp)
                # data = json.load(fp)
        else:
            data = {}

        return data

    def file_dump(self,data,w_pro='wb+'):
        with open(self.filename,w_pro) as fp:
            pickle.dump(data,fp)
            # json.dump(data,fp)
            fp.flush()