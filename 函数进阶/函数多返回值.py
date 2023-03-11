# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/17/2023 10:44 AM
# 文件名称: 函数多返回值.PY

def test_return():
    return 1,"aa",True

x,y,z = test_return()
print(x)
print(y)
print(z)