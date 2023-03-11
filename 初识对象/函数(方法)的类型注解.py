# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 3/1/2023 8:36 AM
# 文件名称: 函数(方法)的类型注解.PY

'''
函数和方法的形参类型注解语法：
    def 函数方法名(形参名：类型，形参名：类型...)
        pass
'''

#对参数进行类型注解
from typing import Union


def add(x:int,y:int):
    return x + y


print(add(1, 2))

#对返回值进行类型注解
def fun(data:list) -> list:
    return data


# Union联合类型注解
my_list:list[Union[int,str]] = [1,2,"abc","def"]

def func(data:Union[int,str]) -> Union[int,str]:
    pass

func()








