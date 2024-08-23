# TestSuite和TestRunner的使用
# 1.导包
import unittest

from frame.unittest_01 import TestDemo
from frame.unittest_02 import TestDemo2

# 2. 创建套件对象
suite = unittest.TestSuite()

# 3.使用套件对象，添加测试用例
# 方法一(将测试类中的指定方法进行添加)：套件对象.addTest(测试类名（'方法名'））
# suite.addTest(TestDemo('test_1'))
# suite.addTest(TestDemo('test_2'))
# suite.addTest(TestDemo2('test_1'))
# suite.addTest(TestDemo2('test_2'))
# 方法二（将测试类中的所有方法进行添加）：套件对象.addTest(unittest.makeSuite(测试类名))
suite.addTests(unittest.makeSuite(TestDemo))
suite.addTests(unittest.makeSuite(TestDemo2))
# 4.实例化运行对象
runner = unittest.TextTestRunner()

# 5.运行测试用例(运行对象.run(套件对象))
runner.run(suite)