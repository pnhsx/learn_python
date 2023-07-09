"""
    函数(方法) 进行类型注解
"""


# 对形参进行注解
def add(x: int, y: int):
    return x + y


add(1, 3)


# 对返回值进行注解
def func(data: list) -> list:
    return data


func(123)
print(func(123))
func([1, 2])
