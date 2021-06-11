library(reshape)
library(ggplot2)

setwd("/Users/m239830/Dropbox (ASU)/Fryer_Lab/TTR/GTEx/")
ranks <- read.csv("GTEx_Brain_TTR_Ranks.csv", header = TRUE)
ranks$X <- NULL # remove column X
ranks_melt <- melt(ranks) # reformat the data 
ranks_melt_NoNA <- na.omit(ranks_melt) # remove rows with NA
# remove rows with tissue name as "value"
ranks_melt_NoNA <- ranks_melt_NoNA[- grep("value", ranks_melt_NoNA$variable),]


# plot
p <- ggplot(ranks_melt_NoNA, aes(x=variable, y=value)) + 
  geom_violin() +
  geom_boxplot(width=0.1, color="grey", alpha=0.2) +
  geom_jitter(position=position_jitter(0.2)) +
  xlab("Tissue") + ylab("rank")  +
  theme(axis.text.x = element_text(angle = 75, hjust =1)) # rotate the X axis labels

p 
p +ggtitle("TTR rank in GTEx brain samples")
