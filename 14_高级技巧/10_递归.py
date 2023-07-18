"""
    递归
    需求:通过递归,找出一个指定文件夹内全部内容

    思路:写一个函数,列出文件夹内全部内容,如果是文件就收集到list
    如果是文件夹,就递归调用自己,再次判断

"""
import os


def test_os():
    """演示os模块的3个基础方法"""
    print(os.listdir("./test"))  # 列出路径下的内容
    print(os.path.isdir("./test"))  # 判断指定路径是不是文件夹
    print(os.path.exists("./test"))  # 判断指定路径是否存在


def txt_os(path) -> object:
    """
    从指定的文件夹中使用递归的方式, 获取全部的文件列表
    :param path: 被判断的文件夹
    :return: list 包含全部的文件,如果目录不存在或者无文件就返回一个空 list
    """
    print(f"当前判断的文件夹是{path}")
    file_list = []
    if os.path.exists(path):
        middle_list = os.listdir(path)
        for f in middle_list:
            new_path = path + '/' + f
            if os.path.isdir(new_path):
                file_list += txt_os(new_path)
            else:
                file_list.append(new_path)
    else:
        print('路径为空')
        return []

    return file_list


if __name__ == '__main__':
    # test_os()
    res = txt_os("./test")
    print(res)
