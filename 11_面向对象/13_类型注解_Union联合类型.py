"""
    Union 联合类型注解
"""

# 使用Union 类型,需要先导包
from typing import Union

my_list: list[Union[int, str]] = [1, 2, "itheima"]


def func(data: Union[int, str]) -> Union[int, str]:
    pass


func()
