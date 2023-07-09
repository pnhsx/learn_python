my_dict = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}

# 新增元素
my_dict["张信哲"] = 66
print(f"新增元素,结果:{my_dict}")

# 更新元素
my_dict["周杰伦"] = 33
print(f"更新元素,结果:{my_dict}")

# 删除元素
score = my_dict.pop("周杰伦")
print(f"字典移除了一个元素,结果:{my_dict},移除的元素:{score}")

# 获取全部 key
my_dict = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}
keys = my_dict.keys()
print(f"字典全部key:{keys},类型:{type(keys)}")
for key in keys:
    print(f"字典的key:{key}")
    print(f"字典的value:{my_dict[key]}")

for key in my_dict:
    print(f"--字典的key:{key}")
    print(f"--字典的value:{my_dict[key]}")

num = len(my_dict)
print(f"字典长度:{num}")
