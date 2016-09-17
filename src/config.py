#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# import environ

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # WeChat Config Start
    TOKEN = os.getenv('TOKEN'),
    APPID = os.getenv('APPID'),
    APPSECRET = os.getenv('APPSECRET'),

    # API
    ## HeWeatcher
    HEWEATHER_KEY= os.getenv('HEWEATHER_KEY')
    ## Baddu Geocoding v2
    BAIDU_AK = os.getenv('BAIDU_AK')

    ## Tuling Robot
    TULING_ROBOT = os.getenv('TULING_ROBOT')

    # 关注欢迎语
    WELCOME_TEXT = '欢迎来到 壮哉我大德玛'


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
