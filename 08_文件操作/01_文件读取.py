# f = open("./00_测试.txt", "r", encoding='utf-8')

# print(f"读取10个字节的结果:\n{f.read(10)}")
# print(f"全部读取的结果:\n{f.read()}")
print("------------------------------------------")

# lines = f.readlines()
# print(f"lines内容:{lines}")


# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
#
# print(f"第一行内容:{line1}")
# print(f"第二行内容:{line2}")
# print(f"第三行内容:{line3}")

# for line in f:
#     print(f"每一行内容:{line}")

# f.close()

with open("./00_测试.txt", "r", encoding='utf-8') as f:
    for line in f:
        print(f"每一行数据:{line}")
