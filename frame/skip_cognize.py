import unittest

condition = 10
class SkipCognize(unittest.TestCase):
    @unittest.skip('跳过测试')
    def test_1(self):
        print('test_1')
    @unittest.skipIf(condition > 5 , '跳过测试')
    def test_2(self):
        print('test_2')

    def test_3(self):
        print('test_3')