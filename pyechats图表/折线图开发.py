# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/27/2023 3:47 PM
# 文件名称: 折线图开发.PY

import json
# 处理数据

f = open("D:/美国.txt","r",encoding="UTF-8")
us_data = f.read()

# 去掉不合JSON规范的开头
us_data = us_data.replace("jsonxxxxxx","")

# 去掉不合规范的结尾 删掉2个符号
us_data = us_data[:-2]

#Json转python字典
us_dict = json.loads(us_data)
print(type(us_dict))
print(us_dict)

trend_data = us_dict["data"][0]['trend']

x_data = trend_data['updateDate'][:314]

y_data = trend_data['list'][0]['data']

#生成图表

#关闭文件



