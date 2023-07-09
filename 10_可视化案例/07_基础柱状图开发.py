from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar1 = (
    Bar()
    .add_xaxis(["中国", "美国", "英国"], )
    .add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
    .reversal_axis()
    .render("./data/07.html")
)


#
# from pyecharts.charts import Bar
# from pyecharts.options import LabelOpts
#
# data = [("中国", 30), ("美国", 20), ("英国", 10)]
# bar2 = (
#     Bar()
#     .add_xaxis([x[0] for x in data])
#     .add_yaxis("GDP", [x[1] for x in data], label_opts=LabelOpts(position="right"))
#     .reversal_axis()
#     .render("./data/07.html")
# )
