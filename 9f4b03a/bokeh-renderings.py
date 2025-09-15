#| renderings: [light, dark]
from bokeh.plotting import figure, show
import numpy as np
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
p = figure(width=300, height=300, toolbar_location=None, match_aspect=True)
p.line(r * np.cos(theta), r * np.sin(theta), line_color="blue")
#p.axis.visible = False; p.grid.visible = False; p.outline_line_color = None

light_theme()
show(p)

# dark_theme()
# show(p)
