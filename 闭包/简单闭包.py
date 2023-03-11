# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 3/9/2023 7:28 PM
# 文件名称: 简单闭包.PY



'''
优点
无需定义全局变量即可实现通过函数  持续访问 修改某个值
闭包使用的变量的在函数内 难以被错误调用修改


缺点内存空间一直被占用 不释放
'''
# 目标：既想依赖外部全局变量，又不想这个变量能被修改  所以闭包

# 目的是内部函数可以使用外部变量
def outer(logo):

    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")
    return inner

fn1 = outer("siemens")
print(f"{type(fn1)}")
fn1("sdl")
fn1("T six")


#需要使用nonlocal关键字修饰外部函数的变量 才可以在内部函数修改它
def outer(num1):

    def inner(num2):
        nonlocal  num1
        num1 += num2
        print(num1)
    return inner

fn = outer(10)
fn(10)


#闭包实现ATM小案例
def account_create(initial_amount=0):

     def atm(num,deposite=True):
         nonlocal initial_amount
         if deposite:
             initial_amount += num
             print(f"存款:+{num},账户余额：{initial_amount}")
         else:
             initial_amount -= num
             print(f"取款:-{num},账户余额：{initial_amount}")
     return atm

atm = account_create()
atm(100)
atm(200)
atm(100,deposite=False)