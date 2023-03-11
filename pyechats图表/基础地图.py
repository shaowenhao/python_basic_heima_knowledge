# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/27/2023 4:47 PM
# 文件名称: 基础地图.PY

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()

data = [
    ("北京",99),
    ("上海",199),
    ("广州",299),
    ("福建",399)
]

map.add("测试地图",data,"china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"label":"1-99","color":"#CCFFFF"},
            {"min":100,"max":199,"label":"10-199","color":"#FF6666"},
            {"min":200,"max":299,"label":"200-299","color":"#990033"}
        ]
    )
)

map.render()

