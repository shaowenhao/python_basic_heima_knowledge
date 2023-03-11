# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 3/1/2023 9:08 AM
# 文件名称: 多态.PY

'''
演示 多态以及 抽象类（接口）的使用

Animal的写法 叫 抽象类，也可以称为接口
抽象类：含有抽象方法的类称之为抽象类
抽象方法：方法体是空实现的 pass 称之为抽象方法
'''

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal:Animal):
    ''' 制造噪音 需要传入Animal对象'''
    animal.speak()

"""演示多态  使用2个子类对象来调用"""
dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)