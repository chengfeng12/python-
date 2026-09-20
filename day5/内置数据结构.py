print("----Part 1・list（数组）----")
arr = [3,1,4,1,5,1,1]
# copy 数组
arr2 = arr.copy()

# 末尾加一个
arr.append(9)
# 末尾加多个（等价 +=）
arr.extend([2, 6])
# 在位置索引为 0的位置 插入 0
arr.insert(0, 0)
arr.insert(1, 100)
# 删除第一个值为 1 的元素（按值删除，不是按位置删除）
arr.remove(1)
# 删除末尾元素并返回它
result = arr.pop()
# 原地排序（返回None）, 数字按数值，字符串按字典序
# arr.sort()
# 返回新排序列表，原list不变
newArr = sorted(arr)
# # 找100的下标  和 string 中的方法一致
print(arr.index(100))
# 数1出现几次，和 string 中的方法一致
print(arr.count(1))

print(f"newArr--{newArr}")
print(f"{result}删除的值-pop")
print(arr)
print(len(arr))

print(arr2)

### 三个易错点

# 1. **`sort()` vs `sorted()`**：`list.sort()` 原地排序返回 None；`sorted(list)` 返回新列表。和 JS 的 `arr.sort()`（原地）不一样，JS 没有返回新数组的版本。
# 2. **`remove(x)` 按值删，只删第一个**；要按位置删用 `pop(i)`。
# 3. **拷贝用切片** `lst[:]`（Day 2 讲过引用问题），别直接 `y = lst`。

print("----Part 2・tuple（不可变列表----")
# tuple 就是**不可变的 list**。什么时候用？

# - 函数返回多个值时（`divmod(10,3)` 返回 `(3,1)`，本质是 tuple）。
# - 不希望被改的数据（坐标、配置项）。
# - dict 的键、set 的元素必须是不可变类型（tuple 可以，list 不行）。
t = (1, 2, 3)
t[0] # 1
# t[0] = 99  # TypeError，不能改 TypeError: 'tuple' object does not support item assignment

a, b, c = t
print(a, b, c)   # 10 20 30

a = 20
print(t)

print("----Part 3・dict（字典，和 JS 对象最像----")

# d = { name: "张三", age: 18 } # 会报错，要写成下面的格式 NameError: name 'name' is not defined
d = { "name": "张三", "age": 18 } 
print(d["name"])
print(d.get("score"))      # None（不存在不报错！对应 JS d.score ?? undefined）)
d["city"] = "上海"   # 新增
del d["age"]        # 删除
d["name"] = "李四"
print(d)
# print(d['sex']) # 直接报错，写成下面的格式
print(d.get("sex")) # None
d.update({"name": "大明", "job": "工程师"})  # 批量更新

# 三个遍历方法

# 和 key in d.keys() 效果一样
for key in d:
  print(f"key--{key}")

for value in d.values():
  print(f"value--{value}")

for key, value in d.items():
  print(f"key--{key}------value--{value}")

### 两个关键区别（vs JS 对象）

# 1. **`d["key"]` vs `d.get("key")`**：键不存在时 `d["key"]` 直接 KeyError 报错；`d.get("key")` 返回 None。**不确定键是否存在时一律用 `.get()`**。
# 2. **遍历 dict 用 `.items()`**：`for k, v in d.items()` 一次拿键值。JS 是 `Object.entries(d)`，Python 更直接。

print("-----Part 4・set（集合，去重神器）------")
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1 & s2) # 交集 
print(s1 | s2) # 并集
print(s1 - s2) # 差集

print(list(set([1,1,2,2,3,3])))   # [1,2,3]  去重

# set 就是 JS 的 Set。两个高频用途：

# - **去重**：`list(set(lst))` 一行搞定（但会丢失顺序，Python 3.7+ dict 保序，set 不保序）。
# - **集合运算**：判断两个列表有没有共同元素、差集，用 `&` `|` `-` 比写循环优雅得多

