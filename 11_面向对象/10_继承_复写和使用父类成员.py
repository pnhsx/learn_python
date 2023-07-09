class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("使用5g网络进行通话")


class MyPhone(Phone):
    prodecer = "ITHEIMA"

    def call_by_5g(self):
        print("开启CPU单核模式,省电")
        # # 方式 1
        # print(f"父类的厂商是{Phone.producer}")
        # Phone.call_by_5g(self)
        # 方式 2
        print(f"父类的厂商是{super().producer}")
        super().call_by_5g()
        print("关闭CPU单核模式,确保性能")


phone = MyPhone()
phone.call_by_5g()
print(phone.prodecer)
