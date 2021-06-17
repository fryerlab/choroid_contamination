# load libraries
library(ggplot2)
library(reshape)
library(scales)

# set working directory
setwd(".")
#setwd(getSrcDirectory()[1])

# read in GEO wed scraping file
rank <- read.csv("title_and_rank_priority.csv")
p <- rank$p.values
BH <- p.adjust(p, method = "BH", n = length(p))
rank$FDR <- BH
rank$priority_FDR <- NA
mouse_rank <- subset(rank, rank$animal == "Mus musculus")
human_rank <- subset(rank, rank$animal == "Homo sapiens")
df <- rank

#-------------------- p.value
df <- df[complete.cases(df$priority),] # remove rows with NA
v1 <- nrow(subset(df, priority == "1"))
v2 <- nrow(subset(df, priority == "2"))
v3 <- nrow(subset(df, priority == "3"))
v4 <- nrow(subset(df, priority == "4"))
v5 <- nrow(subset(df, priority == "5"))
total <- v1 + v2 + v3 + v4 + v5
v1 <- (v1 / total) * 100
v2 <- (v2 / total) * 100
v3 <- (v3 / total) * 100
v4 <- (v4 / total) * 100
v5 <- (v5 / total) * 100

pie_df <- data.frame(Rank = c("1", "2", "3", "4", "5"),
                     value = c(v1, v2, v3, v4, v5))
bp <- ggplot(pie_df, aes(x = "", y = value, fill = Rank)) +
  geom_bar(width = 1, stat = "identity")
pie <- bp + coord_polar("y", start = 0)


blank_theme <- theme_minimal() +
  theme(
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    panel.border = element_blank(),
    panel.grid = element_blank(),
    axis.ticks = element_blank(),
    legend.text = element_text(size = 10),
    plot.title = element_text(size = 10, face = "bold")
  )

pie_df$pos <- c(85, 65, 40, 15, 2)

pdf(
  file = ("GEO_pie_all_pvalue.pdf"),
  width = 3,
  height = 3
)
bp <- ggplot(pie_df, aes(x = "", y = value, fill = Rank)) +
  geom_bar(width = 1, stat = "identity")
pie <- bp + coord_polar("y", start = 0)
pie + geom_text(aes(
  x = "",
  y = pos,
  label = percent(value / 100)
),
size = 3.5,
alpha = 1)  +
  blank_theme +
  theme(axis.text.x = element_blank())  + scale_fill_brewer(palette = "Pastel1")
dev.off()

#-------------------- FDR
df$priority_FDR <- ifelse(df$FDR <= .05, "1",
                          ifelse((df$FDR > .05 & df$FDR < .1),
                                 "2",
                                 ifelse(df$priority == 4, "4",
                                        #        ifelse(df$FDR == "NA", "3",
                                        ifelse(df$priority == 5, "5", "3"))
                          ))

df <- df[complete.cases(df$FDR),] # remove rows with NA
v1 <- nrow(subset(df, priority_FDR == "1"))
v2 <- nrow(subset(df, priority_FDR == "2"))
v3 <- nrow(subset(df, priority_FDR == "3"))
v4 <- nrow(subset(df, priority_FDR == "4"))
v5 <- nrow(subset(df, priority_FDR == "5"))
total <- v1 + v2 + v3 + v4 + v5
v1 <- (v1 / total) * 100
v2 <- (v2 / total) * 100
v3 <- (v3 / total) * 100
v4 <- (v4 / total) * 100
v5 <- (v5 / total) * 100

pie_df <- data.frame(Rank = c("1", "2", "3", "4", "5"),
                     value = c(v1, v2, v3, v4, v5))
bp <- ggplot(pie_df, aes(x = "", y = value, fill = Rank)) +
  geom_bar(width = 1, stat = "identity")
pie <- bp + coord_polar("y", start = 0)

blank_theme <- theme_minimal() +
  theme(
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    panel.border = element_blank(),
    panel.grid = element_blank(),
    axis.ticks = element_blank(),
    legend.text = element_text(size = 10),
    plot.title = element_text(size = 10, face = "bold")
  )

pie_df$pos <- c(85, 75, 50, 15, 2)

pdf(
  file = ("GEO_pie_all_FDR.pdf"),
  width = 3,
  height = 3
)
bp <- ggplot(pie_df, aes(x = "", y = value, fill = Rank)) +
  geom_bar(width = 1, stat = "identity")
pie <- bp + coord_polar("y", start = 0)
pie + geom_text(aes(
  x = "",
  y = pos,
  label = percent(value / 100)
),
size = 3.5,
alpha = 1)  +
  blank_theme +
  theme(axis.text.x = element_blank())  + scale_fill_brewer(palette = "Pastel1")
dev.off()
