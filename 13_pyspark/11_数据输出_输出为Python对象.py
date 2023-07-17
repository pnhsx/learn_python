from pyspark import SparkConf, SparkContext
import os
import json

os.environ['PYSPARK_PYTHON'] = "D:\Software\python\python3.11.4\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("spark_test")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

# collect算子,输出RDD 为list对象
rdd_list = rdd.collect()
print(rdd_list)
print(type(rdd_list))
# reduce算子,对RDD进行两两聚合
num = rdd.reduce(lambda a, b: a + b)
print(num)
# take算子, 取出RDD前 n个元素,组成 list返回
take_rdd = rdd.take(3)
print(take_rdd)
# count,统计 RDD内有多少条数据,返回为数字
num_count = rdd.count()
print(num_count)

sc.stop()
