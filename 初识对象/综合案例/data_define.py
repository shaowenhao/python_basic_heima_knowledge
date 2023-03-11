# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 3/1/2023 9:36 AM
# 文件名称: data_define.PY

'''
1. 数据定义的类
'''

class Record:
# 思考更合适的定义方式 构造方法
#     date = None
#     order_id = None
#     money = None
#     province = None
    def __init__(self,date,order_id,money,province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

# 打印内容的时候 不在是对象的内存地址 而是下面的内容
    def __str__(self):
         return f"{self.date},{self.order_id},{self.money},{self.province}"