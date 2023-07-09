def text_func(compute):
    result = compute(1, 2)
    print(f"compute类型:{type(compute)}")
    print(f"计算结果:{result}")


def compute(x, y):
    return x + y


text_func(compute)