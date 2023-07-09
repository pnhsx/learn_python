# 单继承

class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_4g(self):
        print("4g通话")


class Phone2022(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("2022新功能,5g通话")


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()


# 多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("nfc读卡")

    def write_card(self):
        print("nfc写卡")


class RemoteContral:
    rc_type = "红外遥控"

    def contral(self):
        print("红外遥控开启了")


class MyPhone(Phone, NFCReader, RemoteContral):
    pass


phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.contral()

print(phone.producer)
