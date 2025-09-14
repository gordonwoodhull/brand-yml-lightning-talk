#| renderings: [light, dark]
from plotnine import *
import numpy as np
import pandas as pd

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
df = pd.DataFrame(
  {'x': r*np.cos(theta),
   'y': r*np.sin(theta)})
plot = (ggplot(df, aes('x', 'y'))
  + geom_path(color="blue")
  + coord_fixed(ratio=1)
  + theme_minimal())
(plot + light_theme).show()
(plot + dark_theme).show()
