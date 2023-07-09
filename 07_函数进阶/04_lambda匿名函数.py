def text_func(compute):
    result = compute(1, 2)
    print(f"计算结果:{result}")


text_func(lambda x, y: x + y)
