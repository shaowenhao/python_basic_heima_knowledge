# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/27/2023 10:26 AM
# 文件名称: json.PY

"""
演示json数据和python字典的相互转换
"""

import json

#准备列表， 列表内每一个元素都是字典，将其转换为JSON
data = [{"name":"邵文浩","age":10},{"name":"b","age":11},{"name":"c","age":12}]

json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)


# 准备字典 将字典转化为JSON
d = {"name":"ab","addr":"xx"}
json_str = json.dumps(d)
print(json_str)

# 将JSON字符串转为Python的数据类型
s = '[{"name": "邵文浩", "age": 10}, {"name": "b", "age": 11}, {"name": "c", "age": 12}]'
l = json.loads(s)
print(type(l))
print(l)

s = '{"name": "ab", "addr": "xx"}'
d = json.loads(s)
print(type(d))
print(d)