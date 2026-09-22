print("-----阶段一项目实践：命令行通讯录-----")
import os
fileName = "userList.txt"
def initFile():
  if not os.path.exists(fileName):
    with open(fileName, "w", encoding="utf-8") as f:
      pass
    print("userList.txt 不存在，已自动创建")
  else:
    print("userList.txt 已存在，直接使用")
initFile()

def checkParams(*args):
  name, tel = args
  if bool(name) == False:
    print("姓名不能为空！")
    return False
  if bool(tel) == False:
    print("电话不能为空！")
    return False

  return True

def addUser(*args):
  name, tel = args
  if checkParams(name, tel) == False:
    return
  if checkUser(tel):
    print(f"{name}该用户已存在，无需重复添加！")
    return
  with open(fileName, "a", encoding="utf-8") as f:
    f.write(f"{name},{tel}\n")
    print(f"名字：{name}，电话：{tel}， 添加成功")

def delUser(*args):
  name, tel = args
  # 1. 参数校验  
  if checkParams(name, tel) == False:
    return

  # 2. 先确认存在，不存在就没必要走后面流程
  if checkUser(tel) == False:
    print("该用户不存在，无法删除！")
    return

  # 3. 读出全部行
  with open(fileName, "r", encoding="utf-8") as f:
    lines = f.readlines()

  # 4. 过滤：命中目标的行丢弃，其余保留
  kept = []
  for line in lines:
    user = line.strip().split(",")
    if tel == user[1]:
      continue
    kept.append(line)

  # 5. 重写
  with open(fileName, "w", encoding="utf-8") as f:
    # f.writelines(kept) 等价下面
    for line in kept:
      f.write(line)

  print(f"名字：{name}，电话：{tel}， 删除成功")

def findUser(*args):
  name, tel = args
  if checkParams(name, tel) == False:
    return
  if checkUser(tel) == False:
    print("该用户不存在，无法查找！")
    return
  with open(fileName, "r", encoding="utf-8") as f:
    for line in f:
      user = line.strip().split(",")
      if tel == user[1]:
        print(f"名字：{user[0]}，电话：{user[1]}， 查找成功")
        return

def checkUser(tel):
  with open(fileName, "r", encoding="utf-8") as f:
    for line in f:
      print(line)
      user = line.strip().split(",")
      if tel == user[1]:
        return True
  return False


addUser("尹天雪", "15638331204")
findUser("尹天雪", "15638331204")
delUser("尹天雪", "15638331203")

