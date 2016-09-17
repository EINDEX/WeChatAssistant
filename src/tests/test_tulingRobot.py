from unittest import TestCase

from app.main.api.tuling_robot import TulingRobot


class TestTulingRobot(TestCase):
    def setUp(self):
        self.api = TulingRobot('')

    def test_send_message(self):
        res = self.api.send_message('你好',0)
        print(res)
