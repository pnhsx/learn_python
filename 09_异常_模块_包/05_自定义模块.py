# # 导入自定义模块
# import my_module1
#
# my_module1.data(1, 2)

# # 导入不同模块同名共功能
# from my_module1 import data
# from my_module2 import data
# data(1,2)

# __main__ 变量
from my_module1 import text

# __all__ 变量
from my_module1 import *

text_a(1, 2)
text_b(1, 2)
