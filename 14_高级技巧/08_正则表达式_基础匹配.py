"""
     Python 正则表达式 re模块的3个基础匹配方法
"""
import re

str1 = "1python itheima python python"
# match 从头匹配

res = re.match('python', str1)
print(res)
# print(res.span())
# print(res.group())

# search 搜索匹配
res = re.search('python', str1)
print(res)

# findall 搜索全部匹配
res = re.findall('python', str1)
print(res)
