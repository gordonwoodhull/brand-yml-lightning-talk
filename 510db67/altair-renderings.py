#| renderings: [light, dark]
r = np.arange(0, 2, 0.01); theta = 2*np.pi*r
df = pd.DataFrame({
    'x': r*np.cos(theta),
    'y': r*np.sin(theta),
    'idx': range(len(r))})
chart = (alt.Chart(df).mark_line(color='blue')
         .encode(x='x', y='y', order='idx')
         .properties(width=450, height=400))

alt.theme.enable('light_theme')
chart.show()

alt.theme.enable('dark_theme')
chart.show()
