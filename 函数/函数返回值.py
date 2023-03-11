# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/15/2023 3:44 PM
# 文件名称: 函数返回值.PY

def add(a,b):
    '''
    函数说明文档 加法方法
    :param a: 一个数字
    :param b: 另一个数字
    :return:  返回两数字的和
    '''
    result = a + b
    return result

sum = add(1,2)
print(f"和是{sum}")

