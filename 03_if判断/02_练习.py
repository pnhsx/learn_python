import random

num = random.randint(1, 10)
guess_num = int(input("猜数1-10:"))
print(num)

if guess_num == num:
    print("对了")
else:
    if guess_num > num:
        print("大了")
    else:
        print("小了")

    guess_num = int(input("再猜:"))

    if guess_num == num:
        print("对了")
    else:
        if guess_num > num:
            print("大了")
        else:
            print("小了")

            guess_num = int(input("再猜:"))

            if guess_num == num:
                print("对了")
            else:
                print("三次机会用完了,没猜中")
