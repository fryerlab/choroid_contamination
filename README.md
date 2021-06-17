# Widespread choroid plexus contamination in sampling and profiling of brain tissue
*TTR, Ttr* expression in human and mouse data sets

## Abstract
The choroid plexus, a tissue responsible for the production of cerebrospinal fluid, is found predominantly in the lateral and fourth ventricles of the brain. It is a highly vascularized and ciliated tissue made up of epithelial cells and capillary networks surrounded by connective tissue that could potentially result in contamination during routine tissue dissection. 
We used the *TTR, Ttr* gene as a marker to query the gene expression omnibus (GEO) database for transcriptome studies of brain tissue and identified at least some level of likely choroid contamination in many studies which  may have confounded data analysis. We also analyzed the human genotype-tissue expression (GTEx) database and found choroid contamination, with regions in closer proximity to choroid more likely to be impacted such as hippocampus, cervical spinal cord, substantia nigra, hypothalamus, and amygdala. 
We suggest that some studies may warrant a reevaluation with removal of choroid contaminated samples, or where choroid expression is accounted for in the statistical modeling. Additionally, we suggest that a simple RT-qPCR or Western blot for choroid markers would mitigate unintended choroid contamination for any experiment, but particularly for samples intended for more costly omic profiling. 

## Here we provide our scripts for the following: 
1) GEO web scraping to identify datasets that may have choroid contamination.
2) Allen Brain gene differential expression between likely contaminated samples and samples that likely do not have choroid contamination.
3) GTEx gene differential expression between likely contaminated samples and samples that likely do not have choroid contamination.

## STEP 1: GEO - quantify the scope of potential choroid plexus contamination among human and mouse brain datasets.
within the GEO directory go through the following steps. 
First, unzip any files and folders. 


1. GEO rank category definitions for *TTR* or *Ttr* contamination or lack of contamination among samples within a dataset. One way ANOVA to determine if there are statistially significant differences betwee/among the means for *TTR/Ttr* expression. Datasets will be placed in one of the following scores: 


| Rank priority | Description |
| --- | --- |
| 1 | TTR/Ttr expression almost exclusively between groups|
| 2 | TTR/Ttr  expression moderately between groups |
| 3 | TTR/Ttr  expressed in no clear pattern (catch all)  |
| 4 | TTR/Ttr  expressed highly |
| 5 | TTR/Ttr  expressed lowly |


The following command will take a list of GEO web profile URLs and compute a one way ANOVA and assign the dataset to a rank priority value. 
```
python GEO/geo.py
```

The following command will create a pie chart of results of the GEO web scraping. Additionally, the command will compute a false discovery rate of the p-values from the one way ANOVA tests computed in step 1 above. 
```
Rscript GEO/pieChart.R
```

## STEP 2: Allen Brain Atlas - Gene differential expression between likely contaminated samples and samples that likely do not have choroid contamination.
within the  Allen Brain Atlas directory go through the following steps. 
First, unzip any files and folders. 


1. Download human TPM counts and metadata files.
Got to the Allen Brain Atlas website here: https://aging.brain-map.org/download/index
Download the following files: 
- tbi_data_files.csv
- DonorInformation.csv
- rsem_GRCh38.p2.gtf

save the files in the 02_AllenBrainAtlas directory

```
export RSTUDIO_PANDOC=/Applications/RStudio\ 2.app/Contents/MacOS/pandoc
Rscript -e "rmarkdown::render('Allen_create_hippocampus_counts.Rmd', params=list(args = myarg))"
``` 

2. Plot TTR percentile rank in Allen Brain tissue regions

```
Rscript Allen_TTR_rank.R
``` 

3. Differential expression between likely not contaminated samples and samples that likely do have choroid contamination 
Export RSTUDIO_PANDOC only needs to be run once
```
export RSTUDIO_PANDOC=/Applications/RStudio\ 2.app/Contents/MacOS/pandoc
Rscript -e "rmarkdown::render('Allen_hip_DEGs.Rmd', params=list(args = myarg))"
``` 

## STEP 3: GTEx - Gene differential expression between likely contaminated samples and samples that likely do not have choroid contamination.
within the GTEx directory go through the following steps. 
First, unzip any files and folders. 

GTEx TPM counts and metadata files were downloaded from https://gtexportal.org/home/
Config files for each tissue are provided in the GTEx_config folder. 
TTR percential ranks file is provided. 

1. For each tissue_counts.tsv, percentile rank (aka bin) the expression for each gene for each sample. Every gene will have a rank expression from 0-100. Zero being no expression, and 100 being the highest expressed genes for that sample. Plot a violin jitter showing rank values of TTR expression for each brain tissue. 
```
Rscript GTEx_TTR_rank_violin.R 
```

2. Differential expression between likely not contaminated samples and samples that likely do have choroid contamination 
```
export RSTUDIO_PANDOC=/Applications/RStudio\ 2.app/Contents/MacOS/pandoc
Rscript -e "rmarkdown::render('GTEx_DEG_all_samples.Rmd', params=list(args = myarg))"
```

## Group Members
Name | email | github ID
--- | --- |  ---
Kimberly Olney | olney.kimberly@mayo.edu | @olneykimberly
Kennedi Todd | todd.kennedi@mayo.edu | @kenneditodd
Praveen Pallegar | Pallegar.Praveen@mayo.edu | @pallegar
Melissa A. Wilson | mwilsons@asu.edu | 
John D. Fryer| fryer.john@mayo.edu | 

