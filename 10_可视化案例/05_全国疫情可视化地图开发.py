import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 读取数据
with open("./data/疫情.txt", "r", encoding="utf-8") as f:
    data = f.read()
# 解析数据
data_dict = json.loads(data)
province_data_list = data_dict["areaTree"][0]["children"]
data_list = []
for element in province_data_list:

    province_confirm = (element["name"] + "省", element["total"]["confirm"])
    data_list.append(province_confirm)


# 配置颜色区间
color_config = [
    {"min": 1, "max": 99},
    {"min": 100, "max": 999},
    {"min": 1000, "max": 4999},
    {"min": 5000, "max": 9999},
    {"min": 10000, "max": 99999},
    {"min": 100000, "label": "100000+"}
]
# 创建地图
map1 = (
    Map()
    .add("疫情地图", data_list, "china")
    .set_global_opts(
        visualmap_opts=VisualMapOpts(
            is_show=True,
            is_piecewise=True,
            pieces=color_config
        )
    )
    .render("./data/05.html")
)
