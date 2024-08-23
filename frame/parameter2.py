# 1.导包
import json
import unittest
from parameterized import parameterized

from frame.tools import login

# 组织测试数据
def data2():
    with open("frame\data.json", encoding="UTF-8") as f:
        result = json.load(f)
        data = []
        for i in result:
            data.append((i.get("username"), i.get("password"), i.get("expect")))

    return data
# 2.定义测试类
class TestLogin(unittest.TestCase):
    # 3.书写测试方法（测试数据用变量代替）
    @parameterized.expand(data2())
    def test_login(self, username, password, expect):
        self.assertEqual(expect, login(username, password))


# 4.组织测试数据并传参（装饰器@）