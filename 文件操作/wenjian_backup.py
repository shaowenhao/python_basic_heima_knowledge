# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/23/2023 2:58 PM
# 文件名称: wenjian_backup.PY

#打开文件得到 文件对象 准备读取
fr = open("d:/test.txt","r",encoding="UTF-8")
# 打开文件得到文件对象 准备写入
fw = open("d:/test.bak","w",encoding="UTF-8")
# for循环读取文件
for line in fr:
    line = line.strip()
#判断内容 将满足的内容写出
    if line.split(",")[2] == "测试":
        continue
    fw.write(line)
    fw.write("\n")
#close2个文件对象、

fr.close()
fw.close()