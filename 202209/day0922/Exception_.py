# -*- coding:utf-8 -*-

# 零除数异常
# print(10 / 0)

# try:
#     print(10 / 0)
# except (ZeroDivisionError, TypeError):
#     pass

x = 10
try:
    if x > 5:
        raise Exception("x 的值不能大于 5，当前 x 的值为{}".format(x))
except Exception:
    print("异常捕获！")
    raise

print("程序继续执行")

