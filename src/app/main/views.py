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
@main.route('/wechat', methods=['POST'])
def wechat_route():
    """

    :return:
    """
    timestamp = request.args.get('timestamp')
    openid = request.args.get('openid')
    wechat.parse_data(data=request.data)
    return WechatHander(openid, request.data,timestamp=timestamp).wechat_handler()


@main.route('/wechat', methods=['GET'])
def wechat_check():
    """

    :return:
    """
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    if wechat.check_signature(signature, timestamp, nonce):
        return request.args.get('echostr')
