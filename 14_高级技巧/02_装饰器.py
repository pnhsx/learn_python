"""
    装饰器
"""


# # 装饰器一般写法
#
# def outer(func):
#     def inner():
#         print("睡觉了")
#         func()
#         print("起床了")
#
#     return inner
#
#
# def sleep():
#     import random
#     import time
#     print("睡眠中....")
#     time.sleep(random.randint(1, 5))
#
#
# fn = outer(sleep)
# fn()

# 装饰器的快捷写法 (语法糖)
def outer(func):
    def inner():
        print("睡觉了")
        func()
        print("起床了")

    return inner


@outer
def sleep():
    import random
    import time
    print("睡眠中....")
    time.sleep(random.randint(1, 5))


sleep()
