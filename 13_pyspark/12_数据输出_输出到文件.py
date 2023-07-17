from pyspark import SparkConf, SparkContext
import os
import json

os.environ['PYSPARK_PYTHON'] = "D:\Software\python\python3.11.4\python.exe"
os.environ['HADOOP_HOME'] = "D:\Software\hadoop\hadoop-3.3.1"

conf = SparkConf().setMaster("local[*]").setAppName("spark_test")
# 设置默认一个分区
# conf.set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)

# 设置默认分区为1 关键字和位置传参
rdd = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)

rdd2 = sc.parallelize([('hello', 2), ('spark', 7), ('python', 4)], 1)

rdd3 = sc.parallelize([[1, 2, 3], [1, 4, 2], [7, 3, 6]], 1)

# 默认有多个分区,根据 cpu核数创建
rdd.saveAsTextFile("./output")
rdd2.saveAsTextFile("./output2")
rdd3.saveAsTextFile("./output3")

sc.stop()
