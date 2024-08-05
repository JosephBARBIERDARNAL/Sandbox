# Load required libraries
library(ggplot2)
library(hexSticker)

# Create a base plot
p <- ggplot() +
  geom_polygon(aes(x = c(-1, 1, 1, -1), y = c(-1, -1, 1, 1)),
    fill = "#2C3E50", color = "white"
  ) +
  annotate("text",
    x = 0, y = 0.5, label = "EcoModel",
    size = 8, color = "white", fontface = "bold"
  ) +
  annotate("text",
    x = 0, y = -0.5, label = "R Package",
    size = 6, color = "white"
  ) +
  theme_void()

# Create the sticker
sticker(p,
  package = "EcoModel",
  p_size = 20, s_x = 1, s_y = 0.8, s_width = 1.5,
  h_fill = "#3498DB", h_color = "#1ABC9C",
  filename = "EcoModel_logo.png"
)
