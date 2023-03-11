# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/22/2023 7:53 PM
# 文件名称: 文件读取联系.PY

f = open("D:/PycharmProjects/bookLearn/test.txt","r",encoding="UTF-8")

# 读取全部内容 通过字符串count方法统计 单次出现的次数
# content = f.read()
# count = content.count("aaa")
# print(f"aaa出现的次数：{count}")

# 读取内容 一行一行读取
count = 0
for line in f:
    line = line.strip() # 去掉开头和结尾的空格以及换行符
    words = line.split(" ")
    for word in words:
        if word == "aaa":
            count += 1
print(f"aaa出现的次数{count}")
f.close()