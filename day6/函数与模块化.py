print("----Part 1・def 定义函数----")
def green(name):
  return f"你好，{name}!"
print(green("张三"))

# Python 没有 return 的函数返回 `None`，不是 undefined

print("----Part 2・参数：位置 / 默认 / 关键字----")
def grent_full(name, grenting = "你好", punctuation = "!"):
  return f"{grenting}, {name}{punctuation}"
print(grent_full("张三"))
print(grent_full("李四", "你好", "！"))
print(grent_full("王五", punctuation = "！"))
print(grent_full("赵六", "你好"))

# 三种调用方式：

# 1. **位置参数**：按顺序传，`greet_full("小刚", "晚上好", "。")`
# 2. **默认参数**：不传就用默认值，`greet_full("小明")`
# 3. **关键字参数**：按名字传，顺序无所谓，`greet_full("小红", greeting="早上好")`

# > 💡 默认参数必须放在最后：`def f(a, b=10)` ✅，`def f(a=10, b)` ❌ 报错。这和 JS 的默认参数一样。

print("----Part 3・*args 和 **kwargs----")
def sum_all(*args):
  print(type(args)) # <class 'tuple'>
  return sum(args)

print(sum_all(1, 2, 3, 4))   # 10
# `*args` 把传入的多个参数打包成一个 tuple，函数内部用 `args` 接收。

### **kwargs：接收任意多个关键字参数（打包成 dict）

def print_info(**kwargs):
  for k, v in kwargs.items():
    print(f"  {k} = {v}")

print_info(name="小明", age=18, city="上海")
# name = 小明
# age = 18
# city = 上海

# `**kwargs` 把关键字参数打包成 dict，用 `.items()` 遍历。

# > 
# > 🧠 命名约定：`*args` 收位置参数，`**kwargs` 收关键字参数。这两个名字只是约定，用 `*nums` `**opts` 也行，但团队都认 args/kwargs。

print("----Part 4・return 多值返回----")

def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([3, 1, 4, 1, 5])
result = min_max([3, 1, 4, 1, 5])
print(f"最小值={lo}, 最大值={hi}")   # 最小值=1, 最大值=5
print(f"{result}")   # result (1, 5)

# JS 要返回多个值得写 `return [min, max]` 再解构，Python 直接逗号分隔就行。Day 2 讲过 tuple 解包，这里就是它的应用。

print("----Part 5・作用域----")

x = 100  # 全局变量

def func():
    x = 200  # 局部变量，和全局 x 互不影响
    print("函数内 x =", x)

func()              # 函数内 x = 200
print("函数外 x =", x)   # 函数外 x = 100

# **核心规则**：函数内部给变量赋值，默认创建局部变量，不会修改全局变量。想在函数内改全局变量要写 `global x`（但尽量少用，函数应该通过参数输入、return 输出，而不是改全局）。

# > 
# > 对应 JS 的函数作用域 / 块级作用域，Python 的规则类似：函数是一层作用域。

print("----Part 6・lambda 匿名函数----")
square = lambda n: n * n
print(square(3))   # 9

# lambda 就是**一行的小函数**，等价于：
def square(n):
  return n * n
print(square(3))   # 

# 最常见用途：配合 sort 的 key 参数，传入匿名函数。
pairs = [(2, "b"), (1, "a")]
pairs.sort(key=lambda p: p[0])
print(pairs)   # [(1, 'a'), (2, 'b')]
# lambda 只适合**一行表达式**，逻辑复杂就用 `def`。

print("----Part 7・docstring + import----")

def add(a, b):
    """返回两数之和。"""
    return a + b

print(add.__doc__)     # 返回两数之和。
# help(add)              # 更详细的帮助


import math                    # 导入整个模块，用 math.sqrt()
print(math.sqrt(16))           # 4.0

from random import randint     # 只导入需要的函数，直接用
print(randint(1, 10))          # 随机数

import datetime as dt          # 起别名
print(dt.date.today())         # 2026-09-20

# > Python 标准库很丰富，常用的 `math`（数学）、`random`（随机）、`datetime`（日期）、`os`（操作系统）、`json`（JSON 处理）以后都会用到。

print("随堂练习")

# 写一个 `rectangle_area(w, h)` 函数，返回矩形面积。
def rectangle_area(w, h):
  return w * h

print(rectangle_area(3, 4)) 

# 写一个 `average(*nums)` 函数，接收任意多个数，返回平均值。
def sums(*nums):
  return sum(nums)
  
print(sums(1, 2, 3, 4, 5))

# 用 `import math` 写一个 `circle_area(r)`，返回圆面积 `π * r²`。
def circle_area(r):
  return math.pi * r * r

print(circle_area(3))

print("----Day 6 课后作业----")

# 写一个 `greet(name="同学")` 函数，默认参数为 "同学"，调用时不传参和传参各打印一次。
def greet(name = "同学"):
  return f"{name}"

print(greet())
print(greet("同学"))

# 写一个 `is_even(n)` 函数，返回 True/False 判断是否偶数。
def is_even(n):
  return n % 2 == 0

print(is_even(3))
print(is_even(4))

# 写一个 `analyze(numbers)` 函数，返回列表的最大值、最小值、平均值（三个返回值）。
def analyze(numbers):
  return max(numbers), min(numbers), sum(numbers) / len(numbers)
  
print(analyze([1, 2, 3, 4, 5]))

# 写一个 `sum_args(*args)` 函数，接收任意多个数字，返回它们的和。
def sum_args(*args):
  return sum(args)
  
print(sum_args(1, 2, 3, 4, 5))


# 写一个 `print_person(**kwargs)` 函数，遍历打印所有关键字参数。

def print_person(**kwargs):
  for k, v in kwargs.items():
    print(f"{k} = {v}")
    
print_person(name="小明", age=18, city="上海")

# 用 lambda 把 `[(3, "c"), (1, "a"), (2, "b")]` 按第一个元素排序。
pairs = [(3, "c"), (1, "a"), (2, "b")]
pairs.sort(key=lambda p: p[0])
print(pairs)

# 写一个 `celsius_to_fahrenheit(c)` 函数，摄氏转华氏（公式：`c * 9/5 + 32`），并写 docstring 说明。
def celsius_to_fahrenheit(c):
  """
  摄氏转华氏（公式：c * 9/5 + 32）
  """
  return c * 9/5 + 32

print(celsius_to_fahrenheit(30))

# 用 `import math` 写一个 `circle_area(r)` 函数，返回圆面积，保留 2 位小数。
def circle_area(r):
  return round(math.pi * r * r, 2)

print(circle_area(3))