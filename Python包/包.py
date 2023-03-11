# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/24/2023 9:22 AM
# 文件名称: 包.PY


'''
从物理上看 包就是一个文件夹 在该文件夹下包含一个__init__.py文件
它包含多个模块文件
'''

#导入自定义的包中的模块并使用
# import Python包.my_module1
# import Python包.my_module2
#
# Python包.my_module1.fun1()
# Python包.my_module2.fun2()

#方式二
# from Python包 import my_module1
# from Python包 import my_module2
# my_module1.fun1()
# my_module2.fun2()

#方式三
# from  Python包.my_module1 import fun1
# from  Python包.my_module2 import fun2
# fun1()
# fun2()

# 方式四 只对星生效 因为__init__.py文件 all只定义了 module1
from Python包 import *
my_module1.fun1()




