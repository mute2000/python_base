# testcase书写步骤
# 1.导包
import unittest
# 2.创建测试类(测试类：需要继承unittest模块中的TestCase的类)
class TestDemo2(unittest.TestCase):
    # 3.创建测试方法
    # 书写要求：test开头
    def test_2_1(self):
        print("test_2.1")
    def test_2_2(self):
        print("test_2.2")

# 4.执行测试方法
# python -m unittest 路径
# python -m unittest 路径按这个方法运行后会自动生成__pycache__ 文件夹
# __pycache__ 文件夹的作用是
# 1.提升性能：编译后的字节码比直接运行源代码要快
# 2.减少编译时间：避免每次运行时都重新编译代码。
