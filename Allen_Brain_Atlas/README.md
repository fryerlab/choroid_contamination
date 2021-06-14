# NOTE: I will fix file naming.

## 1. Create a counts matrix 
- The counts matrix will contains all hippocampus samples from the Allen Brain Atlas Aging, Dementia and TBI dataset.
  - © 2017 Allen Institute for Brain Science. Aging, Dementia and TBI. Available from: https://aging.brain-map.org/
- The script **Allen_create_hippocampus_counts.Rmd** will create a counts table. 
  - 3 files are used as for input.  They came directly from the Aging, Dementia and TBI download page.
    - **rsem_GRCh38.p2.gtf**
    - **tbi_data_files.csv**
    - **DonorInformation.csv**
  - The script will output 2 files.
    - **geneInfo.txt** which contains gene annotation information 
    - **hippocampus_tpm_counts.txt** which contains counts in TPM
    - **hippocampus_metadata.txt** which contains donor metadata for downstream analyses
## 2. Find differentially expressed genes between highly choroid contaminated hippocampus samples and clean hippocampus samples.
- Run the script **Allen_DEGs_hip_all_samples.Rmd**.  It will read in 3 files.
  - hippocampus_tpm_counts.txt
  - gene_info_for_counts_file.txt
  - metadata.txt
-  2 files will be output
  - DEG_dirty_vs_clean_FDRq1_log2FC0.txt which contains a differentially expressed genes list with the specified cutoffs.
  - DEG_dirty_vs_clean_FDRq0.05_Log2FC1.txt whcih contains a differentially expressed genes list with the specified cutoffs. 
