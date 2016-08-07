#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@ Date: 2016-8-6
@ Auther:EINDEX
"""
from instance.config import Config


class WechatHander(object):
    def __init__(self, openid, data, msgsignature=None, timestamp=None, nonce=None):
        self.openid = openid
        self.data = data
        self.wechat = Config().get_wechat()
        if msgsignature is not None:
            pass
        self.wechat.parse_data(self.data, msg_signature=msgsignature, timestamp=timestamp, nonce=nonce)
        self.id = self.wechat.message.id  # 对应于 XML 中的 MsgId
        self.target = self.wechat.message.target  # 对应于 XML 中的 ToUserName
        self.source = self.wechat.message.source  # 对应于 XML 中的 FromUserName
        self.time = self.wechat.message.time  # 对应于 XML 中的 CreateTime
        self.type = self.wechat.message.type  # 对应于 XML 中的 MsgType
        print(self.wechat.message.raw)  # 原始 XML 文本，方便进行其他分析

    def text_hander(self):
        return '文本消息'

    def image_hander(self):
        return '图片消息'

    def voice_hander(self):
        return '声音消息'

    def video_hander(self):
        return '影音消息'

    def location_hander(self):
        return '位置消息'

    def link_hander(self):
        return '链接消息'

    def event_hander(self):
        return '事件消息'

    def type_hander(self):
        if self.type == 'text':
            return self.text_hander()
        elif self.type == 'image':
            return self.image_hander()
        elif self.type == 'voice':
            return self.voice_hander()
        elif self.type == 'vodeo':
            return self.video_hander()
        elif self.type == 'location':
            return self.location_hander()
        elif self.type == 'link':
            return self.link_hander()
        elif self.type == 'event':
            return self.event_hander()
        else:
            return '您触发了个Bug呢'

    def wechat_hander(self):
        message = self.type_hander()
        return self.wechat.response_text(message, escape=False)
