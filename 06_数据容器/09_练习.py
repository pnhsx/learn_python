str1 = "itheima itcast boxuegu"

num = str1.count("it")
print(f"字符串{str1}中有{num}个it字符")
str2 = str1.replace(" ", "|")
print(f"str1:{str1},替换后str2:{str2}")
list1 = str2.split("|")
print(f"list1:{list1}")
