# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 3/4/2023 8:48 AM
# 文件名称: 基础准备.PY

'''
pySpark的执行环境入库对象 SparkContext
'''
from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

sc = SparkContext(conf=conf)

print(sc.version)
sc.stop()