library(ggraph)
library(igraph)
library(tidyverse)
library(dplyr)
library(dendextend)
library(colormap)

data <- read.table("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/13_AdjacencyUndirecterWeighted.csv", header=T, row.names="Cities.", sep=",")# %>% as.matrix
colnames(data) <- gsub("\\.", " ", colnames(data))
data <- as.data.frame(data)
str(data)
str(data)
head(data)

dend <- as.dist(data) %>%
  hclust(method="ward.D") %>%
  as.dendrogram()
