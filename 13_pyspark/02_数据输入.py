"""
pyspark 代码加载数据,即数据输入
"""

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local[*]').setAppName('text_spark')

sc = SparkContext(conf=conf)

# # 通过 parallelize 方法将 python 对象加载到Spark 内,成为 RDD对象
# rdd1 = sc.parallelize([1, 2, 3, 4, 5])
# rdd2 = sc.parallelize((1, 2, 3, 4, 5))
# rdd3 = sc.parallelize('abcde')
# rdd4 = sc.parallelize({1, 2, 3, 4, 5})
# rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})
#
# # 如果要查看 RDD 里面什么内容,需要使用collect()方法
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())

# 通过 textFile方法,读取文件数据加载到Spark内, 成为RDD 对象
rdd = sc.textFile("./02__text.txt")
print(rdd.collect())

sc.stop()
