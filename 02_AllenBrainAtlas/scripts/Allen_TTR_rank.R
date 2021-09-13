library(reshape2)
library(dplyr)

#- read in Allen Brain TPM counts
genes <- read.delim("geneInfo.txt")
hip.counts <- read.delim("hippocampus_tpm_counts.txt")
FWM.counts <- read.delim("FWM_tpm_counts.txt")
PCx.counts <- read.delim("PCx_tpm_counts.txt")
TCx.counts <- read.delim("TCx_tpm_counts.txt")

# gene and count dataframes
hip.df <- cbind(genes$gene_symbol, hip.counts)
FWM.df <- cbind(genes$gene_symbol, FWM.counts)
PCx.df <- cbind(genes$gene_symbol, PCx.counts)
TCx.df <- cbind(genes$gene_symbol, TCx.counts)

# percentail rank function
foo = function(x){
  pr <- percent_rank(x)
  return(c(pr))
}

hip.pr <- sapply(hip.df, foo)
hip.pr.df <- as.data.frame(hip.pr)
hip.pr.df$Description <- genes$gene_symbol
hip.ranks <- subset(hip.pr.df, Description == "TTR")

FWM.pr <- sapply(FWM.df, foo)
FWM.pr.df <- as.data.frame(FWM.pr)
FWM.pr.df$Description <- genes$gene_symbol
FWM.ranks <- subset(FWM.pr.df, Description == "TTR")

PCx.pr <- sapply(PCx.df, foo)
PCx.pr.df <- as.data.frame(PCx.pr)
PCx.pr.df$Description <- genes$gene_symbol
PCx.ranks <- subset(PCx.pr.df, Description == "TTR")

TCx.pr <- sapply(TCx.df, foo)
TCx.pr.df <- as.data.frame(TCx.pr)
TCx.pr.df$Description <- genes$gene_symbol
TCx.ranks <- subset(TCx.pr.df, Description == "TTR")

hip.ranks$`genes$gene_symbol` <- NULL # remove column X
hip.ranks.melt <- melt(hip.ranks) # reformat the data 
hip.ranks.melt$Tissue <- "Hippocampus"

FWM.ranks$`genes$gene_symbol` <- NULL # remove column X
FWM.ranks.melt <- melt(FWM.ranks) # reformat the data 
FWM.ranks.melt$Tissue <- "Frontal white matter"

PCx.ranks$`genes$gene_symbol` <- NULL # remove column X
PCx.ranks.melt <- melt(PCx.ranks) # reformat the data 
PCx.ranks.melt$Tissue <- "Parietal cortex "

TCx.ranks$`genes$gene_symbol` <- NULL # remove column X
TCx.ranks.melt <- melt(TCx.ranks) # reformat the data 
TCx.ranks.melt$Tissue <- "Temporal cortex "

ranks <- rbind(hip.ranks.melt, FWM.ranks.melt, PCx.ranks.melt, TCx.ranks.melt)
ranks$value <- (ranks$value)*100
#---------
library(reshape)
library(ggplot2)
library(forcats)

pdf(file = ("Allen_Brain_jitter_rank.pdf"),
    width = 3.5,
    height = 3.8
)
#title <- expression(paste(italic("TTR"), " rank", " \n\n Allen Brain Atlas samples"))

title <- expression(paste
                    (atop("Allen Brain Atlas",
                          paste(italic("TTR")," rank"))))


#title <- expression(paste (atop("Allen Brain Atlas ", paste(italic("TTR")," rank"))))
p <- ggplot(ranks, aes(x=reorder(Tissue, -value, fun = median), y=value)) + 
  geom_violin() +
  geom_boxplot(width=0.1, color="black", alpha=0.1, outlier.shape = NA) +
  geom_jitter(position=position_jitter(0.2), color = "blue", alpha =.35, size =.1) +
  xlab("Tissue") + ylab("Rank")  +
  theme(axis.text.x = element_text(angle = 55, hjust =1, size=10)) + # rotate the X axis labels
  ggtitle(title)+ 
  theme(plot.title = element_text(size=12)) +
  theme(axis.title.x=element_text(size=12), 
        axis.text.x=element_text(size=9)) +
  theme(axis.title.y=element_text(size=12),
        axis.text.y=element_text(size=12)) 
 # scale_x_discrete(labels= c("Amygdala" = "Amygdala", "Anterior_Cingulate_Cortex" = "Anterior cortex", "Caudate_Basal_Ganglia" = "Caudate basal ganglia", "Cerebellar_Hemisphere" = "Cerebellar hemisphere", "Cerebellum" = "Cerebellum", "value" = "value", "Frontal_Cortex_BA9" = "Frontal cortex", "Hippocampus" = "Hippocampus", "Hypothalamus" = "Hypothalamus", "Nucleus_Accumbens_Basal_Ganglia" = "Nucleus accumbens", "Putamen_Basal_Ganglia" = "Putamen basal ganglia", "Spinal_Cord_C1" = "Spinal cord", "Substantia_Nigra" = "Substantia nigra"))
p
dev.off()
