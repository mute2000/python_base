# testloader的使用

# 1.导包
import unittest

# 2.实例化加载对象并添加用例
# unittest.TestLoader().discover('路径','用例文件名')
suite = unittest.TestLoader().discover('frame','unittest_*.py')

# 3.实例化运行对象
runner = unittest.TextTestRunner()

# 4.运行用例
runner.run(suite)