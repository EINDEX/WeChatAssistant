#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from wechat_sdk import WechatBasic

from config import Config, config

wechat = WechatBasic(token=Config.TOKEN[0], appid=Config.APPID[0], appsecret=Config.APPSECRET[0])


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)
    return app
