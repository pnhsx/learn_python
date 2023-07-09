"""
list1 = []
num = 0
with open("./data/02.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        str_list = line.split(' ')
        list1.extend(str_list)
    print(list1)

for element in list1:
    list1[list1.index(element)] = element.replace("\n", "")

num = list1.count("itheima")

print(list1)
print(f"itheima出现{num}次")
"""
f = open("./text/02.txt", "r", encoding="utf-8")

content = f.read()
count = content.count("itheima")
print(count)
