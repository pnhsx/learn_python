from pyecharts.charts import Map
from pyecharts.options import *
import json

f = open("./data/疫情.txt", "r", encoding="utf-8")
data = f.read()
f.close()

data_dict = json.loads(data)
epidemic_data = data_dict["areaTree"][0]["children"][3]["children"]

data_list = []
for element in epidemic_data:
    data_set = (element["name"] + "市", element["total"]["confirm"])
    data_list.append(data_set)

data_list.append(("济源市", 5))

# color_config = [
#     {"min": 1, "max": 99},
#     {"min": 100, "max": 999},
#     {"min": 1000, "max": 4999},
#     {"min": 5000, "max": 9999},
#     {"min": 10000, "max": 99999},
#     {"min": 100000, "label": "100000+"}
# ]

map2 = (
    Map()
    .add("河南疫情", data_list, "河南")
    .set_global_opts(
        title_opts=TitleOpts(title="河南疫情地图"),
        visualmap_opts=VisualMapOpts(
            is_show=True,
            # is_piecewise=True,
            # pieces=color_config
        )
    )
    .render("./data/06.html")
)
