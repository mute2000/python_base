# 1.查找列表中的最大值
# 方法一：max函数
list = [4, 6, 8, 9, 2, 5, 1, 3]
max = max(list)
print(max)
# 方法二：for循环
max = 0
for i in list:
    if i > max:
        max = i
print(max)

# 2.将列表从小到大排序
# 1.sorted()函数
sort = sorted(list)
print(sort)
# 2.冒泡排序
for i in range(len(list)):
    for j in range(len(list) - 1 - i):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print(list)

# 逆转一个字符串
str = "hello"
# 切片
new_str = str[::-1]
print(new_str)