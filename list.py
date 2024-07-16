# # 定义一个列表
# name_list = ["alice", "john", "coco"]
# print(name_list)

# # 列表的索引
# # 正向索引查找(索引下标从0开始)
# print(name_list[0])
# # 反向索引查找（索引下标从-1开始）
# print(name_list[-3])

# # 列表的方法
# # 查询指定元素列表的索引
# index = name_list.index("alice")
# print(index)
# # 修改
# name_list[0] = "ace"
# name_list[-1] = "Coco"
# print(name_list)
# # 插入
# name_list.insert(0,"err")
# print(name_list)
# # 追加
# name_list.append("Bob")
# print(name_list)
# # 追加2
# name_list2 = ["a", "b", "c"]
# name_list.extend(name_list2)
# print(name_list)
# # 删除
# del name_list[0]
# print(name_list)
# name_list.pop(1)
# print(name_list)
# num = name_list.pop(1)
# print(num)
# num1 = [1,2,3,4,1,5]
# num1.remove(1)
# print(num1)
# # 清空列表
# num1.clear()
# print(num1)
# # 统计
# num = [1,2,3,55,5,85,5,4,46,6,5,5]
# sum = num.count(5)
# sum2 = len(num)
# print(num)
# print(sum)
# print(sum2)

# # 综合练习
# age = [21,25,21,23,22,20]
# num = [29,33,30]
# age.append(31)
# age.extend(num)
# first = age[0]
# print(first)
# last = age.pop(-1)
# print(last)
# select = age.index(31)
# print(select)
# print(age)

# 综合练习2
# num = [1,2,3,4,5,6,7,8,9,10]
# new_num = []
# for x in num:
#     if x % 2 == 0:
#         new_num.append(x)
#     x += 1
# print(new_num)

num = [1,2,3,4,5,6,7,8,9,10]
new_num = []
index = 0
while index < len(num):
    element = num[index]
    if element % 2 == 0:
        new_num.append(element)
    index += 1
print(new_num)