# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 3/1/2023 9:34 AM
# 文件名称: main.PY

'''
1. 设计一个类 可以完成数据的封装
2. 设计一个抽象类 定义文件读取的相关功能 并使用子类实现具体功能
3. 读取文件 生产数据对象
4. 进行数据的逻辑计算
5. 通过PyEcharts进行图绘
'''

from file_define import FileReader,TextFileReader,JsonFileReader
from data_define import Record

text_file_reader = TextFileReader("D:/1月份.txt")
json_file_reader = JsonFileReader("D:/2月份数据.json")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

#将2个月的数据合并为1个list来存储
all_data: list[Record] = jan_data + feb_data

#开始进行数据计算 考虑用字典
#{"2011-01-01":1234,xxxxxx}

data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # 当前日期已经有记录了 所以和老记录做累加即可
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# 至此统计出每一天的销售额 用字典保存下来

