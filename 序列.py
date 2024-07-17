# 序列：内容连续，有序，可使用下标的数据容器
# 创建一个数列
list = [1,2,3,4,5,6]
str = "hello, world, hello"
tuple = ("a", "b", "c","d")
# 起始下标为空
list1 = list[:5]
print(list1)
# 结束下标为空
str1 = str[1: :2]
print(str1)
# 起始和结束都为空
tuple1 = tuple[ : :2] 
print(tuple1)
# 步长为负数
list2 = list[3: 0 : -1]
print(list2)
# 倒序字符串
str2 = str[ : : -1]
print(str2)
# 练习
str = "你好，白小，还有小黑"
str1 = str[4:2:-1]
print(str1)

str2 = str.split("，")[1][::-1]
print(str2)

str3 = str.split("，")
index = str3[1]
last = index[::-1]
print(last)