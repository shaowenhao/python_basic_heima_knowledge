# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 3/10/2023 3:31 PM
# 文件名称: 基础匹配.PY

'''
re模块的3个主要方法
match 从头开始匹配 匹配第一个命中项
search 全局匹配 匹配第一个命中项
findall 全局匹配 匹配全部命中项
'''

import re

s = "python itheima"

#从头部匹配
result = re.match("python",s)
print(result)
print(result.span())
print(result.group())

# 整个字符串搜索 找到以后就停下
result = re.search("python",s)
print(result)


result = re.findall("python",s)
print(result)

