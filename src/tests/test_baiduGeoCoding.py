from unittest import TestCase

from app.main.api.baidu_geocoding import BaiduGeoCoding


class TestBaiduGeoCoding(TestCase):
    def setUp(self):
        self.api = BaiduGeoCoding('')

    def test_geo_decoding(self):
        res = self.api.geo_decoding(location_lat=39.98342407140365, location_lng=116.32298699999993)
        print(res)

    def test_get_encoding(self):
        res=self.api.get_encoding(address='深圳图书馆')
        print(res)
