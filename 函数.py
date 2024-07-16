# # 函数练习（定义）
# def 核酸检查():
#     print("请打开您的核酸码")
# 核酸检查()

# # 函数练习2（参数）
# def tem_check(x):
#     if x <= 37.5:
#         print("体温正常，通过")
#     else:
#         print("体温异常，隔离")

# tem_check(38.6)

# # 作用域
# num = 10
# def a():
#     print(num)
# def b():
#     global num
#     num = 20
#     print(num)
# a()
# b()
# print(num)

# # 综合练习
# # 方法一

# money = 500000
# # 无意义，有没有这行代码都可以
# name = None
# name = input("请输入您的名字：")

# def select_money():
#     print(f"{name},您好，您的余额为{money}")

# def add_money(x):
#     global money
#     money += x
#     print(f"{name},您好，您存款{x}元\n您现在的余额为{money}")

# def subtract_money(y):
#     global money
#     money -= y
#     if y <= money:
#             print(f"{name},您好，您取款{y}元\n您现在的余额为{money}")
#     else:
#          print("余额不足")

# def index():
#     print(f"{name},您好，欢迎来到银行，请选择您的操作\n查询余额\t[输出1]\n存款\t\t[输出2]\n取钱\t\t[输出3]")
#     return input("请输出您的选择")

# while True:
#      select = index()
#      if select == "1":
#           select_money()
#           continue
#      elif select == "2":
#           among = int(input("请输出您的存款金额："))
#           add_money(among)
#           continue
#      elif select == "3":
#           among = int(input("请输出您的取款金额："))
#           subtract_money(among)
#           continue
#      else:
#           print("退出程序")
#           break

# 方法二
money = 1000000
name = None

name = input("请输入您的姓名")

def query():
    print(f"{name},您好，您当前余额为{money}元")

def saving(x):
    global money
    money += x
    print(f"{name},您好，您存款{x}元成功")
    query()

def get_money(x):
    global money
    money -= x
    print(f"{name},您好，您取款{x}元成功")
    query()

def main():
    print(f"{name},您好，欢迎来到银行，请选择操作")
    print("查询余额\t[输出1]")
    print("存款\t\t[输出2]")
    print("取款\t\t[输出3]")
    return input("请输出您的选择")

while True:
    Keyboard_input = main()
    if Keyboard_input == "1":
        query()
        continue
    elif Keyboard_input == "2":
        num = int(input("输出您的存款金额"))
        saving(num)
        continue
    elif Keyboard_input == "3":
        num = int(input("输出您的取款金额"))
        get_money(num)
        continue
    else:
        print("程序结束")
        break
