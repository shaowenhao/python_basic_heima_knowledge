# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/16/2023 1:51 PM
# 文件名称: 集合.PY


'''
集合 是无序的  不支持下标索引访问
和列表一样 允许修改的


可以容纳多个数据，且不同类型
不允许重复数据
可以修改
支持for循环
'''
my_set = {"aa","bb","cc","bb"}
my_set_empty = set()
print(f"my_set的内容是：{my_set},类型是:{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty},类型是:{type(my_set_empty)}")


my_set.add("dd")
print(my_set)

#删除指定数据
my_set.remove("aa")
print(my_set)

#随即取出一个元素
element = my_set.pop()
print(my_set)

my_set.clear()
print(my_set)

#取2个集合的差集 集合1里有集合2里没有的
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(set3)

#集合合并为一个集合 unior
