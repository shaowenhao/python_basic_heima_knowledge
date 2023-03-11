# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 3/10/2023 1:41 PM
# 文件名称: 工厂模式.PY
'''
使用工厂类创建对象的有点

大批量创建对象的时候统一的入口 易于维护
当发生修改 仅修改工厂类的创建方法
符合现实世界的模式 由工厂来制作产品 （对象）
'''

class Person:
    pass

class Worker(Person):
    pass

class Student(Person):
    pass
class Teacher(Person):
    pass

class PersonFactory:
    def get_person(self,p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        else:
            return  Teacher()

pf = PersonFactory()
worker = pf.get_person('w')

stu = pf .get_person('s')
teacher = pf.get_person('t')