arr1 = [3,1,4,1,5,1,1]
arr2 = [3,1,4,1,5,1,1]
print(arr1 == arr2)


print("----Part 5・列表推导式----")
# [表达式  for  变量  in  可迭代  if  条件 ]

# 这是 Python 最具辨识度的语法，**一行替代 JS 的 map + filter**。
# 生成 0-4 的平方
squares = [x*x for x in range(5)]
print(f"squares--{squares}")

# 只取偶数
events = [x for x in range(10) if x % 2 == 0]
print(f"events--{events}")

pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(f"pairs--{pairs}")
# **什么时候用推导式**：短平快的列表生成就用它；逻辑复杂（多层嵌套、多个 if）就别硬写推导式，老老实实写 for 循环，可读性更重要。

print("----Part 6・字典推导式 + 解包----")
d2 = {k: v * 2 for k, v in {"a":1, "b":2}.items()}
print(d2)

# 解包（* 展开）
first, *rest = [1, 2, 3, 4, 5]
# first=1, rest=[2,3,4,5]

a, b, *_, last = [1, 2, 3, 4, 5]
# a=1, b=2, last=5, _ 吞掉中间不要的
# `*rest` 类似 JS 的 `...rest`，把剩余元素收成列表。`*_` 是约定俗成的 "我不关心这些值"。

print("----随堂练习----")
# 用推导式生成 1 到 10 的平方列表。
print([x * x for x in range(1, 11)])
# 用 dict 存三个人的分数 `{"小明": 90, "小红": 85, "小刚": 78}`，求平均分。
d2 = {"小明": 90, "小红": 85, "小刚": 78}
num = 0
for v in d2.values():
  num += v

print((num / len(d2)))
# 用 set 给 `[1,2,2,3,3,3,4]` 去重。
print(set([1,2,2,3,3,3,4]))
print(list(set([1,2,2,3,3,3,4])))

# 用 `first, *rest` 把列表分成第一个和其余。
first, *other = d2.keys()
print(first)
print(other)

print("----Day 5 课后作业----")
# 给定列表 `[5, 2, 9, 1, 5, 6]`，用两种方式排序：① 原地排序后打印；② 用 `sorted()` 不修改原列表。
arr3 = [5, 2, 9, 1, 5, 6]
arr3.sort()
newArr3 = sorted(arr3)
print(arr3, newArr3)

# 用 `append` 和 `extend` 分别操作，说明结果区别。
arr3.append(100)
print(arr3) # 单个追加

arr3.extend([101, 102]) # 多个追加
print(arr3)

# 用 dict 存 `{"a":1, "b":2, "c":3}`，用 `.items()` 遍历打印每对键值。
dic = {"a":1, "b":2, "c":3}
for k, v in dic.items():
  print(k, v)

# 用 `.get()` 安全获取键 `"d"`（不存在），打印结果（应返回 None 不报错）。
print(dic.get("d")) # None

# 两个列表 `[1,2,3,4]` 和 `[3,4,5,6]`，用 set 求交集、并集、差集。
arr4 = [1,2,3,4]
arr5 = [3,4,5,6]
print(set(arr4) & set(arr5))
print(set(arr4) | set(arr5))
print(set(arr4) - set(arr5))

# 用列表推导式：① 生成 1–20 中所有偶数；② 把 `["hello","world","python"]` 每个转大写。
print([x  for x in range(1, 21) if x % 2 == 0])
print([x.upper() for x in ["hello","world","python"]])

# 用字典推导式：把 `{"a":1, "b":2, "c":3}` 的值全部平方。
print({k: v * v for k, v in {"a":1, "b":2, "c":3}.items()})


# 给定 `nums = [10, 20, 30, 40, 50]`，用解包取出第一个、最后一个、和中间剩余部分。
nums = [10, 20, 30, 40, 50]

first, *other, last = nums
print(first, other, last)