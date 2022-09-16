# -*- coding:utf-8 -*-
def change(m):
    print(id(m))
    m = 2
    print(id(m))


a = 1
change(a)
