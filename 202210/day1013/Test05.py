# -*- coding:utf-8 -*-
# 非空集合的定义
name_set = {"田所浩二", "德川", "我修院"}
# 空集合的定义
# name_set = {}
# name_set = set()
# 添加新元素
name_set.add("淳平")
print(name_set)

# 移除元素
# name_set.remove("淳平")
# print(name_set)

# 随机取出元素
# elem = name_set.pop()
# print(elem)

# 差集
# name_set1 = {"我修院"}
# name_set3 = name_set.difference(name_set1)
# print(name_set3)

# 消除差集
# name_set_del = {"我修院"}
# name_set.difference_update(name_set_del)
# print(name_set)

# 集合合并
name_set_union = {"德川", "野兽先辈"}
name_set3 = name_set.union(name_set_union)
print(name_set3)
