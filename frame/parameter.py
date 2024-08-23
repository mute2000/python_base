# 1.导包
import unittest
from parameterized import parameterized

from frame.tools import login

# 组织测试数据
data = [
    ("admin", "123456", "登录成功"),
    ("admin1", "123456", "登录失败"),
    ("admin", "1234567", "登录失败"),
    ("aaa", "1234567", "登录失败")
]
# 2.定义测试类
class TestLogin(unittest.TestCase):
    # 3.书写测试方法（测试数据用变量代替）
    @parameterized.expand(data)
    def test_login(self, username, password, expect):
        self.assertEqual(expect, login(username, password))


# 4.组织测试数据并传参（装饰器@）