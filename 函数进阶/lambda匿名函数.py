# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/22/2023 1:49 PM
# 文件名称: lambda匿名函数.PY

'''
def关键字 可以定义带名称的函数 重复使用
lambda关键字 可以定义匿名函数 临时使用一次

语法：
lambda 传入参数：函数体 （一行代码）
'''


#定义一个函数 接受其它函数输入
def test_func(computer):
    result = computer(1, 2)
    print(result)

#通过lambda匿名函数的形式 将匿名函数作为参数传入
test_func(lambda x,y: x + y)

