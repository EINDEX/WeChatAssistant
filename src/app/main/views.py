#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import request, render_template

from app import wechat
from app.main import main
from app.main.wechathander import WechatHander


@main.route('/')
def index():
    return render_template('index.html')


# 微信接口
@main.route('/wechat', methods=['GET', 'POST'])
def wechat_route():
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    msg_signature = request.args.get('msg_signature')
    nonce = request.args.get('nonce')
    if request.method == 'GET':
        if wechat.check_signature(signature, timestamp, nonce):
            return request.args.get('echostr')
    elif request.method == 'POST':
        openid = request.args.get('openid')
        if msg_signature is not None:
            return WechatHander(openid, request.data.decode('utf-8'), msgsignature=msg_signature, timestamp=timestamp,
                                nonce=nonce).wechat_handler()
        else:
            return WechatHander(openid, request.data).wechat_handler()
    return None
