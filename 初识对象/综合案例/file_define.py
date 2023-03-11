# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 3/1/2023 9:48 AM
# 文件名称: file_define.PY

'''
和文件相关的类定义

先定义一个抽象类来做顶层设计 确定有哪些共轭能需要实现
'''
import json

from 初识对象.综合案例.data_define import Record


class FileReader:

    def read_data(self) -> list[Record]:
        '''读取文件的数据 读到的每条数据转换为Record对象 将他们封装到list内返回'''
        pass

# 文本文件读取
class TextFileReader(FileReader):
    def __init__(self,path):
        self.path = path              # 定义成员变量 记录文件的路径
    # 实现抽象方法
    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="UTF-8")

        record_list:list[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)

        f.close()
        return record_list


#JSON文件读取
class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path = path              # 定义成员变量 记录文件的路径
    # 实现抽象方法
    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="UTF-8")

        record_list:list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict['date'],data_dict['order_id'],data_dict['money'],data_dict['province'])
            record_list.append(record)

        f.close()
        return record_list
if __name__ == '__main__':
    textFileReader = TextFileReader("D:/1月份数据")
    list1 = textFileReader.read_data()

    for l in list1:
        print(l)
    #自测检查结果 打印的默认是Record对象 这里想到魔法方法
