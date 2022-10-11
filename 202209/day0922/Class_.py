# -*- coding:utf-8 -*-
class MyClass:
    i = 1

    def hi(self):
        print("你好，我的值为 {}".format(self.i))


class Complex:
    def __int__(self, real_part, img_part):
        r = real_part
        i = img_part

    # def print_(self):
    #     print(self.__class__)


# 实例化类
# mc = MyClass()
x = Complex(3, 4)
# x.print_()
# mc.hi()

