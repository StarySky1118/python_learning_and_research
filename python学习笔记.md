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

- 大小写敏感
- 不能使用关键字，关键字同样大小写敏感

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

