my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5, }

# len()
print(f"元素个数:{len(my_list)}")
print(f"元素个数:{len(my_tuple)}")
print(f"元素个数:{len(my_str)}")
print(f"元素个数:{len(my_set)}")
print(f"元素个数:{len(my_dict)}")

# max()
print(f"最大元素:{max(my_list)}")
print(f"最大元素:{max(my_tuple)}")
print(f"最大元素:{max(my_str)}")
print(f"最大元素:{max(my_set)}")
print(f"最大元素:{max(my_dict)}")

# min()
print(f"最小元素:{min(my_list)}")
print(f"最小元素:{min(my_tuple)}")
print(f"最小元素:{min(my_str)}")
print(f"最小元素:{min(my_set)}")
print(f"最小元素:{min(my_dict)}")

# 容器转列表
print(f"列表转列表:{list(my_list)}")
print(f"元组转列表:{list(my_tuple)}")
print(f"字符串转列表:{list(my_str)}")
print(f"集合转列表:{list(my_set)}")
print(f"字典转列表:{list(my_dict)}")

# 转元组 字符串 集合 ...

# 容器排序
my_list = [3, 1, 2, 5, 4]
my_tuple = (3, 1, 2, 5, 4)
my_str = "ebfagcd"
my_set = {3, 1, 2, 5, 4}
my_dict = {"key3": 1, "key1": 2, "key2": 3, "key5": 4, "key4": 5, }

print(f"列表排序:{sorted(my_list)}")
print(f"元组排序:{sorted(my_tuple)}")
print(f"字符串排序:{sorted(my_str)}")
print(f"集合排序:{sorted(my_set)}")
print(f"字典排序:{sorted(my_dict)}")

# 反向排序
print(f"列表反向排序:{sorted(my_list, reverse=True)}")
print(f"元组反向排序:{sorted(my_tuple, reverse=True)}")
print(f"字符串反向排序:{sorted(my_str, reverse=True)}")
print(f"集合反向排序:{sorted(my_set, reverse=True)}")
print(f"字典反向排序:{sorted(my_dict, reverse=True)}")
