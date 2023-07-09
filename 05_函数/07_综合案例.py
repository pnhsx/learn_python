money = 5000000
name = input("请输入姓名:")


def menu():
    print("---------------主菜单---------------------")
    print(f"{name},您好,欢迎来到黑马银行ATM,请选择操作")
    print("查询余额 \t[输入1]")
    print("存款 \t[输入2]")
    print("取款 \t[输入3]")
    print("退出 \t[输入4]")
    return input("请输入您的操作:")


def inquire(show):
    if show:
        print("---------------查询余额--------------------")
    print(f"余额:{money}")


def deposit(num):
    print("---------------存款-----------------------")
    global money
    money += num
    print(f"存款:{num}")
    inquire(False)


def withdrawal(num):
    print("---------------取款-----------------------")
    global money
    if money >= num:
        money -= num
        print(f"取款:{num}")
        inquire(False)
    else:
        print("余额不足")


while True:
    res = menu()
    if res == "1":
        inquire(True)
    elif res == "2":
        num = int(input("请输入存款金额:"))
        deposit(num)
    elif res == "3":
        num = int(input("请输入取款金额:"))
        withdrawal(num)
    else:
        print("程序结束")
        break
