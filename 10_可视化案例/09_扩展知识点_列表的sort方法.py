"""
    扩展   列表 sort方法
"""

my_list = [["a", 16], ["b", 6], ["c", 64]]

my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)
