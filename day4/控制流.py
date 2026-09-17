print("----昨日复习----")

wendu = 23.456
print(f"温度{wendu:.1f}")
s = "  hello world  "
print(s.strip().upper().lower())
a = "a,b,c,d"
print("-".join(a.split(",")))
print(a.replace(",", "-"))
s1 = "abcdeshjk"
print(s1[-3:][::-1])
link = "https://baidu.com"
print(link.startswith("https://"))
print(link.find("https://"))
print(s1.count("a"))
print("x" + link[0:])



print("----if /elif/else + 三元----")

score = 85
if score >= 90:
    grade = "优"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"
print(f"成绩{score} -> {grade}")   # 成绩85 -> 及格

# 三元表达式
age = 17
status = "成年" if age >= 18 else "未成年"
print(status)


print("----for循环 + range----")
fruits = ["苹果", "香蕉", "梨"]
for item in fruits:
  print(f"吃 {item}")

# Python 的 `for` 直接遍历元素本身，对应 JS 的 `for (const item of fruits)`。它**不是** C 语言那种 `for(i=0; i<n; i++)`。如果你要数字序列，用 `range`

# range：造数字序列
# 记忆口诀：**`range(start, stop, step)`，start 含、stop 不含**，和切片完全一致。
# > 💡 range 不会真的生成完整列表（它是惰性的），遍历 100 万次也不占多少内存。

print(list(range(10))) # [0, 1, 2, 3, 4]       从0到4（左闭右开）
print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]      从1到9，步长2
print(list(range(1, 10, -1))) # []      从1 开始，到 10 结束，倒叙，没有符合的数据 所以打印 []
print(list(range(10, 0, -1))) # [10,9,8,...,1]       倒序，步长-1
# print(list(range(10, 0, 0))) # 报错 arg 3 must not be zero 第三个参数不能为 0

print("----enumerate 和 zip（高频工具）----")
# JS 里要同时拿下标得写 `fruits.map((item, i) => ...)` 或 `for (let i = 0; i < fruits.length; i++)`
# `start=1` 让序号从 1 开始（不写默认 0）。这是写 "第 N 个元素" 最常用的写法
for i, item in enumerate(fruits, start = 1):
  print(f"第{i}个水果是{item}")

# zip：并行遍历多个序列
names = ["a", "b", "c"]
ages = [20, 30, 40]
# 注意：短的先结束（如果一长一短，按短的截断）。
# 如果两个 list 长度不一致，zip 会截断较长的 list，按最短的长度循环
# ages = [20, 30, 40, 50]
# ages = [20, 30]
# 没有索引
for name, age in zip(names, ages):
  print(f"{name} is {age} years old")

print("---- while + break/continue/pass ----")

n = 0
while n < 5:
  n += 1
  if n == 2:
      continue    # 跳过本次，继续下一轮
  if n == 4:
      break       # 直接跳出整个循环
  print(f"  n={n}")

# Python 的代码块不能空着，不然会报错（冒号下一行必须有内容）。先占坑就用 `pass`

def todo():
  pass

if 1 < 2:
  pass

print("----循环的 else----")

for i, x in enumerate([1, 3, 4, 5, 7]):
  if x == 4:
    print(f"找到4了!，在第{i + 1}个位置")
    break
  else:
    print("没找到4（循环正常结束才走这里）")

print("---- 随堂练习 ----")
# 用 `for + range` 打印 1 到 20 的所有奇数
l1 = list(range(1, 21))
for item in l1:
  if item % 2 != 0:
    print(f"{item}是奇数")
  
# 给定 `["周一","周二","周三"]`，用 `enumerate` 打印 `1. 周一`、`2. 周二`、`3. 周三`。
l2 = ["周一","周二","周三"]

for i, item in enumerate(l2, start=1):
  print(f"{i}.{item}")

# 写一个 while：从 10 开始每次减 3，直到小于 0，打印每一步。
count = 10
while count > 0:
  print(f"当前count为{count}")
  count -= 3
  print(f"减去3后count为{count}")

# 写 FizzBuzz：1 到 15，3 的倍数打 Fizz，5 的倍数打 Buzz，都打 FizzBuzz
FizzBuzz = list(range(1, 16))
for item in FizzBuzz:
  if item % 3 == 0:
    print("Fizz")
  if item % 5 == 0:
    print("Buzz")
  print("FizzBuzz")

print("---- 课后作业 ----")

# 用 `for + range` 打印 1 到 100 的所有奇数

l1 = list(range(1, 101))
for item in l1:
  if item % 2 != 0:
    print(f"{item}是奇数")

# 用 `while` 实现：从 100 不断减 7，直到小于 0，打印每一步。
count = 10
while count >= 0:
  print(f"当前count为{count}")
  count -= 7
  print(f"减去3后count为{count}")

# 给定列表 `[3, 7, 2, 9, 5]`，用 `enumerate` 打印 "第 i 个元素是 x"（序号从 1 开始）
l2 = [3, 7, 2, 9, 5]
for i, item in enumerate(l2, start=1):
  print(f"第{i}个元素是{item}")

# 找列表 `[12, 5, 8, 130, 44]` 中的最大值（先自己写循环，再用内置 `max` 验证）
l3 = [12, 5, 8, 130, 44]
maxNum = 0
for i, item in enumerate(l3):
  if item > maxNum:
    maxNum = item
print(f"最大值为{maxNum},{max(l3) == maxNum}")

# 用 `continue` 打印 1 到 20 中所有不能被 3 整除的数
l4 = list(range(1, 21))
for item in l4:
  if item % 3 == 0:
    continue
  print(f"{item}不能被3整除")

# 用 `break` 在字符串 `"python"` 中找到字母 `"t"` 就停止遍历并打印 "找到了"。
for item in "python":
  if item == "t":
    print("找到了")
    break

nums = [1,2,3]
codes = ["a","b","c"]
obj = {}
for num, code in zip(nums, codes):
  obj[num] = code

print(obj)

# FizzBuzz：1 到 30，被 3 整除打 Fizz，被 5 整除打 Buzz，都整除打 FizzBuzz，否则打印数字
l5 = list(range(1, 31))

for item in l5:
  if item % 3 == 0 and item % 5 == 0:   # 必须先判断"都整除"（即 15 的倍数），否则会被下面的分支提前截走
    print("FizzBuzz")
  elif item % 3 == 0:                  # 用 elif 而不是 if，保证同一轮只走一个分支
    print("Fizz")
  elif item % 5 == 0:
    print("Buzz")
  else:                                # 都不满足才打印数字本身
    print(item)
