print("----Part 1・文件读写----")
with open("test.txt", "w", encoding="utf-8") as f:
  f.write("Hello, world!\n")
  f.write("第二行!")

# **为什么用 with**：它会自动帮你 `f.close()`，哪怕中途报错也会关文件。不用 with 就得手动 close，忘了就泄露资源。对应 JS 的 `fs.open` 但更安全。
# `"w"`写入**覆盖原文件**，没有就新建`"r"`读取文件不存在会报错`"a"`追加在末尾追加，不覆盖

# 三种读取方式
with open("test.txt", "r", encoding="utf-8") as f:
  content = f.read()
  print(content)

print("----")
with open("test.txt", "r", encoding="utf-8") as f:
  for line in f:
    print(line.strip()) # strip() 去掉每行末尾的 \n
    print(line)

# 两个必记
# 1. **`encoding="utf-8"` 必须写**。中文环境不指定会乱码（Windows 默认用 GBK）。
# 2. **`\n` 是换行符**。`write("第一行\n")` 才会换行，不写 `\n` 所有内容挤在一行。

print("----Part 2・异常处理 try/except----")

# - Python 是 `try/except`，JS 是 `try/catch`
# - Python 按**异常类型**精确捕获，JS 的 catch 不分类
# - `except ValueError` 只抓类型错误，其他错误照样抛
try:
  n = int("abc") # 报错是可以拦截，只抓类型错误，其他错误照样抛
  n2 = init("abc") # 报错之后，下面的代码是不会执行的，这个没有执行, NameError 会捕获这个
except ValueError as err:
  print(f"转换失败{err}")
except NameError as err:
  print(f"未定义变量{err}")



try:
  result = 10 / 2
except ZeroDivisionError: # 除零错误
  print("除零")
else:
  print("成功，结果是", result)   # try 没报错才走这里
finally:
  print("无论如何都执行")          # 清理资源，必走


try:
  d = {"a": 1}
  print(d["b"])
except KeyError as e:
  print("键不存在:", e)
except Exception as e:
  print("其他错误:", e)

print("----Part 3・常见异常类型----")

# 异常什么时候触发例子 
# `ValueError`值不对`int("abc")`
# `ZeroDivisionError`除零`1/0`
# `KeyError`dict 键不存在`d["不存在"]`
# `IndexError`列表越界`[1,2][5]`
# `FileNotFoundError`文件不存在`open("不存在.txt")`
# 不确定什么异常就用 `except Exception` 兜底，但**不要滥用**—— 精确捕获比一把抓好，否则会把你没预料到的 bug 也吞掉。

print("----随堂练习----")
# 用 with 写一个 `notes.txt`，写入三行你今天学的内容。
with open("notes.txt", "w", encoding="utf-8") as f:
  f.write("文件读写\n")
  f.write("异常处理\n")
  f.write("常见异常类型")

# 读取 `notes.txt` 并逐行打印。
with open("notes.txt", "r", encoding="utf-8") as f:
  print(type(f)) # <class '_io.TextIOWrapper'>
  for line in f:
   print(line.strip())

# 写一个 try/except：输入一个字符串转 int，转换失败时打印 "请输入数字"。
try:
  n = int("abc")
except ValueError as err:
  print("请输入数组")

print("----Day 7 课后作业----")

# 用 with 写文件 `todo.txt`，写入三行待办事项。
with open("todo.txt", "w", encoding="utf-8") as f:
  f.write("1. 吃饭\n")
  f.write("2. 洗澡\n")
  f.write("3. 睡觉")

# 读取 `todo.txt`，逐行打印（用 for line in f）。
with open("todo.txt", "r", encoding="utf-8") as f:
  for line in f:
    print(line.strip())

# 用 `"a"` 模式往 `todo.txt` 追加一行新待办，再读一次确认。
with open("todo.txt", "a", encoding="utf-8") as f:
  f.write("4. 打游戏")
with open("todo.txt", "r", encoding="utf-8") as f:
  for line in f:
    print(line.strip())

# 写一个 try/except：尝试 `int("hello")`，捕获 ValueError 并打印 "不是数字"。
try:
  n = int("hello")
except ValueError as err:
  print("不是数字")

num = 10
try:
  num = 100 / 2
except ZeroDivisionError as err:
  print("除零")
else:
  print("成功，结果是", num)
finally:
  print("计算结束")


print(num) # 同一个作用域

# 写一个函数 `safe_divide(a, b)`，返回 `a/b`，如果 b=0 返回 None 而不是报错（用 try/except）。
def safe_divide(a, b):
  try:
    return a / b
  except ZeroDivisionError as err:
    return None

print(safe_divide(6, 2))
print(safe_divide(6, 0))