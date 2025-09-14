#| renderings: [light, dark]

import numpy as np
import matplotlib.pyplot as plt
from quarto import theme_colors_matplotlib;

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

light_style()
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.grid(True)
plt.show()

dark_style()
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.grid(True)
plt.show()