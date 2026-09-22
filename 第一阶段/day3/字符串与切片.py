s1 = '单引号'        # 单双引号完全等价，不像 JS 有微妙区别
s2 = "双引号"
s3 = """第一行        # 三引号 = 多行字符串（对应 JS 的反引号模板，但不插值）
第二行
第三行"""
print(s1, s2, s3, sep="\n")
print('它说: "你好"')  # 单引号里可以直接写双引号，不用转义

arr1 = [1,2]
arr1[0] = 3 # 可以直接修改
# s1[0] = "X" # 直接报错 'str' object does not support item assignment

print(arr1, s1, sep="、")

print("----模板字符串----")

name, score = "小明", 95.5

print(f"姓名：{name}, 分数：{score}")

print("----四种高频格式控制----")

# 格式语法记忆：`{变量:填充对齐 宽度 . 精度 类型}`，比如 `{'5':0>3}` 表示用 `0` 填充、`>` 右对齐、宽度 3。
# 日常记住 `:.2f`（小数）、`:,`（千分位）、`:.1%`（百分比）三个就够覆盖 90% 场景

print(f"{'5':0>3}")        # 005        ← 左补零到3位（编号、序号超好用）
print(f"{'5':0<3}")        # 500        ← 右补零到3位（编号、序号超好用）
print(f"{0.25:.1%}")       # 25.0%      ← 百分比
print(f"{1234567:,}")      # 1,234,567  ← 千分位
print(f"{3.14159:.2f}")    # 3.14       ← 保留2位小数
print(f"{3.14559:.2f}")    # 3.15       ← 保留2位小数 --- 四舍五入


print("----索引与切片-----")
# 三个必记要点

# 1. **左闭右开**：`s[1:4]` 取的是下标 1、2、3，**不含 4**。这和 JS 的 `slice(1,4)` 行为一致。
# 2. **越界不报错**：切片索引超出范围会自动截断，不会像 `s[100]` 那样报 IndexError。所以 `s[3:100]` 是安全的。
# 3. **`s[::-1]` 是反转字符串的经典一行写法**，面试高频。JS 要写 `s.split('').reverse().join('')`，Python 一行搞定。

# > 
# > 🧠 切片返回的是**新对象**（新字符串 / 新列表），不修改原对象 —— 这也符合不可变 / 不原地修改的哲学。

s = "abcdef"
print(s[0])      # a      正向索引，从0开始
print(s[-1])     # f      负索引，-1是倒数第一个
print(s[1:4])    # bcd    左闭右开：取下标1、2、3（不含4）
print(s[-1:4])   # 啥也没有
print(s[:3])     # abc    start省略=从头
print(s[3:])     # def    stop省略=到尾
print(s[::2])    # ace    step=2，每隔一个取
print(s[::-1])   # fedcba step=-1，从右往左 = 反转！


print("-----常用方法-----")
# 方法	作用	JS 对应
# .strip()	去首尾空白	.trim()
# .split(",")	按分隔符切成列表	.split(",")（同名）
# "-".join(list)	用分隔符把列表拼成字符串	.join()（但调用者不同，见下）
# .replace("l","L")	替换	.replace()（同名）
# .find("x")	找子串位置，找不到返回 -1	.indexOf()
# .startswith("https")	是否以某串开头	.startsWith()
# .endswith(".py")	是否以某串结尾	.endsWith()
# .upper() / .lower()	大小写	.toUpperCase() / .toLowerCase()
# .count("s")	子串出现次数	JS 无直接对应
# .isdigit()	是否全是数字	需正则

print(" abc ".strip()) # abc 类似 js trim
print("-".join("abc")) # a-b-c
print("abc".upper()) # ABC
print("ABC".lower()) # abc
print("abc".startswith("a")) # True
print("abc".endswith("c")) # True
print("abc".find("b")) # 1  js 中 indexOf 返回 -1
print("abcb".find("b")) # 1  只返回符合条件的第一个下标
print("abcb".find("e")) # -1  没有找到返回 -1
print("abc".replace("b", "B")) # aBc
print("abcb".replace("b", "B")) # aBcB 类似 js 中的 replaceAll
print("abc".split(",")) # ['abc']
print("a,b,c".split(",")) # ['a', 'b', 'c']
print("abaac".count("a")) # 3
print("332323".isdigit()) # True
print("aa2323".isdigit()) # False


print("----编码----")
# - Python 3 的字符串是 **Unicode**，一个中文就是一个字符（`len("你好")=2`），不存在 JS 里某些 emoji 长度为 2 的代理对问题（Python 也有少数极端情况，但日常不用管）。
# - `.encode("utf-8")` 把字符串转成字节（`bytes`，用于网络传输、文件写入）；`.decode("utf-8")` 反向。
# - 读写文件时指定 `encoding="utf-8"`（Day 24 会细讲），中文环境不指定会乱码。

print(ord("A"))    # 65      字符→Unicode码点
print(chr(65))     # A       码点→字符
print("你好".encode("utf-8"))  # b'\xe4\xbd\xa0\xe5\xa5\xbd'  字符串→字节


# 1. 用 f-string 输出：`今天气温 23.456 度，保留 1 位小数`（结果应为 `今天气温 23.5 度`）。
wendu = 23.456
print(f"今天气温{wendu:.1f}")
# 2. 用切片取出 `"abcdef"` 的后 3 个字符，再把整个字符串反转。
print("abcdef"[3:][::-1])
# 3. 验证 `s[0] = "x"` 报错，再用 `s = "x" + s[1:]` 修正。
s = "abcdef"
# s[0] = "x"
s = "x" + s[1:]
print(s) # xbcdef 替换了 a，类似 js 中的 splice(index, 1, "x")
# 4. 把 `"  hello world  "` 去首尾空格并转大写。
print("  hello world  ".strip())


print("----课后作业----")

# 1. 用 f-string 输出：今天气温 23.456 度，保留 1 位小数。
wendu = 23.456
print(f"今天气温 {wendu:.1f}")
# 2. 给定 `"  hello world  "`，去掉首尾空格，并把它整体大写。
s = "  hello world  "
print(s.strip().upper())
# 3. 把 `"a,b,c,d"` 按逗号切成列表，再用 `"-"` 拼回 `"a-b-c-d"`。
s2 = "a,b,c,d"
print("-".join(s2.split(",")))
# 4. 用切片取出字符串 `s` 的后 3 个字符；再把 `s` 反转。
str = "abcdeshjk"
print(str[-3:][::-1])
# 5. 判断字符串 `url` 是否以 `"https://"` 开头，是否包含 `"python"`。
link = "https://baidu.com"
print(link.startswith("https://"))
# 6. 统计一句英文中字母 `e` 出现的次数（提示：`.count()`）。
h = "hello world"
print(h.count("e"))
# 7. 输入 `"2026-09-15"`，用切片分别取出年、月、日。
date = "2026-09-15".split("-")

print(f"年{date[0]},月 {date[1]},日{date}")
# 8. 解释为什么执行 `s = "abc"; s[0] = "x"` 会报错，正确的 "修改" 姿势是什么？
# 因为字符串是不可变对象，正确修改方式是
s = "abc"
s = "x" + s[1:]
print(s)