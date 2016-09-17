#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
