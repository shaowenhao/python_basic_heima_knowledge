# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 12/7/2022 3:40 PM
# 文件名称: zidian1.PY

dictionary1 = {'qq':'376031993','password':'1234qwer'}
print(dictionary1)

# 创建列表
name = ['abc','def']
age = [10,20]
dictionary2 = dict(zip(name,age))
print(dictionary2)

#
dictionary3 = dict( shaowenhao = 'ryan')
print(dictionary3)

print(dictionary1.get('qq'))

for item in dictionary1.items():
    print(item)

dictionary4 = dict((('ag','chengdu game club'),('gk','foshan game club')))
print(dictionary4)
dictionary4['estar'] = 'wuhan game club'
print(dictionary4)


#字典推导式
import random

randomdict ={i:random.randint(10,100) for i in range(1,5)}
print(randomdict)

