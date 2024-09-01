import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,LabelOpts

# 读取数据
file_usa = open('data/USA.txt','r',encoding='utf-8')
file_jp = open('data/Japan.txt','r',encoding='utf-8')
file_id = open('data/India.txt','r',encoding='utf-8')
# 获取文件内容
usa_data = file_usa.read()
jp_data = file_jp.read()
id_data = file_id.read()
# 删除不合理部分
usa_data = usa_data.replace("jsonp_1629344292311_69436(","")
usa_data = usa_data[:-2]
jp_data = jp_data.replace("jsonp_1629350871167_29498(","")
jp_data = jp_data[:-2]
id_data = id_data.replace("jsonp_1629350745930_63180(","")
id_data = id_data[:-2]
# 通过json转换python字典
usa_dict = json.loads(usa_data)
jp_dict = json.loads(jp_data)
id_dict = json.loads(id_data)
# 获取trend key
usa_trend = usa_dict['data'][0]['trend']
jp_trend = jp_dict['data'][0]['trend']
id_trend = id_dict['data'][0]['trend']
# 获取截止2020年12月31日的全部日期数据(索引为314)用于x轴数据
us_x_data = usa_trend['updateDate'][:314]
jp_x_data = jp_trend['updateDate'][:314]
id_x_data = id_trend['updateDate'][:314]
# 获取对应的全部确诊数据(索引为314)
us_y_data = usa_trend['list'][0]['data'][:314]
jp_y_data = jp_trend['list'][0]['data'][:314]
id_y_data = id_trend['list'][0]['data'][:314]
# 构建折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(us_x_data)
#  添加y轴数据
line.add_yaxis("美国",us_y_data,label_opts=LabelOpts(is_show=False)) # 使数值标注不显示
line.add_yaxis("日本",jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度",id_y_data,label_opts=LabelOpts(is_show=False))
# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="Covid-19 Data Of USA, Japan and India",
                         subtitle="2020",
                         pos_left="center",
                         pos_top="bottom"
                        ),
    legend_opts=LegendOpts(is_show=True),
)
# 生成图表
line.render("covid_data.html")
# 关闭文件
file_usa.close()
file_jp.close()
file_id.close()