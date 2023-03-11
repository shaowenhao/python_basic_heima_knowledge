# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/15/2023 6:32 PM
# 文件名称: list列表常用操作.PY

'''
列表可以容纳多个元素
可以容纳不同类型的元素
数据是有序存储的 有下标序号
允许重复元素存在
可以修改
'''

mylist = ["abc","def","python"]

# 下标
index = mylist.index("python")
print(f"下标是{index}")

#修改
mylist[0] = "java"
print(mylist)

# 插入
mylist.insert(1,"go")
print(mylist)

mylist.append("c#")
print(mylist)


#追加一批元素的方法
mylist.extend([1,2,3])
print(mylist)


# 删除的方式
mylist = [1,2,3]
del mylist[2]
print(mylist)

mylist = [1,2,3]
element = mylist.pop(2)
print(f"{mylist}去掉的元素是：{element}")


#删除某元素再列表中的第一个匹配项
mylist = [1,2,3,2,3]
mylist.remove(2)
print(mylist)

#情况列表
mylist = [1,2,3]
mylist.clear()
print(mylist)

mylist = [1,2,3,3,3,4]
num = mylist.count(3)
print(num)

len = len(mylist)
print(len)