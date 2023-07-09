from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

line = Line()
line.add_xaxis(["中国", "美国", "英国"])
line.add_yaxis("GDP", [30, 20, 10])
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)
line.render("./data/02_data.html")

"""
from pyecharts.charts import Line
from pyecharts import options as opts
line = (
    Line()
    .add_xaxis(["中国", "美国", "英国"])
    .add_yaxis("GDP", [30, 20, 25])
    .set_global_opts(title_opts=opts.TitleOpts(title="GDP"))
    .render("./data/data.html")
)
"""
"""
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

line = (
    Line()
    .add_xaxis(["中国", "美国", "英国"])
    .add_yaxis("GDP", [30, 20, 10])
    .set_global_opts(
        title_opts=TitleOpts(title="GDP展示"),
        legend_opts=LegendOpts(is_show=True),
        toolbox_opts=ToolboxOpts(is_show=True),
        visualmap_opts=VisualMapOpts(is_show=True),
    )
    .render("./data/data.html")
)
"""
