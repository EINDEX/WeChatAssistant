import os

import pymysql.cursors

# Connect to the database

import requests


class HeWeather():
    API_URI = 'https://api.heweather.com/x3/weather'

    def __init__(self, key):
        """

        :param key:
        """
        self.key = key

    def get_weather(self, city_id=None, city_name=None):
        """

        :param city_id:
        :param city_name:
        :return:
        """
        if city_id is None and city_name is None:
            raise ValueError()
        if city_id is None:
            city_id = self.__get_city_id(city_name=city_name)
            if city_id is None:
                return '没有你所在地区的天气信息'
        params = {
            'key': self.key,
            'cityid': city_id
        }
        r = requests.get(self.API_URI, params=params)
        return r.json()

    def __get_city_id(self, city_name):
        """

        :param city_name:
        :return:
        """
        connection = pymysql.connect(host=os.getenv('MYSQL_PORT_3306_TCP_ADDR'),
                                     user=os.getenv('MYSQL_USERNAME'),
                                     password=os.getenv('MYSQL_PASSWORD'),
                                     db=os.getenv('MYSQL_INSTANCE_NAME'),
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT city_id FROM Bf9TZ8kzvDUueH20.city WHERE city =%s"
                cursor.execute(sql, (city_name,))
                result = cursor.fetchone()
                if result is not None:
                    return result['city_id']
                else:
                    return None
        finally:
            connection.close()