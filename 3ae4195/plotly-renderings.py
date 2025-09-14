#| renderings: [light, dark]
theta = np.linspace(0, 720, 400)
r = np.linspace(0, 2, 400)
transparent = "rgba(0,0,0,0)"
fig = go.Figure(go.Scatterpolar(r=r, theta=theta, mode='lines', line=dict(color='blue')))
fig.update_layout(width=400, height=400,
                  margin=dict(l=35, r=25, t=25, b=25),
                  polar=dict(bgcolor=transparent), paper_bgcolor=transparent)

fig.update_layout(template='light_brand')
display(fig)

fig.update_layout(template='dark_brand')
display(fig)
