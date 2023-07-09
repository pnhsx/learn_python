"""
    其他内置方法
"""


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__ 魔术方法
    def __str__(self):
        return f"Student类对象,name:{self.name},age:{self.age}"

    # __lt__ 魔术方法
    def __lt__(self, other):
        return self.age < other.age

    # __le__ 魔术方法
    def __le__(self, other):
        return self.age <= other.age

    # __eq__ 魔术方法
    def __eq__(self, other):
        return self.age == other.age


# stu = Student("周杰伦", 19)
# print(stu)
# print(str(stu))

stu1 = Student("周杰伦", 29)
stu2 = Student("周杰伦", 19)
print(stu1 > stu2)
print(stu1 < stu2)
print(stu1 >= stu2)
print(stu1 <= stu2)
print(stu1 == stu2)
