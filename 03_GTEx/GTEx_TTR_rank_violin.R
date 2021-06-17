library(reshape)
library(ggplot2)

ranks <- read.csv("GTEx_Brain_TTR_Ranks.csv", header = TRUE)
ranks$X <- NULL # remove column X
ranks_melt <- melt(ranks) # reformat the data 
ranks_melt_NoNA <- na.omit(ranks_melt) # remove rows with NA
# remove rows with tissue name as "value"
ranks_melt_NoNA <- ranks_melt_NoNA[- grep("value", ranks_melt_NoNA$variable),]

library(forcats)
pdf(file = ("Figures/GTEx_jitter_ylim0.pdf"),
    width = 5.15,
    height = 3.75
)
#title <- c("GTEx\n", TTR rank", expression(paste(italic("TTR"), " rank")))
title <- expression(paste
                    (atop("GTEx ",
                          paste(italic("TTR")," rank"))))

p <- ggplot(ranks_melt_NoNA, aes(x=reorder(variable, -value, fun = median), y=value)) + 
  geom_violin() +
  geom_boxplot(width=0.1, color="black", alpha=0.1, outlier.shape = NA) +
  geom_jitter(position=position_jitter(0.2), color = "blue", alpha =.35, size =.1) +
  xlab("Tissue") + ylab("Rank")  + ylim(0,100) +
  theme(axis.text.x = element_text(angle = 55, hjust =1, size=10)) + # rotate the X axis labels
  ggtitle(title)+ 
  theme(plot.title = element_text(size=12)) +
  theme(axis.title.x=element_text(size=12), 
        axis.text.x=element_text(size=9)) +
  theme(axis.title.y=element_text(size=12),
        axis.text.y=element_text(size=12)) +
  scale_x_discrete(labels= c("Amygdala" = "Amygdala", "Anterior_Cingulate_Cortex" = "Anterior cortex", "Caudate_Basal_Ganglia" = "Caudate basal ganglia", "Cerebellar_Hemisphere" = "Cerebellar hemisphere", "Cerebellum" = "Cerebellum", "value" = "value", "Frontal_Cortex_BA9" = "Frontal cortex", "Hippocampus" = "Hippocampus", "Hypothalamus" = "Hypothalamus", "Nucleus_Accumbens_Basal_Ganglia" = "Nucleus accumbens", "Putamen_Basal_Ganglia" = "Putamen basal ganglia", "Spinal_Cord_C1" = "Spinal cord", "Substantia_Nigra" = "Substantia nigra"))
p
dev.off()
dev.off()

