# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 3/4/2023 10:18 AM
# 文件名称: map方法.PY

from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/dev_tool/Python/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)
print(sc.version)

rdd = sc.parallelize([1,2,3,4,5])

#通过map方法将全部数据都乘以10
def func(data):
    return data * 10

rdd2 = rdd.map(func)
print(rdd2.collect())