# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/28/2023 7:07 PM
# 文件名称: 继承复写_使用父类成员.PY

class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("使用5g通话")

# 定义子类 复写父类成员
class MyPhone(Phone):
    producer = "SIEMENS"

    def call_by_5g(self):
        print("开启CPU单核模式")
        # print("使用5g通话")
        # 方式1
        super().call_by_5g()
        print(f"父类的厂商是{super().producer}")


phone = MyPhone()
phone.call_by_5g()
print(phone.producer)