"""
1.打开浏览器（类级别）
2.输入网址（方法级别）
3.测试用例（测试方法）
4.关闭当前页面（方法级别）
5.关闭浏览器（类级别）
"""
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        print("输入网址")

    def tearDown(self):
        print("关闭当前页面")

    @classmethod
    def setUpClass(cls):
        print("打开浏览器")

    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器")

    def test_1(self):
        print("测试用例1")

    def test_2(self):
        print("测试用例2")