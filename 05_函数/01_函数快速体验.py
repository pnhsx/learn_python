str1 = "itheima"
str2 = "itcast"
str3 = "python"

print(len(str1))

count = 0
for i in str1:
    count += 1

print(f"{str1}长为{count}个字符")


def my_len(data):
    count = 0
    for i in data:
        count += 1

    print(f"{data}长为{count}个字符")


my_len(str1)
my_len(str2)
my_len(str3)
