"""
json 数据 和python 数据相互转换
"""
import json

# 列表转 json
list1 = [{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 19}, {"name": "赵小虎", "age": 17}]
json_str = json.dumps(list1, ensure_ascii=False)  # 是否展示中文
print(json_str)
print(type(json_str))

# 字典转 json
dict1 = {"name": "周杰伦", "addr": "台北"}
json_str1 = json.dumps(dict1, ensure_ascii=False)
print(json_str1)
print(type(json_str1))

# json 字符串转 python
str1 = '[{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 19}, {"name": "赵小虎", "age": 17}]'
list2 = json.loads(str1)
print(list2)
print(type(list2))

str2 = '{"name": "周杰伦", "addr": "台北"}'
dict2 = json.loads(str2)
print(dict2)
print(type(dict2))
