# day1010

## 一、type() 的使用

### 1、基本使用方式

```python
# 查看数据类型
# print(type("哈哈"))
# print(type(11))
# print(type(11.8))

# 将数据类型信息赋值给变量
# string_type = type("哈哈")
# int_type = type(11)
# float_type = type(11.8)

name = "hh"
print(type(name))
name = 11
print(type(name))
```

> python 中变量是没有类型的，变量存储的数据有类型。

执行 11-14 行代码，得到以下结果：

```
<class 'str'>
<class 'int'>
```

## 二、数据类型转换

### 1、基本使用方法

```python
print(int(11.4))
print(float(11))
print(type(str(11)))
```

## 三、python 中的标识符

### 1、命名规则

- 标识符中只允许出现英文、数字、下划线。

- 不能用数字开头。

- 大小写敏感。
- 不能使用关键字，关键字同样大小写敏感。

### 2、命名规范

#### (1) 变量名

- 见名知意

- 下划线命名法

  使用下划线将多个单词进行分隔

- 英文字母全小写

#### (2) 类名

#### (3) 方法名

## 四、运算符的使用

### 1、算术运算符

> // 取整除
>
> % 取余
>
> ** 指数

### 2、赋值运算符

>=
>
>+=
>
>...

## 五、字符串

### 1、三种定义方式

```python
name1 = '田所浩二'
name2 = "田所浩二"
name3 = """
    田所浩二
    24岁
"""
```

正因为字符串既可以使用单引号定义，也可以使用双引号定义，因此字符串中可以包含两种引号。

也可以使用转义字符`\`。

### 2、字符串拼接

使用`+`。

只能由于字符串拼接，如果拼接其他类型的数据，将发生错误。

```python
name = "田所浩二"
age = 24
print("我是" + name + "，今年" + age + "岁")
```

```python
Traceback (most recent call last):
  File "Z:\研究生学习\python_learning_and_research\202210\day1010\Test01.py", line 36, in <module>
    print("我是" + name + "，今年" + age + "岁")
TypeError: can only concatenate str (not "int") to str
```

### 3、字符串格式化

> 字符串拼接麻烦，并且无法拼接其他类型的数据。

使用`%`进行占位拼接。

三种占位符：`%s`、`%d` 和 `%f`。

```python
name = "田所浩二"
age = 24
print("我是%s，今年%d岁" % (name, age))
```

# day1011

## 一、字符串

### 1、格式化精度控制

- `.n` 设置精度

  例如 `.2f`

### 2、字符串格式化

使用 `f"{占位}"` 的方式。

```python
print(f"你好，我是{name}, 今年{age}岁")
```

### 3、表达式格式化

将表达式放入上述字符串格式化变量位置。

```python
print("今年%d岁" % (1 + 1))
print(f"你好，我是{1 + 1}岁的田所浩二")
```

## 二、数据输入

`input()` 函数接收键盘输入，键盘输入内容将作为字符串存储。

```python
print("你是一个一个什么啊?")
name = input()
print("你是一个一个%s啊啊啊" % name)
```

`input()` 函数可以放入字符串作为提示输入的语句。

```python
name = input("你是一个一个什么啊？")
print("你是一个一个%s啊啊啊" % name)
```

## 三、分支结构

### 1、布尔类型与比较运算符

布尔类型 `bool` 属于 `Number` 类型。字面量 `True` 和 `False`。

### 2、分支结构语句格式

```python
if 条件:
    语句
elif 条件:
    语句
elif 条件:
    语句
```

## 四、循环结构

### 1、for 循环语句

for 语句格式：

```python
for x in 待处理数据集（序列）
	语句
```

无法定义循环条件。理论上，python 中的 for 循环无法构建无限循环。

### 2、序列类型

待处理数据集严格来讲，称之为序列类型。

序列类型包括：

- 字符串
- 列表
- 字典

使用 `range()` 可以获得一个简单的数字序列。

`range()` 有三种使用方式：

```python
# range(num)：0,...,num-1
for i in range(5):
    print(i, end="")
    
# range(num1, num2)：num1, num1+1, ..., num2-1
for i in range(0, 5):
    print(i, end="")

# range(num1, num2, step)：num1, num1+step, ...,
# 也不包含num2
for i in range(0, 5, 2):
    print(i, end="")    
```

### 3、循环结构中临时变量的作用范围

理论上来说，变量 `i` 作用范围是 for 循环内部，这是规范。但实际上，在 for 循环外，变量 `i` 也可以被访问到。

