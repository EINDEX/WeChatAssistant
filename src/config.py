#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # WeChat Config Start
    TOKEN = os.getenv('TOKEN','EINDEX'),
    APPID = os.getenv('APPID', 'wx26f3489d4e74c850'),
    APPSECRET = os.getenv('APPSECRET', 'dd2367d836fbc84a91fe65b4aef3b6e5'),

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
