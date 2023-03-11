# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 12/7/2022 4:25 PM
# 文件名称: jihe.PY

set1 = {3,1,1,3,4}
print(set1)

#set()函数创建
set2 = set([1,2,3,4,5])
print(set2)

set3 = set((1,2,3,4,5))
print(set3)

set4 = set("abcde")
print(set4)

set5 = set(" ")
print(set5)

set4.add('f')
print(set4)

set4.remove('a')
print(set4)

set4.pop()
print(set4)
set4.clear()
print(set4)