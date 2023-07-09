import random

balance = 10000

for i in range(1, 21):
    if balance == 0:
        print("余额不足,下个月再来")
        break

    score = random.randint(0, 10)
    if score < 5:
        print(f"员工{i}绩效分{score},低于5,不发工资")
    else:
        balance -= 1000
        print(f"员工{i},发放工资1000,账户余额{balance}")
