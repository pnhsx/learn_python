# 位置

# 关键字

# 缺省(默认值)

# 不定长 位置不定长  *
def user_info(*args):
    print(f"args的类型是{type(args)},内容是:{args}")


user_info(1, "hello", True)


# 不定长 关键字不定长 **
def user_info(**kwargs):
    print(f"args的类型是{type(kwargs)},内容是:{kwargs}")


user_info(name="小明", age=18, gender="男")
