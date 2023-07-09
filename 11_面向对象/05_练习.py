# class Student:
#
#     def __init__(self, name, age, add):
#         self.name = name
#         self.age = age
#         self.add = add
#
#
# for i in range(0, 10):
#     print(f"当前录入第{i + 1}位学生信息, 总共需要录入10位学生信息")
#     name = input("请输入学生姓名:")
#     age = input("请输入学生年龄:")
#     add = input("请输入学生地址:")
#     stu = Student(name, age, add)
#     print(f"学生{i + 1}信息录入完成,信息为:[学生姓名:{name},年龄:{age},地址:{add}]")


class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # def __str__(self):
    #     return f"Student(name={self.name}, age={self.age}, address={self.address})"


students = []
for i in range(10):
    print(f"当前录入第{i + 1}位学生信息, 总共需要录入10位学生信息")
    name = input("请输入学生姓名:")
    age = input("请输入学生年龄:")
    address = input("请输入学生地址:")
    stu = Student(name, age, address)
    students.append(stu)
    print(f"学生{i + 1}信息录入完成, 信息为:[学生姓名:{name}, 年龄:{age}, 地址:{address}]")
for student in students:
    print(student)
