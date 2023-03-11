# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/22/2023 1:32 PM
# 文件名称: 函数作为参数传递.PY

#定义一个函数 接收另一个函数作为传入参数
def test_func(computer):
    result = computer(1,2)
    print(f"computer参数的类型是：{type(computer)}")
    print(result)

#定义一个函数 准备作为参数 传入另一个函数
def computer(x,y):
    return x + y

#调用 并传入函数
test_func(computer)
