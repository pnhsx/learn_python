"""
文件相关的类定义
"""
from data_define import Record
import json


# 定义一个抽象类对象用来做顶层设计,确定有哪些功能要实现

class FileReader:

    def read_data(self):
        # 读取文件数据,读取到的每一条数据都转换问 Record对象,将他们都封装到list内返回
        pass


class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    # 复写父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="utf-8")
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="utf-8")
        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("./2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("./2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()
    for l in list1:
        print(l)
    for l in list2:
        print(l)
