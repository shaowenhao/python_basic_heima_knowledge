# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/23/2023 4:21 PM
# 文件名称: 异常处理.PY

'''
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
'''


#基本捕获语法
try:
    f = open("d:/123456789.txt","r",encoding="UTF-8")
except:
    print("出现异常 文件不存在")
    f = open("d:/123456789.txt","w",encoding="UTF-8")
f.close()

#捕获指定的异常
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)


# 捕获多个异常
try:
 1 / 0
except(NameError,ZeroDivisionError) as e:
    print("出现了变量未定义异常或者除0异常")


#捕获所有异常 基本捕获不写具体的异常其实也是所有捕获
try:
    1 / 0
except Exception as e:
    print("出现异常")


#异常else
try:
    print("hello")
except Exception as e:
    print("出现异常")
else:
    print("没有异常,好高兴")

#异常的finally
# 无论是否异常都需要执行的代码 如 关闭文件
try:
    f = open('test123.txt','r')
except Exception as e:
    f = open('test123.txt','w')
else:
    print("没有异常~~")
finally:
    f.close()
