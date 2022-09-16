# -*- coding:utf-8 -*-
class Homo:
    name = "田所浩二"
    age = 24

    # 定义构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 普通方法
    def reap(self):
        print(str(self.name) + "雷普了远野")


homo1 = Homo("淳平", 24)
homo1.reap()
