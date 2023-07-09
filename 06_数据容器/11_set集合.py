my_set = {"传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima"}
my_set_empty = set()

print(f"my_set:{my_set}类型:{type(my_set)}")
print(f"my_set:{my_set_empty}类型:{type(my_set_empty)}")

my_set.add("Python")
print(f"添加元素后:{my_set}")

my_set.remove("黑马程序员")
print(f"删除元素后:{my_set}")

element = my_set.pop()
print(f"随机取出的元素:{element},取后{my_set}")

my_set.clear()
print(f"清空元素:{my_set}")

# 取 2集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}

set3 = set1.difference(set2)
print(f"取出差集后的结果:{set3}")
print(f"取差集后set1:{set1}")
print(f"取差集后set2:{set2}")

# 消除 2个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(f"消除差集后set1:{set1}")
print(f"消除差集后set2:{set2}")

# 2集合合并
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"集合合并结果{set3}")
print(f"合并后set1:{set1}")
print(f"合并后set2:{set2}")

set1 = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5}
num = len(set1)
print(f"set1有{num}个元素")

# 集合遍历, 集合没有下标,不可以用while遍历

set1 = {1, 2, 3, 4, 5}
for element in set1:
    print(f"集合的元素有:{element}")
