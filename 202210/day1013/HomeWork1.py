# -*- coding:utf-8 -*-
# 定义空列表
number_list = []
even_list = []
# 填入 1-10
i = 1
while i < 11:
    number_list.append(i)
    i += 1

for num in number_list:
    if num % 2 == 0:
        even_list.append(num)
print(even_list)
