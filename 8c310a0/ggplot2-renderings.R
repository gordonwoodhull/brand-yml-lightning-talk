#| renderings: [light, dark]
library(ggplot2)

r <- seq(0, 2, by=0.01)
theta <- 2 * pi * r
plot <- ggplot(
  data.frame(
    x=r*cos(theta),
    y=r*sin(theta)),
  aes(x, y)) +
  geom_path(color="blue") +
  coord_fixed() +
  theme_minimal()

plot + light_theme
plot + dark_theme
