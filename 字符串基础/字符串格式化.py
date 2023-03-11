# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/12/2023 2:58 PM
# 文件名称: 字符串格式化.PY


# % 表示 我要占位
# s 表示将字符串放入占位的地方

# 拼接用的 % 不再是 + name繁琐 且 + 仅限于字符串之间拼接
name = "黑马程序员"
message = "学IT就来 %s" % name
print(message)


# 这么写其实数字类型转成了字符串
class_num = 10
id = 1001
message = "%s 班 学号%s 的同学" % (class_num,id)
print(message)


"""
%s 
%d  将内容转换成整数，放入占位符
%f  将内容转换成浮点型
"""

class_num = 10
id = 1001
message = "%d 班 学号%d 的同学" % (class_num,id)
print(message)