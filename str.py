# # 字符串
# # 定义
# str = "hello, world, hello"
# # 通过索引取值
# index = str[5]
# print(index)
# # index方法
# select = str.index("o")
# print(select)
# # replace方法
# str2 = str.replace("hello","Hello")
# print(str2)
# print(str)
# # spilt方法
# str3 = str2.split(",")
# print(str3)
# strip方法
str = "  hello, world, hello     "
print(str)
str1 = str.strip()
print(str1)
str2 = str1.strip("o")
print(str2)
# 统计字符串中某字符串统计的次数
sum = str.count("o")
print(sum)
# 统计字符串长度
sum2 = len(str)
print(sum2)
# 遍历

# 练习
str = "hello, world, hello"
count = 0
for i in str:
    count += 1
print(count)

sum = str.count("ll")
print(sum)

str1 = str.replace(" ","|")
print(str1)

str2 = str1.split("|")
print(str2)