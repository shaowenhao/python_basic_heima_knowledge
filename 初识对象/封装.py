# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/28/2023 3:39 PM
# 文件名称: 封装.PY

'''
私有成员

定义方式简单：
1. 私有成员变量 变量名以__开头 （2个下划线）
1. 私有成员方法 方法名以__开头 （2个下划线）
'''

# 定义一个类

class Phone:
    __current_voltage = 1

    def __keep_single_core(self):
        print("让cpu单核运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5G通话开启")
        else:
            self.__keep_single_core()
            print("电量不足 无法开启5G通话")

phone = Phone()
# phone.__keep_single_core()

phone.call_by_5g()