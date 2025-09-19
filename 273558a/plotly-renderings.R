#| renderings: [light, dark]
t <- seq(0, 720, length.out=400)
r <- seq(0, 2, length.out=400)
fig <- plot_ly(width=400, height=400,
      r=r, theta=t, type='scatterpolar',
      mode='lines', line=list(color='blue')) %>%
    layout(
      polar=list(bgcolor="transparent"),
      paper_bgcolor="transparent")

fig |> light_theme()
fig |> dark_theme()
