"""
获取 PySpark 的执行环境入库对象: SparkContext
并通过 SparkContext 对象获取当前 PySpark的版本
"""

from pyspark import SparkConf, SparkContext

# 创建 SparkConf 类对象
conf = SparkConf().setMaster("local[*]").setAppName("text_spark_app")
# 基于 SparkConf 类对象创建 SparkContext 对象
sc = SparkContext(conf=conf)

print(sc.version)

sc.stop()
