# -*- coding:utf-8 -*-
name_list = ["田所浩二", "德川", "我修院"]

# 查询下标索引
# index = name_list.index("田所浩二")
# print(f"下表为{index}")
# print(name_list.index("淳平"))

# 插入元素
# name_list.insert(1, "淳平")
# print(name_list)
# name_list.insert(name_list.index("德川"), "淳平")
# print(name_list)

# 追加元素
# number_list = [1, 2, 3]
# name_list.extend(number_list)
# print(f"姓名列表：{name_list}")
# print(f"数字列表{number_list}")

# 删除元素
# del name_list[name_list.index("田所浩二")]
# print(f"name_list{name_list}")
# name = name_list.pop(name_list.index("田所浩二"))
# print(f"取出的名字为{name}"
# name_list.remove("田所浩二")

# 统计元素数量
# count = name_list.count("田所浩二")
# print(count)

# 遍历列表元素
# while 方式
# index = 0
# while index < len(name_list):
#     name_elem = name_list[index]
#     print(name_elem)
#     index += 1

# for 方式
for name in name_list:
    name = "田所浩二"
print(name_list)
