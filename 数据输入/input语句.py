# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/12/2023 4:48 PM
# 文件名称: input语句.PY

# print("who you are")
name = input("who you are?")
print("ni shi: %s" % name)

# input 认为传入的数据是字符串
num = input("你的密码:")
print("你的密码类型：", type(num))

#可以转换
num = input("你的密码again:")
num = int(num)
print("你的密码类型：", type(num))