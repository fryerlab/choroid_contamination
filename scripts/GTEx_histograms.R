setwd("/Users/m239830/Dropbox (ASU)/Fryer_Lab/TTR/GTEx")

# install packages
# if (!requireNamespace("BiocManager", quietly = TRUE))
#   install.packages("BiocManager")
# BiocManager::install("SciencesPo")

# load packages
library(ggplot2) 
library(gridExtra) 
library(reshape)
library(dplyr)
library(tidyr)
library(gridExtra)

# rename the GTEx files replacing "-" with "_"
folder = "/Users/m239830/Dropbox (ASU)/Fryer_Lab/TTR/GTEx"
files <- list.files(folder,pattern = "Brain",full.names = T) 
sapply(files,FUN=function(eachPath){ 
  file.rename(from=eachPath,to= sub(pattern="-", paste0("_"),eachPath))
})
# remove the path information and only keep the name of the files
GTEx <- basename(file.path(files)) 

# only need to do once

# removing the "_counts_mean.txt" from each file name
# sapply(GTEx,FUN=function(eachPath){ 
#   file.rename(from=eachPath,to= sub(pattern="_counts_mean.txt", paste0(""),eachPath))
# })


#----
# read in each tissue file
# pull out TTR gene information, reformat file for down stream use
# take the log2 of TTR values
#---
for(x in GTEx) {
  t <- read.delim(x) # read in each tissue file
  names(t)[names(t) == "Description"] <- "Geneid" # rename Description to Geneid
  tissue <- subset(t, (t$Geneid == "TTR")) # subset each tissue file to only look at TTR 
  tissue$X <- NULL
  tissue$Name <- NULL
  tissue$mean <- NULL
  tissue$median <- NULL
  tissue <- melt(tissue) # will say "Using Geneid as id variable"
  # the new tissue file will have 3 columns: Geneid  variable  value
  tissue$log2 <- log2(tissue$value + 0.01) # add a 4th column that is the log2 value of TTR
  # adding 0.01 prevents taking the log of zero 
  tissue$tissue <- paste0("", x)
  assign(paste(x, sep = ''), tissue) # assign each tissue as an output
}

# rbind all of the tissues together 
do.matrix <- do.call(rbind, lapply( ls(patt="Brain"), get) )
# convert the matrix into a data.frame
DF <- as.data.frame(do.matrix)

#----
# make a histogram plot of the log2 TTR values for each tissue in DF 
#---
HIST_Func <- function(a) {
  tissue <- subset(DF, DF$tissue == a)
  ggplot(tissue, aes(x = log2)) +
    geom_histogram(bins=100) +
    labs(title = a) +ylim(0,15) + xlim(-10,13) 
   # scale_x_continuous(breaks = scales::pretty_breaks(n = 8))
}
Map(HIST_Func, a = GTEx)
HIST_Func <- function(a) {
  tissue <- subset(DF, DF$tissue == a)
  ggplot(tissue, aes(x = value)) +
 # geom_density(alpha=.2, fill="#FF6666") +
  geom_histogram(      # Histogram with density instead of count on y-axis
              # binwidth=.5, 
               bins = 70,
               colour="black", fill="gray") +
  labs(title = a)# + xlim(-7,12.5)
}
all_plots <- Map(HIST_Func, a = GTEx)

a <- all_plots[[1]]
b <- all_plots[[2]]
c <- all_plots[[3]]
d <- all_plots[[4]]
e <- all_plots[[5]]
f <- all_plots[[6]]
g <- all_plots[[7]]
h <- all_plots[[8]]
i <- all_plots[[9]]
j <- all_plots[[10]]
k <- all_plots[[11]]
l <- all_plots[[12]]
m <- all_plots[[13]]
grid.arrange(a, b, c, d, e, f, g, h, i, j, k, l, m, ncol = 2)
cowplot::plot_grid(plotlist = all_plots[[1]])
