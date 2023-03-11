# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/28/2023 6:27 PM
# 文件名称: 单继承.PY

class Phone:
    IMEI = None
    producer = None

    def call_by_4g(self):
        print("4g通话")

class Phone2023(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("5g通话")

phone =  Phone2023()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()



# 多继承 (父类1， 父类2...)


#只想继承 不想添加新的方法或变量 可以直接用 pass

# 对调用同名的变量 遵循谁先继承的优先级

