# 定义一个集合
num = {1,2,2,2,8,9,5,6,0}
num1 = {}
num2 = set()
print(num, type(num))
print(num1, type(num1))
print(num2, type(num2))

# 添加元素
num = {1,2,3}
num.add("数字")
print(num)
# 移除元素
num.remove(1)
print(num)
# 随机取元素
num.pop()
print(num)
# 清空集合
num.clear()
print(num)
# 取两个集合的差集
num1 = {1,2,3,4,9}
num2 = {1,6,3,5,6,8,48,7,9}
num = num1.difference(num2)
print(num)
# 消除两个集合的差集
num1.difference_update(num2)
print(num1)
# 合并两个集合
num3 = num1.union(num2)
print(num3)
# 统计集合数量
sum = len(num3)
print(sum)

# 练习
list = [1,2,3,5,9,7,2,6,8,4,6]
set = set()
for x in list:
    set.add(x)
print(set)