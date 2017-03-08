#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PyCharm : 
Copyright (C) 2016-2017 EINDEX Li

@Author        : EINDEX Li
@File          : wechat_assistant.py
@Created       : 2017/3/8
@Last Modified : 2017/3/8
"""
import itchatmp

from itchatmp.content import TEXT


@itchatmp.msg_register(TEXT)
def text_reply(msg):
    return msg['Content']


if __name__ == '__main__':
    with open('config.json', 'r') as f:
        import json

        config = json.loads(f.read())

        itchatmp.update_config(itchatmp.WechatConfig(
            token=config['wechat']['token'],
            appId=config['wechat']['appid'],
            appSecret=config['wechat']['app_secret']))
    itchatmp.run()
