# 字符串的定义方式
# 单引号，双引号，三引号
name = """
hello,
小白。
"""
print(name);

# 引号的嵌套
print('"hello,world"');
print("'小白'");
print("The word 'hello' means '你好' in English.");
print("\"hello, 小白\"");


# 字符串的拼接

# 通过+拼接
print("你好" + "小白");
str1 = "Hello";
str2 = "World";
print(str1 + str2);
# 通过占位符拼接
"""
name = "小白";
age = 18;
message = "我的名字是%s,今年%s岁" % (name, age);
print(message);
print(type(message));
"""
name = "小白";
age = 18;
Π = 3.14;
message = "我的名字是%s,今年%d岁,圆周率是%f" % (name, age, Π);
print(message);
print(type(message));
# 通过format拼接
message = f"我的名字是{name},今年{age}岁";
print(message);
a = f"{"牛逼"}{666}";
print(a);

# 练习
name = "传智播客"
stock_price = 19.99
# 需用字符串类型，整数不能以0开头（会有SyntaxErro报错）
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
last_price = stock_price * stock_price_daily_growth_factor ** growth_days
result = f"公司：{name}, 股票代码：{stock_code}, 当前股价：{stock_price}"
print(result)
result2 = "每日增长系数：%3.1f,经过%d天后,股价达到了%.2f" % (stock_price_daily_growth_factor, growth_days, last_price)
print(result2)