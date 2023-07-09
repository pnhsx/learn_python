# 定义一个类, 内含私有成员变量或方法

class Phone:
    __current_voltage = 0.5  # 当前手机运行电压

    def __keep_single_core(self):
        print("让CPU以单核运行")

    def call_by_5G(self):
        if self.__current_voltage >= 1:
            print("5G通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足,无法使用5G通话,并以设置为单核模式运行进行省电")


phone = Phone()
# phone.__keep_single_core()
# print(phone.__current_voltage)
phone.call_by_5G()
