# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/23/2023 7:24 PM
# 文件名称: 模块.PY

'''
模块 Module 是一个Python文件 以.py结尾
模块能定义 函数 类 和变量 模块里也能包含可执行的代码
看做一哥工具包


模块的导入方式
[from 模块名] import [模块|类|变量|*] [as 别名]

import 模块名
from 模块名 import 类，变量，方法等
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名
'''


# import time
# time.sleep(10)

# 使用from导入time的sleep功能
# from time import sleep
# sleep(10)


# 使用 * 导入time模块的全部功能
# from time import *
# sleep(10)


#使用as给特定功能加上别名
import time as t
t.sleep(10)

from time import sleep as sl
sl(10)


