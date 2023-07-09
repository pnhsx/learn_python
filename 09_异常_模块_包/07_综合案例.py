import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("黑马程序员"))
print(my_utils.str_util.substr("itheima", 1, 3))

file_util.print_file_info("./text/07.txt")
file_util.append_to_file("./text/07.txt", "月薪过万")
