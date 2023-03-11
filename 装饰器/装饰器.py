# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 3/10/2023 11:28 AM
# 文件名称: 装饰器.PY

'''
装饰器 其实也是一种闭包
其功能就是在不破坏目标函数原有的代码和功能的前提下
为目标函数增加新功能
'''

# 装饰器的一般写法
# def outer(func):
#     def inner():
#         print("我睡觉了了")
#         func()
#         print("我起床了")
#     return inner
#
#
# def sleep():
#     import random
#     import time
#     print("睡眠中....")
#     time.sleep(random.randint(1,5))
#
# fn = outer(sleep)
# fn()

# 语法糖写法
def outer(func):
    def inner():
        print("我睡觉了了")
        func()
        print("我起床了")
    return inner

@outer
def sleep():
    import random
    import time
    print("睡眠中....")
    time.sleep(random.randint(1,5))

sleep()