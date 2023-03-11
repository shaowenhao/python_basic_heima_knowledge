# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 3/10/2023 4:22 PM
# 文件名称: 元字符匹配.PY

import  re

s = "abc123def456hello"

result = re.findall(r'\d',s)
print(result)
print(type(result))


r = '^[0-9a-zA-Z]{6,10}$'
s = '1234567'
print(re.findall(r, s))
