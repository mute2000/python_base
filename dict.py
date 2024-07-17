# # 字典
# # 定义字典
# diction = {"alice": 60, "bob": 59, "coco": 90}
# # 空字典
# diction2 = {}
# diction3 = dict()
# print(diction,type(diction))
# print(diction2,type(diction2))
# print(diction3,type(diction3))
# # 通过key获取value的值
# print(diction["alice"])
# # 增加元素
# diction["dd"] = 88
# print(diction)
# # 更新元素
# diction["bob"] = 60
# print(diction)
# # 删除元素
# diction.pop("dd")
# print(diction)
# # 清空元素
# diction.clear()
# print(diction)
# # 获取全部key
# diction = {"alice": 60, "bob": 59, "coco": 90}
# key = diction.keys()
# print(key)
# # 统计字典元素数量
# sum = len(diction)
# print(sum)
# 练习
staff = {
    "a": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "b": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "c": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "d": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    }
}
print(staff)
for key in staff:
    if staff[key]["级别"] == 1:
        staff[key]["级别"] += 1
        staff[key]["工资"] += 1000
print(staff)
