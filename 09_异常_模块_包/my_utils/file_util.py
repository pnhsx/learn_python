def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, "r", encoding="utf-8")
        content = f.read()
        print(content)
    except Exception as e:
        print(f"出现错误,错误信息:{e}")
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="utf-8")
    f.write(data)
    f.write("\n")
    f.close()


if __name__ == '__main__':
    print_file_info("../text/07.txt")
    append_to_file("../text/07.txt", "学it,来黑马")
