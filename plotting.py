from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds = ColumnDataSource(df)

fig = figure(x_axis_type='datetime', height=300,
             width=750, title="Motion graph")

fig.yaxis.minor_tick_line_color = None
fig.yaxis.ticker.desired_num_ticks = 1

hover = HoverTool(
    tooltips=[("Start:", "@Start_string"), ("End:", "@End_string")])
fig.add_tools(hover)

q = fig.quad(left="Start", right="End", bottom=0,
             top=1, color="green", source=cds)

output_file("graph.html")
show(fig)
