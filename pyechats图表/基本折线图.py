# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 2/27/2023 1:42 PM
# 文件名称: 基本折线图.PY

# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,ToolboxOpts
# 创建一个折线图对象
line = Line()

#给折线图添加X轴数据
line.add_xaxis(["中国","美国","英国"])

# 添加y轴数据
line.add_yaxis("GDP",[30,20,10])

#设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),
    toolbox_opts=ToolboxOpts(is_show=True)
)

#通过render方法 将代码生成图像
line.render()


