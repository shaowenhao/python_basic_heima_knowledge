# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/24/2023 9:02 AM
# 文件名称: 模块带方法调用不想import的时候自动执行.PY

def fun1(a,b):
    print(a+b)

# 方法main里 可以测试模块的方法 不会再被import的时候执行 fun1
if __name__ == '__main__':
    fun1(1,2)
