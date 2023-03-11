# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/23/2023 6:37 PM
# 文件名称: 异常的传递.PY

def fun1():
    print("func1 执行")
    num = 1 / 0
    print("func1 结束执行")

def fun2():
    print("func2 执行")
    fun1()
    print("func2 结束执行")

def main():
    try:
            fun2()
    except Exception as e:
        print(f"出现异常，异常信息是{e}")
main()
