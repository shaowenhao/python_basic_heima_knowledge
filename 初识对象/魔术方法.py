# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/28/2023 2:53 PM
# 文件名称: 魔术方法.PY

'''
内置类的方法 各有特殊的功能 称之为 魔术方法
'''

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
#__str__魔术方法
    def __str__(self):
        return f"Student对象，name是{self.name},age是{self.age}"

# __lt__魔术方法
    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("shaowenhao",35)
print(stu1)  #<__main__.Student object at 0x0000026B1C039F70>
stu2 = Student("duxiaodan",35)
print(stu1 < stu2)

print(stu1 == stu2)

