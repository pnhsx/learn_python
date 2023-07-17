"""
    filter
    过滤

"""

from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "D:\Software\python\python3.11.4\python.exe"

conf = SparkConf().setMaster('local[*]').setAppName('text_spark')

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])
result = rdd.filter(lambda a: a % 2 == 0)

print(result.collect())

sc.stop()
