#| renderings: [light, dark]
t <- seq(0, 720, length.out=400)  # 720 degrees = 2 full rotations
r <- seq(0, 2, length.out=400)     # Radius from 0 to 2
fig <- plot_ly(width=400, height=400, r=r, theta=t, type='scatterpolar', mode='lines', line=list(color='blue')) %>%
    layout(polar=list(bgcolor="transparent"), paper_bgcolor="transparent")

fig |> light_theme()
fig |> dark_theme()
