str1 = "  123itheima and itcast231  "

value = str1[3]
print(value)
value = str1.index("and")
print(value)
new_str = str1.replace("it", "程序")
print(new_str)
list1 = str1.split(" ")
print(list1)

str2 = str1.strip()
print(str2)
str3 = str2.strip("123")
print(str3)
