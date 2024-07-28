# 返回多个值
def a():
    return "a", 12, True
print(a())
def code(name, age, sex):
    print(f"姓名为{name}, 年龄为{age}, 性别为{sex}")
# 位置参数
code("alice", 18, "女")
# 关键字参数
code(sex = "男", name = "bob", age = 16)
# 混用
code("alice", 18, sex = "女")
# 缺省参数
def code2(name, sex, age = 18):
    print(f"姓名为{name}, 年龄为{age}, 性别为{sex}")
code2("alice", 18)
# 不定长参数
def code3(*args):
    print(args)
code3("a","56485",True,896)
