from .heweather import HeWeather
from .baidu_geocoding import BaiduGeoCoding
from .tuling_robot import TulingRobot
from config import Config

tuling_robot_api = TulingRobot(Config.TULING_ROBOT)
baidu_geo_coding_api = BaiduGeoCoding(Config.BAIDU_AK)
he_weather_api = HeWeather(Config.HEWEATHER_KEY)