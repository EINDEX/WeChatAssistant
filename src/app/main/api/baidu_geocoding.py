import requests


class BaiduGeoCoding():
    """
    Baidu GeoCoding API
    """
    API_URL = 'http://api.map.baidu.com/geocoder/v2/'

    def __init__(self, ak):
        """
        set ak_key
        :param ak: ak_key
        """
        self.ak = ak

    def geo_decoding(self, location_lat, location_lng, output='json', pois=0):
        """

        :param location_lat:
        :param location_lng:
        :param output:
        :param pois:
        :return:
        """
        params = {
            'ak': self.ak,
            'location': '{lat},{lng}'.format(lat=location_lat, lng=location_lng),
            'output': output,
            'pois': pois
        }
        r = requests.get(self.API_URL, params=params)
        res_json = r.json()
        if res_json['status'] == 0:
            return res_json['result']
        return

    def get_encoding(self, address, city=None, output='json'):
        """

        :param address: 地址
        :param city: 城市
        :param output: 返回类型
        :return: 返回值
        """
        params = {
            'ak': self.ak,
            'address': address,
            'output': output,
            'city': city
        }
        r = requests.get(self.API_URL, params=params)
        response = r.json()
        return response
