# -*- coding:utf-8 -*-
my_list = []

i = 0
while i < 10:
    my_list.append(i)
    i += 1

# 进行序列切片
# l1 = my_list[1:5]
# print(l1)

# l2 = my_list[:]
# print(l2)

# 从头到尾步长为2
# l3 = my_list[::2]
# print(l3)

# 从尾到头
l4 = my_list[::-1]
print(l4)
