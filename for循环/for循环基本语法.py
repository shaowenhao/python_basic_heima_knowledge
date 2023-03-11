# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/12/2023 7:49 PM
# 文件名称: for循环基本语法.PY

"""
for 临时变量 in 待处理数据集 （序列）：
    循环满足条件时执行的代码
"""

name = "items"

for x in name:
    # 将name的内容 挨个取出赋值于临时变量
    # 就可以在循环体对x进行处理
    print(x)
