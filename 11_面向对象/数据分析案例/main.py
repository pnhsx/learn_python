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
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader("./2011年1月销售数据.txt")
json_file_reader = JsonFileReader("./2011年2月销售数据JSON.txt")

jan_data = text_file_reader.read_data()
feb_data = json_file_reader.read_data()

all_data: list[Record] = jan_data + feb_data

data_dict = {}
for record in all_data:
    if record.data in data_dict:
        data_dict[record.data] += record.money
    else:
        data_dict[record.data] = record.money

# 可视化图表开发

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.add_xaxis(list(data_dict.keys()))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render("./每日销售额柱状图.html")


"""
from collections import defaultdict
from data_define import Record
from file_define import TextFileReader, JsonFileReader
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType


def calculate_daily_sales(data):
    data_dict = defaultdict(float)
    for record in data:
        data_dict[record.data] += record.money
    return data_dict


def create_chart(data_dict):
    bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
    bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
    bar.add_xaxis(list(data_dict.keys()))
    bar.set_global_opts(
        title_opts=TitleOpts(title="每日销售额")
    )
    bar.render("./每日销售额柱状图.html")


text_file_reader = TextFileReader("./2011年1月销售数据.txt")
json_file_reader = JsonFileReader("./2011年2月销售数据JSON.txt")
jan_data = text_file_reader.read_data()
feb_data = json_file_reader.read_data()
all_data = jan_data + feb_data
data_dict = calculate_daily_sales(all_data)
create_chart(data_dict)
"""
