from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

data = [
    ("北京市", 99),
    ("湖北省", 199),
    ("江苏省", 599),
    ("河南省", 7),
    ("安徽省", 54),
    ("四川省", 643),
    ("广东省", 1999)
]

map_zn = (
    Map()
    .add("测试地图", data, "china")
    .set_global_opts(
        visualmap_opts=VisualMapOpts(
            is_show=True, is_piecewise=True, pieces=[
                {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
                {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
                {"min": 100, "max": 499, "label": "100-499人", "color": "#FF9966"},
                {"min": 500, "max": 999, "label": "500-999人", "color": "#FF6666"},
                {"min": 1000, "max": 9999, "color": "#CC3333"},
                {"min": 10000, "label": "10000以上", "color": "#990033"},
            ]
        )
    )
    .render("./data/04.html")
)
