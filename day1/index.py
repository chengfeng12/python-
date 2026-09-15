print("Hello Python")
name = "前端工程师"

if name:
  print(name)
else:
  print("name is empty")

age = 28
if age >= 18:
  print("我是一个成年人")
else:
  print("我是一个未成年人")

print("1", "2", "3", sep = "|")

print(type(1))

type1 = type(1)          # <class 'int'> —— 查看类型，比 JS 的 typeof 更准
dir1 = dir("abc")       # 列出字符串能用的所有方法
# help1 = help(str.upper)  # 就地查某个方法的文档，按 q 退出帮助
print("abc".upper())   # ABC —— 现学现用

print(type(1), type(1.0), type("x"), type(True), type(None))

total = 1234 * 5678
print(type(total))