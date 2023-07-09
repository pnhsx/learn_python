"""
    变量的类型注解
"""
import json
import random

# # 基础数据类型
# var_1: int = 10
# var_2: str = "itheima"
# var_3: bool = True
#
#
# # 类对象类型
# class Student:
#     pass
#
#
# stu: Student = Student()

# 容器类型
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"itheima": 666}

# 容器类型详细注解
my_list1: list[int] = [2]
my_tuple1: tuple[int, str, bool] = (1, "itheima", True)
my_dict1: dict[str, int] = {"itheima": 1}

# 注释中类型注解
var_1 = random.randint(1, 10)  # type: int
var_2 = json.loads('{"name": "张三"}')  # type: dict[str,str]


def func():
    return 10


var_3 = func()  # type: int

# 类型注解限制
var_4: int = "itheima"
var_5: str = 123
