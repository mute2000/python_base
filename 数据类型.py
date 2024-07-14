

# 验证数据类型的方法
# 使用print直接输出
print(type("小白"));

# 使用变量存储type()语句的结果
a = type(666);
print(a);

# 使用type()语句，查看变量中存储的数据类型信息
b = 13.14;
c = type(b);
print(c);

# 数据类型的转换

# 整数转换为浮点数
num1 = float(12);
print(type(num1), num1);

num2 = int(13.94);
print(type(num2), num2);
# 数字类型转换为字符串
str1 = str(12);
print(type(str1), str1);
# 字符串类型转换为数字
str2 = int("12");
print(type(str2), str2);
"""
如果字符串不是数字,则会报错(ValueError)
str3 = float("小白");
print(type(str3),str3);
"""
