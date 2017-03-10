#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PyCharm : 
Copyright (C) 2016-2017 EINDEX Li

@Author        : EINDEX Li
@File          : config.py
@Created       : 2017/3/9
@Last Modified : 2017/3/9
"""

with open('config.json', 'r') as f:
    import json
    config = json.loads(f.read())
