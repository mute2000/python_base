# if的练习题
print("欢迎来到儿童游乐场,儿童免费,陪同10元。(18岁及以上)")
age = input("请输入您的年龄")
age = int(age)
if age >= 18 :
    print("您已成年,陪同10元。")
print("祝您游玩愉快")

# if else的练习题
print("欢迎来到动物园")
high = int(input("请输出您的身高(cm):"))
if high >= 120:
    print("您需要购票")
else:
    print("不需要购票")
print("祝您玩的开心")

#if elif练习
num = 3;
if int(input("请输出您的猜想数字：")) == num:
    print("一次就猜对了")
elif int(input("不对，再猜一次，请输出您的猜想数字：")) == num:
    print("二次就猜对了")
elif int(input("不对，你还有最后一次机会，请输出您的猜想数字：")) == {num}:
    print("三次就猜对了")
else:
    print("全部猜错了，我写下的数字是", num)

# 嵌套语句的练习
age = 18
work_time = 1
level = 1
if age >= 18:
    print("符合第一项判断")
    if age < 30:
        print("年龄符合")
        if work_time > 2:
            print("年龄和工作时间满足条件，可以领取礼物")
        elif level > 3:
            print("年龄和等级满足条件，可以领取礼物")
        else:
            print("你不符合领取条件")
    else:
        print("您的年龄过大了，不符合领取条件")
else:
    print("未成年，不符合领取条件")

# 实例练习
import random
num = random.randint(1,10)

guess1 = int(input("请输入您的第一次猜测："))
if guess1 == num:
    print("第一次就猜对了")
else:
    if guess1 > num:
        print("大了")
    else:
        print("小了")

    guess2 = int(input("请输出您的第二次猜测："))
    if guess2 == num:
        print("第二次就猜对了")
    else:
        if guess2 > num:
            print("大了")
        else:
            print("小了")

        guess3 = int(input("请输出您的第三次猜测"))
        if guess3 == num:
            print("第三次猜测正确")
        else:
            print("三次机会用完了")
# 注意 嵌套逻辑