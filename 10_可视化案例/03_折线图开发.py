"""
    可视化需求:折线图开发
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# 处理数据
f_us = open("./data/美国.txt", "r", encoding="utf-8")
us_data = f_us.read()

f_jp = open("./data/日本.txt", "r", encoding="utf-8")
jp_data = f_jp.read()

f_in = open("./data/印度.txt", "r", encoding="utf-8")
in_data = f_in.read()

# 去除首尾不规范字符
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_data = us_data[:-2]
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
jp_data = jp_data[:-2]
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
in_data = in_data[:-2]

# json 转 pyth
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取 trend key
us_trend_data = us_dict["data"][0]["trend"]
jp_trend_data = jp_dict["data"][0]["trend"]
in_trend_data = in_dict["data"][0]["trend"]
# print(trend_data)
# print(type(trend_data))

# 获取 x,y轴数据
us_x_data = us_trend_data["updateDate"][0:314]
us_y_data = us_trend_data["list"][0]["data"][0:314]
jp_x_data = jp_trend_data["updateDate"][0:314]
jp_y_data = jp_trend_data["list"][0]["data"][0:314]
in_x_data = in_trend_data["updateDate"][0:314]
in_y_data = in_trend_data["list"][0]["data"][0:314]

line = (
    Line()
    .add_xaxis(us_x_data)
    .add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
    .add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
    .add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=TitleOpts(title="2020年美日印三国确诊人数", pos_left="center", pos_bottom="1%")
    )
    .render("./data/03.html")
)

f_us, f_jp, f_in.close()
