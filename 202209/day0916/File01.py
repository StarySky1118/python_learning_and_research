# -*- coding:utf-8 -*-

fileName = "Z:\\abc.txt"
# file = open(fileName, "w")  # 向文件中写入
# file.write("昔人已乘黄鹤去，此地空余黄鹤楼。")
# file.close()
#
# print("文件写入成功！")

# 演示文件的读取
# file = open(fileName)
# s = file.read()
# print(s)

# file = open(fileName)
# for line in file:
#     print(line, end="")

s3 = "日暮乡关何处是，烟波江上使人愁。"
file = open(fileName, "a")
num = file.write(s3)
print("写入成功！写入字符数：" + str(num))

print("文件对象当前所处位置：" + str(file.tell()))
file.close()


