# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/12/2023 5:56 PM
# 文件名称: if_elif_else.PY

heigh = int(input("输入升高"))
vip = int(input("输入VIP等级"))

if heigh < 120:
    print("可以免费")
elif vip > 10:
    print("也可以免费")
else:
    print("2个条件都不满足 不免费")
