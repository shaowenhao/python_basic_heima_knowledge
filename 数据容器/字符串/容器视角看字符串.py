# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/16/2023 10:49 AM
# 文件名称: 容器视角看字符串.PY

'''
只可以存储字符串
长度任意 取决于内存大小
支持下标索引
允许重复字符串
不可以修改
支持for
'''

# 通过下标索引取值
my_str = "hello python"
value = my_str[4]
print(value)

# 字符串无法修改

# index方法
index = my_str.index("python")
print(index)

#replace方法
str2 = my_str.replace("python","Java")
print(str2)

# split 分割存入列表
list = my_str.split(" ")
print(f"list的类型{type(list)}内容是：{list}")

#字符串的规整操作
#str.strip() 去前后空格
#str.strip(字符串) 去前后指定字符串

my_str = "12hello world21"
print(my_str.strip("12"))