# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/27/2023 8:20 PM
# 文件名称: 类和对象.PY

import  winsound
class Clock:
    id = None
    price = None

    def ring(self):
        winsound.Beep(1000,1000)

clock1 =  Clock()
clock1.ring()

