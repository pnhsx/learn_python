"""
    构造方法
"""


class Student:

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student创建了一个类对象")


stu = Student("周杰伦", 19, 18500004444)
print(stu.name)
print(stu.age)
print(stu.tel)
