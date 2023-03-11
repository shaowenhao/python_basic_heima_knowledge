# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/13/2023 1:01 PM
# 文件名称: 循环中断.PY

# for i in range(1,6):
#     print("语句1")
#     continue
#     print("语句2")


# continue嵌套

# for i in range(1,6):
#     print("语句1")
#     for j in range(1,6):
#         print("语句2")
#         continue
#         print("语句3")
#     print("语句4")
#

# break嵌套应用
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        break
        print("语句3")
    print("语句4")