# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/28/2023 8:00 PM
# 文件名称: 变量注解.PY

#基础数据类型注解

# 语法  变量：类型
import random

var1: int = 10
var2: str = "abc"

print(type(var1))
print(type(var2))


#类对象类型注解：
class Student:
    pass
stu: Student = Student()

#基础容器注解
my_list: list = [1,2,3]
#详细容器类型注解
my_list: list[int] = [1,2,3]

my_tuple: tuple[int,str,bool] = (1,"aaa",False)

my_dict: dict[str,int] = {"A":111}

# 除了使用变量:类型 这种语法做注解外 也可以在注释中进行类型注解


var_1 = random.randint(1,10) # type: int
print(var_1)

#类型注解的限制
