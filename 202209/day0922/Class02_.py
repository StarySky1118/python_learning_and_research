# -*- coding:utf-8 -*-
# 人类
class People:
    # 定义公开属性
    name = ''  # 姓名
    age = 0  # 年龄

    # 定义私有属性
    __weight = 0

    # 定义构造方法
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    # 定义实例方法
    def hi(self):
        print("你好，我是{}，今年{}岁".format(self.name, self.age))

    # 定义私有方法
    def __hello(self):
        print("这是一个私有方法。")


class Student(People):
    grade = 0

    def __init__(self, name, age, weight, grade):
        People.__init__(self, name, age, weight)
        self.grade = grade

    def hi(self):
        print("你好，我是{}，今年{}岁，上{}年级".format(self.name, self.age, self.grade))


# 创建对象
people = Student('田所浩二', 24, 114514, 8)
people.hi()
