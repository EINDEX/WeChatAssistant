#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from instance.config import Config
from wechathander import WechatHander

app = Flask(__name__)


# 微信接口
@app.route('/', methods=['GET', 'POST'])
def index():
    config = Config()
    wechat = config.get_wechat()
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
            return WechatHander(openid, request.data.decode('utf-8'), msgsignature=msg_signature, timestamp=timestamp, nonce=nonce).wechat_hander()
        else:
            return WechatHander(openid,request.data).wechat_hander()
    return None


if __name__ == '__main__':
    app.run(debug=True)
