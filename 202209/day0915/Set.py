# -*- coding:utf-8 -*-

mySet = {100, 100.0, "逼乎", "知网"}

print(mySet)

# 测试集合成员
testStr = "逼乎"
if testStr in mySet:
    print(testStr + "在集合中")
else:
    print(testStr + "不在集合中")


