# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/16/2023 1:07 PM
# 文件名称: 序列.PY

'''
序列是指：内容连续 有序 可使用下标索引的一类数据容器
列表，元组，字符串 均可以视为序列
'''

# 切片
my_list = [0,1,2,3,4,5,6]
newList = my_list[1:4]
print(newList)


my_tuple = (0,1,2,3,4,5)
newTuple = my_tuple[:]
print(newTuple)

my_str = "0123456"
newStr = my_str[::2]
print(newStr)

# 反向切片 等同于序列翻转
my_str = "0123456"
newStr = my_str[::-1]
print(newStr)

my_list = [0,1,2,3,4,5,6]
newList = my_list[3:1:-1]
print(newList)

my_list = "123456"
newList = my_list[:-2]
print(newList)