#----
# TTR expression in GTEx tissues
#-----
# set working directory
setwd("/Users/m239830/Dropbox (ASU)/Fryer_Lab/TTR/GTEx")

# create an empty data frame
df <- data.frame()

# read in  tissue files
Brain_Caudate <- read.delim("Brain-Caudate_basalganglia_counts_mean.txt", header = TRUE, sep = "\t")

# number of samples
dim <- dim(Brain_Caudate)
numberOfSamples <- dim[2] -5
# percentile rank of each gene
Brain_Caudate_rank = mutate(Brain_Caudate, percentile_rank = ntile(Brain_Caudate$mean,100))

# subset tissue file to only look at TTR
Brain_Caudate_TTR <- subset(Brain_Caudate_rank, Description == "TTR")

# add information to the empty data frame
df <- rbind(df, c("Brain_Caudate", numberOfSamples, Brain_Caudate_TTR$mean, Brain_Caudate_TTR$median, Brain_Caudate_TTR$percentile_rank))

# histogram of TTR expression across samples for each tissue
drops <- c("X", "name", "Description", "mean", "median", "percentile_rank")
Brain_Caudate_TTR_hist <- Brain_Caudate_TTR[, !names(Brain_Caudate_TTR) %in% drops]
hello <- melt(Brain_Caudate_TTR_hist)
hist(hello$value)
