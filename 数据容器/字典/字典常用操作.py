# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/16/2023 3:29 PM
# 文件名称: 字典常用操作.PY


'''
可以容纳多个数据 ， 且不同类型
每一分数据都都是keyValue
可以通过key获得value key不可以重复
不支持下标索引
可以修改
支持for
'''
my_dict = {"ryan":100,"iris":110}

#新增元素
my_dict["junbao"] = 120
print(my_dict)

# pop 删除，也可以得到删除的值
score = my_dict.pop("junbao")
print(f"{score},{my_dict}")

#获取全部key
keys = my_dict.keys()
print(f"keys的内容{keys},类型{type(keys)}")

#遍历字典 通过获取到全部的key来完成
for key in keys:
    print(f"字典的key是:{key}")
    print(f"字典的value是:{my_dict[key]}")


#方式2：直接对字典进行for循环变量 每一次循环都是直接得到key
for key in my_dict:
    print(f"字典的key是:{key}")
    print(f"字典的value是:{my_dict[key]}")


