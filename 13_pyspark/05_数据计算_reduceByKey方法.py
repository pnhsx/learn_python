from pyspark import SparkConf, SparkContext
import os

# pyspark 找不到 python解释器  设置python解释器路径
os.environ["PYSPARK_PYTHON"] = "D:\Software\python\python3.11.4\python.exe"

conf = SparkConf().setMaster('local[*]').setAppName('text_spark')

sc = SparkContext(conf=conf)

rdd = sc.parallelize([("男", 83), ("女", 89), ("女", 78), ("男", 74)])

rdd1 = rdd.reduceByKey(lambda a, b: a + b)
print(rdd1.collect())

sc.stop()
