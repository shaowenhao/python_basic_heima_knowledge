# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/15/2023 3:49 PM
# 文件名称: None.PY

def say_hi():
    print("hello")

result = say_hi()
print(f"无返回值函数，返回的内容是{result}")
print(f"无返回值函数，返回的内容类型是是{type(result)}")

# None用于if判断
'''
在if判断中 None等同于Fasle
一版用于在函数中主动返回None 配合if判断做相关处理
'''

def check_age(age):
    if age > 18:
        return "Success"
    else:
        return None
result =  check_age(16)
if not result:
    #进入if 表示result是None 也就是False
    print("未成年，不可以进入")


# None用于声明无初始化内容的变量
name = None


