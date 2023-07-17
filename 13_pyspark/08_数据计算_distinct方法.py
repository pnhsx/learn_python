"""
    distinct
    去重
"""


from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "D:\Software\python\python3.11.4\python.exe"

conf = SparkConf().setMaster('local[*]').setAppName('text_spark')

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 8, 9, 3, 4, 6, 8])

rdd2 = rdd.distinct()

print(rdd2.collect())

sc.stop()
