# -*- coding:utf-8 -*-
import operator
lst = ["Tencent", "Alibaba", "NetEase"]

# 列表元素的添加
print(lst)
lst.append("BaiDu")
print(lst)

# 列表元素的删除
lst.remove("BaiDu")
print(lst)

# 列表的比较
a = [1, 2]
b = [2, 3]
c = [2, 3]
print(operator.eq(a, b))
print(operator.eq(b, c))

# 列表相关函数
print(len(lst))  # 列表元素个数
max(lst)  # 列表元素最大值
