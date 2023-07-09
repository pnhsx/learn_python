def str_reverse(e):
    """
    将字符串完成反转操作
    :param e: 将要反转的字符串
    :return: 反转后的字符串
    """
    return e[::-1]


def substr(s, x, y):
    return s[x: y]


if __name__ == '__main__':
    print(str_reverse("hello"))
    print(substr("黑马程序员", 1, 4))
