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
from pprint import pprint

import itchatmp
import requests
import models
import json

from itchatmp.content import TEXT, SAFE, LOCATION

from config import config

itchatmp.update_config(itchatmp.WechatConfig(
    token=config['wechat']['token'],
    appId=config['wechat']['appid'],
    appSecret=config['wechat']['app_secret']))

session = requests.session()


def command(cmd, user):
    c = cmd.split('_')[0]
    t = cmd.split('_')[1:]
    if c == 'name' and len(t) > 0:
        user.name = t[0]
        return f'你的名字设置为: {user.name}'
    elif c == 'help':
        return """使用说明:
        修改名字: \\name_<你的新名字>
        发送地理位置更新你所在的城市
        """
    else:
        return '未知指令'


def user_command(func):
    def weppar(msg):
        db = models.DBSession()
        user = db.query(models.User).filter_by(wechat_id=msg['FromUserName']).first()
        if user:
            if user.name:
                if 'Content' in msg and msg['Content'][0] == '\\':
                    result = command(msg['Content'][1:], user)
                else:
                    result = func(msg, user, db)
            else:
                user.name = msg['Content'].strip()
                result = f'你的名字设置为: {user.name}, 以后需要修改，请发送 \\name_<你的新名字>'
        else:
            user = models.User(wechat_id=msg['FromUserName'])
            db.add(user)
            result = '初次见面，你的名字是？'
        db.commit()
        db.close()
        return result

    return weppar


@itchatmp.msg_register(TEXT)
@user_command
def text_reply(msg, user, *args):
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    params = {
        "perception": {
            "inputText": {
                "text": msg['Content']
            },
            "selfInfo": {

            }
        },
        "userInfo": {
            "apiKey": config['tuling']['key'],
            "userId": user.id
        }
    }
    rmsg = '灵零:'
    if user.city_id:
        params['location'] = {'city': user.city.name}
    try:
        r = requests.post(url, json=params)
        if r.ok:
            data = json.loads(r.content.decode())
            if data['intent']['code'] == 4003:
                rmsg += '今日调戏次数已用尽'
            elif 4000 <= data['intent']['code'] <= 8000:
                rmsg += f'异常错误{data["intent"]["code"]}'
            else:
                flag = False
                for result in data['results']:
                    rmsg = '\n' * flag + result['values'][result['resultType']].replace('#{userName}', user.name)
                    flag = True
        return rmsg
    except:
        return '链接灵零失败'


@itchatmp.msg_register(LOCATION)
@user_command
def location_get(msg, user, db, *args):
    """
    通过 ip 获得所在地理位置并更新到数据库中
    :param msg: 传入的消息
    :return: 文字
    """
    params = {
        'location': f'{msg["Location_X"]},{msg["Location_Y"]}',
        'output': 'json',
        'pois': '1',
        'ak': config['baidu']['ak']
    }
    try:
        r = session.get('http://api.map.baidu.com/geocoder/v2/', params=params)
        if r.ok:
            print(r.text)
            data = json.loads(r.text)
            if data['status'] == 0:
                # success
                # 将位置保存到数据库
                city_name = data['result']['addressComponent']['city'][:-1]
                city = db.query(models.City).filter_by(name=city_name).first()
                if city:
                    user.city_id = city.id
                    return f'成功将您的城市更新为{city_name}'
                return '不支持的城市'
            else:
                # todo save into log
                return '解析地理位置失败'
    except:
        # todo save into log
        return ' 链接 GPS 解析失败'


if __name__ == '__main__':
    # models.Base.metadata.create_all(models.engine)
    itchatmp.run(port=8000)
    print(itchatmp.send('123', config['wechat']['admin']))
