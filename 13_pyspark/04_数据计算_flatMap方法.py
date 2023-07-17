from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "D:\Software\python\python3.11.4\python.exe"

conf = SparkConf().setMaster('local[*]').setAppName('text_spark')
sc = SparkContext(conf=conf)

# 准备一个 RDD
rdd = sc.parallelize(["itheima itcast python", "hello world", "itheima python"])

# 将 RDD中单词一个个 取出来  flatMap 最后会解除嵌套
rdd1 = rdd.flatMap(lambda x: x.split(' '))
print(rdd1.collect())

sc.stop()
