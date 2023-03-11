# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 3/4/2023 9:29 AM
# 文件名称: 数据输入.PY

'''
RDD对象 是pyspark中数据计算的载体

如何输入数据到spark 得到RDD对象 2中方式
通过SparkContext的parallelize 将Python数据容器转换为RDD对象
或者textFile 读取文件得到RDD
'''
from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)
print(sc.version)

rdd1 = sc.parallelize([1,2,3,4,5])
rdd2 = sc.parallelize((1,2,3,4,5))
rdd3 = sc.parallelize("abcdefg")

# 查看RDD里有什么内容
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())


# 通过textFile方法 获取文件数据加载到spark内 称为RDD对象
rdd4 = sc.textFile("文件路径")
print(rdd4.collect())

sc.stop()