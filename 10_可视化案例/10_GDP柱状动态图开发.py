"""
    GDP 柱状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

f = open("./data/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
f.close()
data_lines.pop(0)

data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])

    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

stored_year_list = sorted(data_dict.keys())

timeline = Timeline({"theme":ThemeType.LIGHT})

for year in stored_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for data in year_data:
        x_data.append(data[0])
        y_data.append(data[1])

    x_data.reverse()
    y_data.reverse()
    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis("GDP", y_data, label_opts=LabelOpts(position="right"))
        .reversal_axis()
        .set_global_opts(title_opts=TitleOpts(title=f"{year}年全球前8GDP排行"))
    )

    timeline.add(bar, str(year))


timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
timeline.render("./data/10.html")
