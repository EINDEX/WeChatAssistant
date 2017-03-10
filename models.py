#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PyCharm : 
Copyright (C) 2016-2017 EINDEX Li

@Author        : EINDEX Li
@File          : models.py
@Created       : 2017/3/9
@Last Modified : 2017/3/9
"""
import datetime
import config
from sqlalchemy import DateTime, Column, Integer, String, create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    wechat_id = Column(String(30), unique=True)
    city_id = Column(String(11), ForeignKey('citys.id'))  # 使用和风天气代码
    weather_time = Column(DateTime(), default=datetime.datetime.now().replace(hour=9, minute=0, second=0))

    city = relationship('City', lazy='joined', cascade='all')


class City(Base):
    __tablename__ = 'citys'

    id = Column(String(11), primary_key=True)
    name = Column(String(100))


engine = create_engine(config.config['config']['db'], connect_args={'charset': 'utf8'}, echo=True)
DBSession = sessionmaker(bind=engine)
