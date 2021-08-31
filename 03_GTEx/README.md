# GTEx
- Download **GTEx_analyses.zip** project folder
- Within this project folder there are four subfolders
  1. Scripts
  - There are four R Markdown files.  Three scripts classifies choroid contaimination based on TTR expression (all samples, males, females).  The fourth script classifies choroid contaimination based on FOLR1 expression in all samples.
  2. Files
  - This folder contains the iput files (counts, metadata, annotation) for all scripts.
  3. DEGs
  - Contains differentially expressed genes list based on varying cutoffs.
  - An excel version of the differentially expressed genes (FDRq < 0.05, LFC = 1) between likely choroid contaminated and likely not contaminated based on TTR expression in all GTEx samples is also in this GitHub folder.  This file is called **DEGs_TTR_dirty_vs_clean_FDRq0.05_Log2FC1.excel**.
  4. Figures
  - This contains all figure output from the scripts.
