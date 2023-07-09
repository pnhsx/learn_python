from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = (
    Bar()
    .add_xaxis(["中国", "美国", "英国"], )
    .add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
    .reversal_axis()
)
bar2 = (
    Bar()
    .add_xaxis(["中国", "美国", "英国"], )
    .add_yaxis("GDP", [50, 60, 40], label_opts=LabelOpts(position="right"))
    .reversal_axis()
)
bar3 = (
    Bar()
    .add_xaxis(["中国", "美国", "英国"], )
    .add_yaxis("GDP", [70, 80, 60], label_opts=LabelOpts(position="right"))
    .reversal_axis()
)

timeline = Timeline({"theme":ThemeType.LIGHT})

timeline.add(bar1, "2018")
timeline.add(bar2, "2019")
timeline.add(bar3, "2020")
timeline.add_schema(
    play_interval=1000,         # 自动播放时间间隔,单位毫秒
    is_timeline_show=True,      # 是否在自动播放时,显示时间线
    is_auto_play=True,          # 是否自动播放
    is_loop_play=True           # 是否循环自动播放
)
timeline.render("./data/08.html")




from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts

# x_data = ["中国", "美国", "英国"]
# y_data = [[30, 20, 10], [50, 60, 40], [70, 80, 60]]
# timeline = Timeline()
# for i, year in enumerate(["2018", "2019", "2020"]):
#     bar = (
#         Bar()
#         .add_xaxis(x_data)
#         .add_yaxis("GDP", y_data[i], label_opts=LabelOpts(position="right"))
#         .reversal_axis()
#     )
#     timeline.add(bar, year)
# timeline.add_schema(
#     play_interval=1000,
#     is_timeline_show=True,
#     is_auto_play=True,
#     is_loop_play=True
# )
# timeline.render("./data/08.html")
