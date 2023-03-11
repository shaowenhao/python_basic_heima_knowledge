# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/17/2023 10:45 AM
# 文件名称: 函数多种传参方式.PY

'''
位置参数    据参数定义的参数位置来传参
关键字参数   函数调用时，通过 键=值 形式传递参数
缺省参数 也叫默认参数 调用函数时不可传入该默认参数值 （位置参数 必须在默认参数前面）
不定长参数
'''


def user_info(name,age,gender):
    print(f"你的名字是{name},年龄是{age},性别是{gender}")

#关键字传参
user_info(name="a",age=10,gender="男")

#可以不按固定顺序
user_info(age=10,name="c",gender="男")

#可以和位置参数混用，位置参数必须在前
user_info("b",gender="男",age=10)



# 缺省参数(默认值) 默认值在最后
def user_info(name, age, gender='男'):
    print(f"name:{name},age{age},gender:{gender}")

user_info("u1",20)
user_info("u2",30,'女')


# 不定长参数

# 1. 位置传递 *args 穿进去的所有参数都会被args变量收集，根据传进参数的位置并为一个元组
# 2.关键字传递 **kwargs 参数是 键=值 所有的键值对被kwargs接受，组成字典

def user_info(*args):
    print(f"{type(args)},{args}")
user_info(1,2,3,'xiao')


def user_info(**kwargs):
    print(f"{type(kwargs)},{kwargs}")
    print(f"{type(kwargs)},{kwargs},{kwargs['name']}")
user_info(name='abc',age=10)