print(type(42), type(3.14), type("你好"), type(True), type(None))
# <class 'int'> <class 'float'> <class 'str'> <class 'bool'> <class 'NoneType'>


### Python	JS 对应	关键差异（坑）
### int 整数	number（不区分整 / 浮点）	Python 整数没有大小上限，不会溢出
### float 浮点	number	同样有 0.1+0.2 精度问题
### bool 布尔	boolean	只有 True/False（首字母大写）；bool 是 int 的子类，True=1
### str 字符串	string	单双引号等价；不可变
### NoneType	null + undefined	只有一个值 None，Python 不再区分 null 和 undefined

# Python 整数是任意精度的，多大都精确。这在加密、大整数计算场景是巨大优势
big = 2 ** 100
print(big)
# 1267650600228229401496703205376   （31 位，精确！）

a, b = 7, 2

print(a / b)    # 3.5   ← 单斜杠永远得到 float（即使整除）
print(a // b)   # 3     ← 整除（向下取整），JS 没有这个
print(a % b)    # 1     ← 取余，和 JS 一样
print(a ** b)   # 49    ← 幂运算，和 JS 的 ** 一样



# **Python 里所有东西都是对象**，包括整数、字符串。只不过 `int/str/float/bool/tuple` 是**不可变对象**—— 你没法 "原地修改" 它们，
# 所以看起来像 "值传递"。而 `list/dict/set` 是**可变对象**，能原地修改，所以标签效应很明显
x = [1, 2]
y = x          # y 不是复制了一份，而是和 x 指向同一个列表
y.append(3)
print(x)       # [1, 2, 3]  ← x 也变了！
print(x is y)  # True       ← is 判断"是否同一个对象"
print(x == y)  # True       ← == 判断"值是否相等"
# 判断是否为 `None` 永远写 `x is None`，不要写 `x == None`
print(a is b, "a is b") # False a is b
print(a is None, "a is None") # False a is None

# print(a === None, "a === Non") #  print(a === None, "a === Non") # False a is None SyntaxError: invalid syntax

# 注意：Python 里字典的键必须加引号，JSON/JS 那种 {name: "张三"} 写法会报 NameError
xObj = {
  "name": "张三",   # key 必须是字符串（或不可变类型），和 JS 不同
  "age": 18
}
yObj = xObj        # 赋值 = 引用同一个字典，不是复制（和上面列表一个道理）
yObj["age"] = 28   # 改 yObj 就是改 xObj，两者指向同一块内存
print(xObj)        # {'name': '张三', 'age': 28}  ← xObj 也被改了！
print(yObj)        # {'name': '张三', 'age': 28}
print(xObj is yObj)  # True  ← is 判断是否同一个对象

# 想让两者互不影响，必须显式复制：
zObj = xObj.copy()   # 浅拷贝（一层深；嵌套的列表/字典仍是共享的）
zObj["age"] = 99
print(xObj)          # {'name': '张三', 'age': 28}   ← 不受影响
print(zObj)          # {'name': '张三', 'age': 99}

# 需要连嵌套结构一起复制时用深拷贝：
import copy
deepObj = copy.deepcopy(xObj)


str1 = "abc"
str2 = str1
str2 += "d"
print(str1)
print(str2)

# 运算符	含义	类比
# ==	值是否相等	JS 的 ===（Python 的 == 不会乱转型）
# is	是否同一个对象（内存地址相同）	JS 引用比较

# 类型转换
print(int("42") + 8)      # 50      字符串转整数
# print(int("True"))        # 直接报错
print(int(True))          # 1
print(str(100) )     # 100分   整数转字符串
print(str(True))     # string True
print(float("3.14"))       # 3.14
# print(float("True"))       # 直接报错
print(float(True))       # 1.0
print(bool(0), bool(""), bool("1"),  bool(1))   # False False True True


# 真值规则与逻辑运算符
# **假值 = False / 0 / 空 / None**。其余全为真（包括非空字符串、非空列表、非零数字）。
print("真值规则与逻辑运算符")
bool(False), bool(0), bool(0.0), bool(""), bool(None), bool([]), bool({}), bool(set())

print(True and 1) # 1
print("1" and 0) # 0
print(0 and 1) # 0
print(True and False) # False   不是 &&
print(True and "1") # 1
print(True or False) # True    不是 ||
print(True or 1) # true
print(1 or True) # 1
print(not True) # False   不是 !

age = 30
print(18 <= age <= 60)   # True

print(0.1 + 0.2)              # 0.30000000000000004
print(0.1 + 0.2 == 0.3)      # False

print(1 < 2 < 3 < 4) # True
print(6 < 2 < 3 < 4) # False


print(abs(0.1+0.2 - 0.3) < 1e-9) # True

# 课后作业
print("课后作业")
# 1. 计算 `2 ** 100`，数一数结果有多少位（提示：转成 `str` 取 `len`）。
print(len(str(2 ** 100))) # 31
# 2. 给定 `x = 17, y = 5`，打印商（浮点）、整除结果、余数。
x, y = 17, 5
print(x / y)
print(x // y)
print(x % y)

# 3. 写表达式判断一个数 `n` 是否为偶数（提示：`n % 2 == 0`）。
n = 10
if (n % 2 == 0):
  print("偶数")
else:
  print("非偶数")
# 4. 说明 `0.1 + 0.2 == 0.3` 的结果并解释原因，给出一种安全判断两浮点近似相等的写法。
# 精度失真导致的 0.1 + 0.2 不等于 0.3

if ((0.1 * 10 + 0.2 * 10) / 10 == 0.3): 
  print("0.1 + 0.2 == 0.3")



# 5. `a = [1]; b = a; b.append(2)`，打印 `a` 看到什么？说明为什么。再用 `b = a.copy()` 重做，看 `a` 还变不变。
# a = [1, 2],因为b引用了a，修改b会影响a

# 6. 写一行代码：`score` 为 0 时打印 "零分"，否则打印 "有分"（用真值规则，不要写 `score == 0`）。
score = 0
if (score):
  print("有分")
else:
  print("零分")


# 7. 用链式比较和 `and` 写出：" 年龄在 18 到 60 之间 **且** 不是游客 " 的条件表达式（`is_visitor = False` 时应为真）。
age = 30
is_visitor = False
print(18 <= age <= 60 and not is_visitor)


