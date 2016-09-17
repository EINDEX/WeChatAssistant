from pprint import pprint
from unittest import TestCase

from app.main.api import he_weather_api


class TestHeWeather(TestCase):
    def test_get_weather(self):
        json = he_weather_api.get_weather('CN101010100')
        print(json)

    def test_get_city_id(self):
        import requests
        from bs4 import BeautifulSoup as bs
        res=requests.get('http://www.heweather.com/documents/cn-city-list')
        res_bs = bs(res.text,"html.parser")
        tr_list=res_bs.find_all('tr')
        for line in tr_list:
            import re
            if re.match('.*CN.*',str(line)):
                box_list = [box.text for box in line.find_all('td')]

                print ("INSERT INTO `Bf9TZ8kzvDUueH20`.`city` (`city_id`, `pingyin`, `city`, `aera`, `province`) VALUES ('%s','%s','%s','%s','%s');"%
                         (box_list[0],box_list[1],box_list[2],box_list[3],box_list[4]))
