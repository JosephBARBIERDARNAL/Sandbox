library(rayshader)
library(terra)
# Define a region for the SRTM data (example: Swiss Alps)
extent_alps <- extent(7.0, 9.0, 46.0, 47.5)

# Download SRTM data
srtm_alps <- getData("SRTM", lon = 8.0, lat = 46.75)

# Crop the SRTM data to the defined extent
srtm_alps_cropped <- crop(srtm_alps, extent_alps)

# Convert the raster data to matrix
elevation_matrix <- raster_to_matrix(srtm_alps_cropped)



elevation_matrix %>%
  sphere_shade(texture="desert", sunangle = 45) %>%
  add_water(detect_water(elevation_matrix)) %>%
  add_shadow(ray_shade(elevation_matrix), 0.5) %>% # this line adds a shadow
  add_shadow(ambient_shade(elevation_matrix), 0) %>% # this line adds an ambient shadow
  plot_3d(elevation_matrix, zscale = 50)
render_snapshot()