# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/16/2023 4:00 PM
# 文件名称: caozuo.PY

my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = "abcde"

my_set = {1,2,3,4,5}
my_dict = {"key1":1,"key2":2,"key3":3}

#len元素个数
print(len(my_list))
print(len(my_tuple))
print(len(my_set))
print(len(my_set))
print(len(my_dict))


# max 最大元素
print(max(my_list))
print(max(my_tuple))
print(max(my_str))
print(max(my_set))
print(max(my_dict))


# 类型转换 容器转列表
print(list(my_list))
print(list(my_tuple))
print(list(my_str))
print(list(my_set))
print(list(my_dict))

# 容器 转元组
print(tuple(my_list))
print(tuple(my_tuple))
print(tuple(my_str))
print(tuple(my_set))
print(tuple(my_dict))

# 容器转 字符串
print(str(my_list))
print(str(my_tuple))
print(str(my_str))
print(str(my_set))
print(str(my_dict))

# 排序 sorted(容器，[reverse=true]) 有序列表
my_list = [5,2,3,4,1]
my_tuple = (1,5,3,4,2)
my_str = "cbade"

my_set = {1,2,5,4,3}
my_dict = {"key3":1,"key2":2,"key1":3}

print("=============")
print(sorted(my_list))
print(sorted(my_tuple))
print(sorted(my_str))
print(sorted(my_set))
print(sorted(my_dict))
