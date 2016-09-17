import requests


class TulingRobot():
    API_URI = 'http://www.tuling123.com/openapi/api'

    def __init__(self, key):
        self.key = key

    def send_message(self, info, user_id=None):
        params = {
            'key': self.key,
            'info': info,
            'userid': user_id
        }
        res_json = requests.get(self.API_URI, params=params).json()
        if res_json['code'] == 100000:
            return res_json['text']
        else:
            return '我会记录此次错误'
