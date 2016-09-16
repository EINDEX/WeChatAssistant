#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import gevent.monkey

gevent.monkey.patch_all()

import multiprocessing

bind = '0.0.0.0:5000'

workers = 1
workers_class = 'gevent'
timeout = 120
keepalive = 2

preload = True

x_forwarded_for_header = 'X-FORWARDED-FOR'

