class Student:
    name = None

    def say_hi(self, msg):
        print(f"大家好,我是{self.name},{msg}")


stu1 = Student()
stu1.name = "周杰伦"
stu1.say_hi("哎呦,不错呦")

stu2 = Student()
stu2.name = "林俊杰"
stu2.say_hi("小伙子,我看好你")
