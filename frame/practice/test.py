import unittest

from frame.practice.tools import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        if add(1,2) == 3:
            print("测试通过")
        else:
            print("测试失败")