# # 定义元组
# age = (1,2,3,6,8)
# print(age,type(age))

# ## 定义一个元素的元组
# age = (1,)
# print(age,type(age))

# # 元组的嵌套
# num = ((1,2,3), (4,5))
# index = num[1][0]
# print(num)
# print(index)

# # 元组的查找（index）
# age = (1,2,3,6,8,6)
# a = age.index(6)
# print(a)
# # 元组的统计（count）
# sum = age.count(6)
# print(sum)
# # 统计（len()）
# all = len(age)
# print(all)

# 练习
tuple1 = ("张三", 18, ["football", "music"])
select = tuple1.index(18)
print(select)
select1 = tuple1[0]
print(select1)
del tuple1[2][0]
print(tuple1)
tuple1[2].append("coding")
print(tuple1)