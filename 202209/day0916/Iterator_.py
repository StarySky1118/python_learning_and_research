# -*- coding:utf-8 -*-
lst = [1, 2, 3, 4]
# 创建迭代器对象
it = iter(lst)

# print(next(it))
#
# print(next(it))

# 使用for进行遍历
for i in it:
    print(i, end="")
