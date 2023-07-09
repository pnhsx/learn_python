def list_while_func():
    """
    while 循环列表
    :return: None
    """
    index = 0
    list1 = ['itheima', 'itcast', 'python']
    while index < len(list1):
        element = list1[index]
        print(f"列表元素:{element}")
        index += 1


list_while_func()


def list_for_func():
    """
    for 循环列表
    :return: None
    """
    list2 = [1, 2, 3, 4]
    for element in list2:
        print(f"列表元素:{element}")


list_for_func()
