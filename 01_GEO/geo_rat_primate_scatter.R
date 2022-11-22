setwd("~/Dropbox/Mac/Documents/poster_presentations")
library(ggplot2)
rat <- read.table("geo_rat.tsv", header = TRUE, sep = "\t")
primate <- read.table("geo_primate.tsv", header = TRUE, sep = "\t")
rat$Strain <- factor(rat$Strain)
rat$Tissue <- factor(rat$Tissue, levels = c("hippocampus","cerebellum","amygdala",
                                            "ventral striatum","dorsal striatum",
                                            "cerebral cortex","frontal cortex"))
primate$Group <- factor(as.character(primate$Group),levels = c("young","old","old + amyloid"))
primate$Sex <- factor(primate$Sex)

p1 <- ggplot(rat, aes(Tissue, Value)) +
  geom_jitter(aes(color=Strain), size = 5) +
  theme_classic() +
  scale_color_manual(values = c("yellow3", "green4","purple")) +
  labs(title = paste0("GEO GDS589\nRat"), x=NULL, y="Value") +
  theme(axis.text.x = element_text(angle = 45, hjust =1, size=14)) +
  theme(axis.title.x = element_text(size = 28), axis.text.x = element_text(size = 16)) +
  theme(axis.title.y = element_text(size = 28), axis.text.y = element_text(size = 16)) +
  theme(plot.title = element_text(size = 28)) +
  theme(legend.text=element_text(size=16), legend.title = element_text(size = 14)) +
  ylim(0,1500)
p1

p2 <- ggplot(primate, aes(Group, Value)) +
  geom_jitter(aes(color=Sex), size = 5) +
  theme_classic() +
  scale_color_manual(values = c("yellow3", "green4")) +
  labs(title = paste0("GEO GDS589\nGray Mouse Lemur"), x=NULL, y="Value") +
  theme(axis.text.x = element_text(angle = 45, hjust =1, size=14)) +
  theme(axis.title.x = element_text(size = 28), axis.text.x = element_text(size = 16)) +
  theme(axis.title.y = element_text(size = 28), axis.text.y = element_text(size = 16)) +
  theme(plot.title = element_text(size = 28)) +
  theme(legend.text=element_text(size=16),legend.title = element_text(size = 14)) +
  ylim(0,25000)
p2

library(gridExtra)

plots1 <- list(p1,p2)
layout1 <- cbind(c(1,2))
grid1 <- grid.arrange(grobs = plots1, layout_matrix = layout1)
