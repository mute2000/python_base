import unittest

from frame.tools import login

class TestLogin(unittest.TestCase):
    def test_username_password_ok(self):
        self.assertEqual('登录成功', login('admin', '123456'))

    def test_username_password_error(self):
        self.assertEqual('登录失败', login('aaa', '1234567'))

    def test_username_error(self):
        self.assertEqual('登录失败', login('admin1', '123456'))

    def test_password_error(self):
        self.assertEqual('登录失败', login('admin', '1234567'))