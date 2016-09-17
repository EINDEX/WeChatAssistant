#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import gevent.monkey

gevent.monkey.patch_all()

import multiprocessing

bind = '0.0.0.0:5000'

max_requests = 10000
workers = 1
timeout = 120
keepalive = 5
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

preload = True

x_forwarded_for_header = 'X-FORWARDED-FOR'

