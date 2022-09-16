# -*- coding:utf-8 -*-
class Dog:
    name = "田所浩二"
    age = 24

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def reap(self):
        print(str(self.name) + "雷普了" + "远野")


dog = Dog("田所浩二", 25)
dog.reap()
print(dog.age)


