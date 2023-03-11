# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/27/2023 8:28 PM
# 文件名称: 构造方法.PY

'''
Python 类可以使用： __init__() 方法 称之为构造方法
1. 在创建类对象的时候  会自动执行
2. 在创建类对象的时候 将传入的参数自动传递给__init__方法使用
'''

class Student:
    name =  None
    age = None
    tel = None

    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建一个类对象")

stu = Student("shaowenhao",35,"18611640282")
print(stu.name)
print(stu.age)
print(stu.tel)