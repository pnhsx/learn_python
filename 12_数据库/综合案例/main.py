"""
面向对象,数据分析案例,主业务逻辑代码
实现步骤:
1. 设计一个类,可以完成数据的封装
2. 设计一个抽象类,定义文件读取的相关功能,并使用子类实现具体功能
3. 读取文件,产生数据对象
4. 进行数据需求的逻辑计算 (计算每一天的销售额)
5. 通过PyEcharts进行图形绘制

"""

from data_define import Record
from file_define import TextFileReader, JsonFileReader
from pymysql import Connect

text_file_reader = TextFileReader("./2011年1月销售数据.txt")
json_file_reader = JsonFileReader("./2011年2月销售数据JSON.txt")

jan_data = text_file_reader.read_data()
feb_data = json_file_reader.read_data()

all_data: list[Record] = jan_data + feb_data

conn = Connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True
)
cursor = conn.cursor()
conn.select_db('py_sql')

for record in all_data:
    sql = f"insert into orders(order_date,order_id,money,province) " \
          f"values('{record.data}','{record.order_id}',{record.money},'{record.province}')"
    执行
    cursor.execute(sql)

conn.close()
