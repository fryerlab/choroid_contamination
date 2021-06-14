# NOTE: I will fix file naming.

## 1. Create a counts matrix 
- The counts matrix will contains all hippocampus samples from the Allen Brain Atlas Aging, Dementia and TBI dataset.
  - © 2017 Allen Institute for Brain Science. Aging, Dementia and TBI. Available from: https://aging.brain-map.org/
- The script **Allen_create_hip_tpm_counts.Rmd** will create a counts table. 3 files are used as for input.
  - rsem_GRCh38.p2.gtf 
  - tbi_data_files.csv
  - DonorInformation.csv
- The script will output two files.
  - hippocampus_tpm_counts.txt
  - hippocampus_donorid_sex.txt
## 2. Find differentially expressed genes between highly choroid contaminated hippocampus samples and clean hippocampus samples.
- Run the script **Allen_DEGs_hip_all_samples.Rmd**.  It will read in 3 files.
  - hippocampus_tpm_counts.txt
  - gene_info_for_counts_file.txt
  - metadata.txt
