# 捕获异常
try:
    f = open("./data.txt", 'r', encoding="utf-8")
except:
    print("出现异常,文件不存在")

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print("出现变量未定义异常")
    print(e)

# 捕获多个异常
try:
    1 / 0
except(NameError, ZeroDivisionError) as e:
    print('出现了变量未定义异常或者除以0异常')
    print(e)

# 捕获所有异常
try:
    # f = open("./data.txt", 'r', encoding="utf-8")
    print('hello')
except Exception as e:
    print("出现异常了")
    print(e)
else:
    print("未出现异常")
finally:
    print("有没有异常都执行")
