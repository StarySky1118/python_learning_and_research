# -*- coding:utf-8 -*-
class Dog:
    name = ""
    __age = 0

    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 打印输出私有属性
    def get_age(self):
        print(self.__age)

    # 私有方法
    def __wolf(self):
        print("狗在狼叫什么？")


dog = Dog("哈士奇", 11)
dog.get_age()

