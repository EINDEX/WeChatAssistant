#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import multiprocessing

bind = '0.0.0.0:5000'

max_requests = 10000
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 60
keepalive = 5
worker_class = 'gevent'

preload = True

x_forwarded_for_header = 'X-FORWARDED-FOR'
