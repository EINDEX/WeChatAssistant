#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@ Date: 2016-8-6
@ Auther: EINDEX
"""
from wechat_sdk.messages import TextMessage, EventMessage, LocationMessage, VoiceMessage, ImageMessage, VideoMessage, \
    ShortVideoMessage, LinkMessage, UnknownMessage

from app import wechat
from config import Config


class WechatHander():
    def __init__(self, openid, data, timestamp=None):
        """

        :param openid:
        :param data:
        :param timestamp:
        """
        self.openid = openid
        self.data = data
        wechat.parse_data(self.data)
        self.message = wechat.message
        self.id = self.message.id  # 对应于 XML 中的 MsgId
        self.target = self.message.target  # 对应于 XML 中的 ToUserName
        self.source = self.message.source  # 对应于 XML 中的 FromUserName
        self.time = self.message.time  # 对应于 XML 中的 CreateTime
        self.type = self.message.type  # 对应于 XML 中的 MsgType
        self.row = self.message.raw  # 原始 XML 文本，方便进行其他分析

    def text_handler(self, content):
        from app.main.api import tuling_robot_api
        return tuling_robot_api.send_message(info=content)

    def image_handler(self, picurl):
        return '抱歉 我还没有拥有眼睛'

    def voice_handler(self, recognition):
        from app.main.api import tuling_robot_api
        return tuling_robot_api.send_message(info=recognition)

    def video_handler(self, media_id, thumb_midea_id):
        return '影音消息'

    def location_handler(self, location, label):
        from .api import baidu_geo_coding_api,he_weather_api
        location_json = baidu_geo_coding_api.geo_decoding(location_lat=location[0],location_lng=location[1])
        return he_weather_api.get_weather(city_name=location_json['addressComponent']['city'][:-1])

    def link_handler(self, title, description, url):
        return '链接消息'

    def event_handler(self, type, key=None, ticket=None):
        if type == 'subscribe':
            if key is not None and ticket is not None:
                pass
            return Config.WELCOME_TEXT
        elif type == 'unsubscribe':
            pass

    def type_handler(self):
        if isinstance(self.message, TextMessage):
            content = self.message.content
            return self.text_handler(content)

        elif isinstance(self.message, ImageMessage):
            picurl = self.message.picurl
            return self.image_handler(picurl)

        elif isinstance(self.message, VoiceMessage):
            recognition = self.message.recognition
            return self.voice_handler(recognition)

        elif isinstance(self.message, VideoMessage) or isinstance(self.message, ShortVideoMessage):
            media_id = self.message.media_id
            thumb_midea_id = self.message.thumb_media_id
            return self.video_handler(media_id, thumb_midea_id)

        elif isinstance(self.message, LocationMessage):
            location = self.message.location
            label = self.message.label
            return self.location_handler(location, label)

        elif isinstance(self.message, LinkMessage):
            title = self.message.title
            description = self.message.description
            url = self.message.url
            return self.link_handler(title, description, url)

        elif isinstance(self.message, EventMessage):
            type = self.message.type
            key = self.message.key
            ticket = self.message.ticket
            return self.event_handler(type, key=key, ticket=ticket)

        elif isinstance(self.message, UnknownMessage):
            return self.message.type

    def wechat_handler(self):
        response = self.type_handler()
        return wechat.response_text(response, escape=False)
