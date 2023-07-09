f = open("./text/05.txt", "r", encoding="utf-8")
copy = open("./text/05_拷贝.txt.bak", "w", encoding="utf-8")

for line in f:
    # print(line)
    if "测试" in line:
        continue
    copy.write(line)
    """
    line = line.strip()  # 去除首位空格,及换行符
    if line.split(",")[4] == "测试":
        continue

    copy.write(line)
    copy.write("\n")
    """

f, copy.close()
