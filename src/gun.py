#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import gevent.monkey

gevent.monkey.patch_all()

import multiprocessing

bind = '0.0.0.0:5000'
pidfile = 'log/gunicorn.pid'
logfile = 'log/debug.log'

workers = multiprocessing.cpu_count() * 2 + 1
workers_class = 'gunicorn.workers.ggevent.GeventWorker'

x_forwarded_for_header = 'X-FORWARDED-FOR'

