def check(num):
    print("欢迎来到黑马程序员,请出示核算证明,测量体温")
    if num <= 37.5:
        print(f"您的体温是{num},体温正常,请进")
    else:
        print(f"您的体温是{num},需要隔离")


check(39.0)
check(36.3)
check(37.4)
check(37.6)
