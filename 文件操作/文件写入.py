# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/23/2023 2:33 PM
# 文件名称: 文件写入.PY

# 打开文件 不存在的文件 w模式 文件不存在会创建，文件存在 清空原有内容
f = open("D:/test.txt","w",encoding="UTF-8")

# write写入
f.write("hello python")

f.flush()

f.close()  # close方法内置 flush的功能

