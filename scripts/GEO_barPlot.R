# bar plot of GEO 

# setwd
setwd("/Users/m239830/Dropbox (ASU)/Fryer_lab/TTR")

library(tidyverse)
library(scales)
library(ggplot2)

# read in GEO value and rank priority 
# https://docs.google.com/spreadsheets/d/1OyNS1Te3rZMD0HJXNfpUq-zcvirqBK_tVfUhUpXDt7g/edit?usp=sharing 
GEO <- read.delim("GEO_updated.txt", header = TRUE, sep = "\t")

# bar plot
png(filename ="Value.png",width=6,height=6,units="in",res=1200)

bar_plot_value <- ggplot(GEO, aes(x=Value, fill=as.factor(Value))) + geom_bar()+
  xlab("Value Priority") +
  ylab("Count") +
  scale_fill_brewer(palette = "Set1", name = "Value priority", labels = c("1 = exclusively between groups", "2 = moderately between groups", "3 = no clear pattern", "4 = highly expressed among samples", "5 = lowly expressed among samples")) +
  theme_bw()
bar_plot_value +geom_text(aes(label = scales::percent(..prop..), group = 1), stat= "count",  vjust=-0.25)
dev.off()
dev.off()
# Summarize to get counts and percentages
png(filename ="Rank.png",width=6,height=6,units="in",res=1200)
bar_plot_rank <- ggplot(GEO, aes(x=Rank, fill=as.factor(Rank))) + geom_bar() +
 xlab("Rank Priority") +
 ylab("Count") +
  scale_fill_brewer(palette = "Pastel1", name = "Rank priority", labels = c("1 = exclusively between groups", "2 = moderately between groups", "3 = no clear pattern", "4 = highly ranked among samples", "5 = lowly ranked among samples")) +
  theme_bw()
bar_plot_rank +geom_text(aes(label = scales::percent(..prop..), group = 1), stat= "count",  vjust=-0.25)
dev.off()

#pie chart



