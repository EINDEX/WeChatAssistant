#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@ Date: 2016-8-6
@ Auther:EINDEX
"""
from app import wechat


class WechatHander(object):
    def __init__(self, openid, data, msgsignature=None, timestamp=None, nonce=None):
        self.openid = openid
        self.data = data
        self.wechat = wechat
        if msgsignature is not None:
            pass
        self.wechat.parse_data(self.data, msg_signature=msgsignature, timestamp=timestamp, nonce=nonce)
        self.id = self.wechat.message.id  # 对应于 XML 中的 MsgId
        self.target = self.wechat.message.target  # 对应于 XML 中的 ToUserName
        self.source = self.wechat.message.source  # 对应于 XML 中的 FromUserName
        self.time = self.wechat.message.time  # 对应于 XML 中的 CreateTime
        self.type = self.wechat.message.type  # 对应于 XML 中的 MsgType
        print(self.wechat.message.raw)  # 原始 XML 文本，方便进行其他分析

    def text_handler(self):
        return '文本消息'

    def image_handler(self):
        return '图片消息'

    def voice_handler(self):
        return '声音消息'

    def video_handler(self):
        return '影音消息'

    def location_handler(self):
        return '位置消息'

    def link_handler(self):
        return '链接消息'

    def event_handler(self):
        return '事件消息'

    def type_handler(self):
        if self.type == 'text':
            return self.text_handler()
        elif self.type == 'image':
            return self.image_handler()
        elif self.type == 'voice':
            return self.voice_handler()
        elif self.type == 'vodeo':
            return self.video_handler()
        elif self.type == 'location':
            return self.location_handler()
        elif self.type == 'link':
            return self.link_handler()
        elif self.type == 'event':
            return self.event_handler()
        else:
            return '暂不支持'

    def wechat_handler(self):
        message = self.type_handler()
        return self.wechat.response_text(message, escape=False)
