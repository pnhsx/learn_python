"""
    python 闭包
"""


# # 简单闭包
# def outer(logo):
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
#
# f1 = outer("黑马程序员")
# f1("python")
#
# f2 = outer("传智播客")
# f2("python")

# # 使用 nonlocal关键字修改外面函数的值
# def outer(num1):
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#
#     return inner
#
#
# fn1 = outer(10)
# fn1(10)
# fn1(10)
# fn1(10)

# 闭包实现 ATM小案例
def account_create(initial_amount=0):
    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款:+{num},余额:{initial_amount}")
        else:
            initial_amount -= num
            print(f"取款:-{num},余额:{initial_amount}")

    return atm


atm = account_create()
atm(1000)
atm(200, False)
