# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/27/2023 5:12 PM
# 文件名称: 设计对象.PY

class Student:
    name = None
    gender =  None
    nationality = None
    native_place = None
    age = None

stu_1 = Student()

stu_1.name = "shaowenhao"
stu_1.gender = "男"
stu_1.native_place = "中国"
stu_1.nationality = "浙江省"
stu_1.age = 35

print(stu_1.age)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)