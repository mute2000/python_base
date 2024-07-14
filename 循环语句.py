# while练习1
# i = 1
# j = 0
# while i <= 100:
#     j += i
#     i += 1
# print(j)

# while练习2
# 方法一
# import random
# num = random.randint(1,100)

# # 定义一个用来计数的变量
# sum = 0
# guess = int(input("请输出您的猜测"))

# while guess != num:
#     if guess > num:
#         print("大了")
#     else:
#         print("小了")
#     sum += 1
#     guess = int(input("请再次输出您的猜测"))

# # 加上最后猜对的那次的次数
# sum += 1
# print(f"您猜对了，猜了{sum}次")

# 方法二
# import random
# num = random.randint(1,100)
# print(f"{num}")

# count = 0
# condition = True

# while condition:
#     guess = int(input("请输出您的猜测"))
#     count += 1
#     if guess == num:
#         print(f"猜对了，猜了{count}次")
#         condition = False
#     else:
#         if guess > num:
#             print("大了")
#         else:
#             print("小了")

# # while练习3
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j} * {i} = {i * j}\t", end='')
#         j += 1
#     i += 1
#     print()

# # for循环练习
# name = "hello,HELLO"
# sum = 0

# for i in name:
#     if i == "l":
#         sum += 1
# print(f"name中有{sum}个l")
 
# range语句练习
# sum = 0
# for i in range(1, 100):
#     if i % 2 == 0:
#         sum += 1
# print(f"其中有{sum}个偶数")

# # for 循环练习2
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j} * {i} = {j * i}\t", end= '')
#     print()

# 综合练习
import random

res_money = 10000
for i in range(1, 21):
    num = random.randint(1,10)
    if num < 5:
        print("不发工资，下一位")
        continue
    else:
        if res_money > 0:
            res_money -= 1000
            print(f"编号{i}员工发工资,1000")
        else:
            print("工资发完了")
            break


    