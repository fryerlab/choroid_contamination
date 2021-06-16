# Widespread choroid plexus contamination in sampling and profiling of brain tissue
*TTR, Ttr* expression in human and mouse data sets

## Abstract
The choroid plexus, a tissue responsible for the production of cerebrospinal fluid, is found predominantly in the lateral and fourth ventricles of the brain. It is a highly vascularized and ciliated tissue made up of epithelial cells and capillary networks surrounded by connective tissue that could potentially result in contamination during routine tissue dissection. 
We used the *TTR, Ttr* gene as a marker to query the gene expression omnibus (GEO) database for transcriptome studies of brain tissue and identified at least some level of likely choroid contamination in many studies which  may have confounded data analysis. We also analyzed the human genotype-tissue expression (GTEx) database and found choroid contamination, with regions in closer proximity to choroid more likely to be impacted such as hippocampus, cervical spinal cord, substantia nigra, hypothalamus, and amygdala. 
We suggest that some studies may warrant a reevaluation with removal of choroid contaminated samples, or where choroid expression is accounted for in the statistical modeling. Additionally, we suggest that a simple RT-qPCR or Western blot for choroid markers would mitigate unintended choroid contamination for any experiment, but particularly for samples intended for more costly omic profiling. 

Here we provide our scripts for the following: 
1) GEO web scraping to identify datasets that may have choroid contamination
2) Allen Brain gene differential expression between likely contaminated samples and samples that likely do not have choroid contamination
3)GTEx gene differential expression between likely contaminated samples and samples that likely do not have choroid contamination

### Parsing GTEx data to find samples with and without TTR expression
- Script: `parse_gtex.py`
1. Subset samples from the GTEx TPM count file:
- Example using liver where one specifies the samples to be subsetted via the config file
```
python scripts/parse_gtex.py --data rna --config GTEx_configs/Liver_config.json --gtex_file data/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_tpm_clean.gct --subset_samples_outfile Liver_counts.tsv
```
GTEx count files are located here: /data/CEM/shared/controlled_access/GTEX/version8/counts/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_tpm.gct.gz

- Instead of providing the samples to be subsetted via the config file, you can also provide a sample via `--sample` or a file with each sample on a row via `--samples_file`

2. For each tissue_counts.tsv, percentile rank (aka bin) the expression for each gene for each sample. Every gene will have a rank expression from 0-100. Zero being no expression, and 100 being the highest expressed genes for that sample. 

3. Subset the counts to get TTR TPM expression and TTR rank expression

4. Violin jitter plots showing rank values of TTR expression for each tissue. 
