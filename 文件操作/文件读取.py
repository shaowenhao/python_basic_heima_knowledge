# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/22/2023 5:05 PM
# 文件名称: 文件读取.PY

f = open("D:/PycharmProjects/bookLearn/test.txt","r",encoding="UTF-8")
print(type(f))

# print(f"文件读取3个字节{f.read(3)}")
# print(f"文件读取全部内容{f.read()}")

#d读取文件的全部行 封装到列表中 打开了文件上面9-10行代码已经读完了
# lines = f.readlines()
# print(f"{type(lines)}")
# print(f"{lines}")

# 读取文件 readline
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(line1)
# print(line2)
# print(line3)

# for循环读取文件 包含了换行符， 有需要逐行处理的时候先去掉收尾的换行符
for line in f:
    print(line)


#文件的关闭
f.close()

# with open 语法操作文件 自动关闭文件
with open("D:/PycharmProjects/bookLearn/test.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(line)

