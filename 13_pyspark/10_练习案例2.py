from pyspark import SparkConf, SparkContext
import os
import json

os.environ['PYSPARK_PYTHON'] = "D:\Software\python\python3.11.4\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("spark_test")
sc = SparkContext(conf=conf)

# TODO 需求1： 城市销售额排名
# 1.1读取文件获得rdd
file_rdd = sc.textFile("./orders.txt")
# 1.2取出一个个JSON字符串
json_rdd = file_rdd.flatMap(lambda x: x.split('|'))
# 1.3将一个个JSON字符串转换为字典
dict_rdd = json_rdd.map(lambda x: json.loads(x))
# 1.4取出城市和销售额数据
city_rdd = dict_rdd.map(lambda x: (x["areaName"], int(x["money"])))
# 1.5按城市分组,按销售额聚合
res_rdd = city_rdd.reduceByKey(lambda a, b: a + b)
# 1.6按销售额聚合结果进行排序
res_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)

print(res_rdd.collect())

# TODO 需求2： 全部城市中有哪些商品在售卖
# 取出全部商品类别
commodity_rdd = dict_rdd.map(lambda x: x["category"])
# 对全部商品类别进行去重
res_com_rdd = commodity_rdd.distinct()
print(res_com_rdd.collect())

# TODO 需求3： 北京市有哪些商品在售卖
# 过滤北京市的数据
designate_bj_rdd = dict_rdd.filter(lambda x: x["areaName"] == "北京")
commodity_bj_rdd = designate_bj_rdd.map(lambda x: x["category"]).distinct()
print(commodity_bj_rdd.collect())

sc.stop()
