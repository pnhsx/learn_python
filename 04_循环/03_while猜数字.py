import random

num = random.randint(0, 100)
i = 1
guess = int(input("猜数字1-100:"))

while guess != num:
    if guess > num:
        print("大了")
    else:
        print("小了")

    guess = int(input("再猜猜看:"))
    i += 1

print(f"答对了,答案是{num},你猜了{i}次")
