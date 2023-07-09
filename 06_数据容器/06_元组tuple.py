tup1 = (1, "itheima", True)
tup2 = ("hello")
tup3 = ("hello",)
tup4 = ((1, 2, 3), (4, 5, 6))

print(f"tup1的内容是{tup1}")
print(f"tup2的类型是:{type(tup2)},内容是:{tup2}")
print(f"tup3的类型是:{type(tup3)},内容是:{tup3}")

num = tup4[1][2]
print(f"从嵌套元组中取出数据{num}")

tup5 = ("itheima", "黑马程序员", "传智播客", "itcast", "黑马程序员", "黑马程序员")
index = tup5.index("黑马程序员")
print(f"在元组中查找元素,下标为{index}")
count = tup5.count("黑马程序员")
print(f"在元组中统计元素个数,为{count}")
len = len(tup5)
print(f"元组长度为{len}个")

# tup5[0] = "python"
# tup5 = (1,)
tup6 = (1, 2, ["itheima", "itcast"])
tup6[2][0] = "黑马程序员"
tup6[2][1] = "python"
print(f"tup6的内容是:{tup6}")
