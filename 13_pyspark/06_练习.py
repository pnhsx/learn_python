# 1.构建执行环境入口对象

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:\Software\python\python3.11.4\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("flatmap_example")
sc = SparkContext(conf=conf)

# 2.读取数据文件
rdd = sc.textFile("./06__练习.txt")

# 3.取出全部单词
word_rdd = rdd.flatMap(lambda x: x.split(' '))

# 4.将所有单词都转换成二元元组，单词为key，value 设置为1
word_rdd_one = word_rdd.map(lambda x: (x, 1))
# 5.分组并求和
result = word_rdd_one.reduceByKey(lambda a, b: a + b)
print(result.collect())

sc.stop()
