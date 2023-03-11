# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 12/2/2022 2:03 PM
# 文件名称: liebiao1.PY

#删除

# ['a', 'c']
# 1

team = ['a', 'b','c']
value = 'b'
if team.count(value) > 0:
    team.remove(value)
print(team)

position = team.index('c')
print(position)

result = [1,2,3,4,5]
total = sum(result)
print(total)

# 1.使用列表对象的sort()方法 会改变原列表中的元素顺序
# 2.使用内置的sorted()函数实现 原列表的元素顺序不变


#列表推导式

import random

randomnumber =[random.randint(10,100) for i in range(10)]
print(randomnumber)

price = [10,20,30]
newprice = [ int(x * 0.5) for x in price]
print(newprice)


price = [100,200,300]
sale = [ x for x in price if x < 300]
print(sale)

