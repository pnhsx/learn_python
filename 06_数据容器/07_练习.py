stu = ("周杰伦", 11, ['football', 'music'])

num = stu.index(11)
print(num)
name = stu[0]
print(name)
del stu[2][0]
print(stu)
stu[2].append("coding")
print(stu)
