# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/27/2023 5:35 PM
# 文件名称: 成员方法.PY

'''
在类中定义成员方法和定义函数基本一致，有细微的区别

def 方法名(self,形参1,....形参N)
    方法体
self关键字 是成员方法 定义的时候 必须写的
1. 它用来表示类对象自身的意思
2，放我们使用类对象调用方法，self会自动被python传入
3. 在方法内部 想要访问类的成员变量 必须使用 self

self关键字 尽管在参数列表中 但是传参的时候可以忽略它
'''

class Student:
    name = None

    def say_hi(self):
        print(f"大家好 我是{self.name}")


    def say_hi2(self,msg):
        print(f"大家好 我是{self.name},{msg}")

stu = Student()
stu.name = "ryan"
stu.say_hi()



