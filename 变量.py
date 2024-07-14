"""
变量是在程序运行中用来记录数据的

变量的命名规则
变量名 = 变量值

特征
值可以改变
"""

"""
练习
钱包余额为50
购买了冰激凌10元,可乐5元后
现在钱包余额是多少
"""

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

money = 50;
print('当前钱包余额：', money);

ice = 10;

print('购买了冰激凌,花费:', ice, '元');

coco = 5;

print('购买了可乐,花费:', coco, '元');

money = money - ice - coco;
print("钱包剩余：", money);