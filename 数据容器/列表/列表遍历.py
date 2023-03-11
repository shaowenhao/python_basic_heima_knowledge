# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/15/2023 6:58 PM
# 文件名称: 列表遍历.PY

def list_while_func():
    my_list = [1,2,3,4]
    index = 0
    while index < len(my_list):
        element = my_list[index]
        index += 1
        print(element)

def list_for_func():
    my_list = [6,7,8,9]
    for i in my_list:
        print(i)

# list_while_func()
list_for_func()
