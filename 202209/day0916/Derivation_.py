# -*- coding:utf-8 -*-

names = ["tom", "jack", "mary", "james"]
name = ""
newNames = [name.upper()for name in names if len(name) > 3]
print(newNames)

# 计算30以内可被2整除的整数
i = 0
t = [i for i in range(30) if i % 2 == 0]
print(t)

