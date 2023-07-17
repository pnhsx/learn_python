from pyspark import SparkConf, SparkContext
import os

# pyspark 找不到 python解释器  设置python解释器路径
os.environ["PYSPARK_PYTHON"] = "D:\Software\python\python3.11.4\python.exe"

conf = SparkConf().setMaster('local[*]').setAppName('text_spark')

sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])

# 通过 map方法将全部数乘以10
# (T) -> U
# def func(data):
#     return data * 10
#
#
# rdd1 = rdd.map(func)

# 匿名函数   ////   链式调用
rdd1 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)

print(rdd1.collect())

sc.stop()
