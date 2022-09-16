# -*- coding:utf-8 -*-
# dic = {"name": "田所浩二", "age": 24}
# key = ""
# newDic = {key: len(key) for key in dic}
# print(newDic)

# lst = [1, 2, 3]
# a = 1
# dct = {a: a ** 3 for a in lst}
# print(dct)

a = ""
b = [a for a in "abcdedf" if a not in "abc"]
print(b)
