# # 创建一个类
# class Student:
#     # 定义属性
#     name = "张三"
#     age = 18
#     # 定义方法
#     def say(self):
#         print(f"我叫{self.name},今年{self.age}岁了")

# # 创建一个对象
# s = Student()

# # 调用方法
# s.say()

# # 构造方法__init__
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(f"我叫{self.name},今年{self.age}岁了")

# p = Person("张三",18)

# # 练习
# class Student:
#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address
#     def __str__(self):
#         return f"【学生姓名：{self.name}，年龄：{self.age}，地址：{self.address}】"

        
# for i in range(3):
#     print(f"当前录入第{i+1}个学生信息，总共需要录入3个学生信息")
#     name = input("请输入姓名")
#     age = input("请输入年龄")
#     address = input("请输入地址")
#     s = Student(name,age,address)
#     print(f"学生{i+1}的信息录入完成，信息为{s}")

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"【姓名：{self.name}，年龄：{self.age}】"
    
#     def __lt__(self,other):
#         return self.age < other.age

# p1 = Person("张三",18)
# p2 = Person("李四",19)

# print(p1 < p2)

# 封装练习
class Phone:
    __is_5g_enable = False
    def __check_5g(self):
        if self.__is_5g_enable == True:
            print("5g已开启")
        else:
            print("5g未开启,使用4g")
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()
phone.call_by_5g()