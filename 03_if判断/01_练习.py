"""
print("欢迎来到黑马游乐园,儿童免费,成人收费")
age = int(input("你的年龄为:"))

if age >= 18:
    print("您已成年,游玩需要补票10元")

print("祝您游玩愉快")
"""
"""
height = int(input("请输入您的身高:"))

if height > 120:
    print("您的身高超出120cm,需要购票")
else:
    print("您的身高不满120cm,免费游玩")
"""
if int(input("年龄:")) < 18:
    print('未成年免费游玩')
elif int(input("vip等级:")) > 3:
    print('vip3级以上免费')
elif int(input("今天几号:")) == 1:
    print("1号免费")
