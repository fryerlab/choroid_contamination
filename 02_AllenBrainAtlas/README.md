# Allen Brain Atlas
This will provide the steps for the Allen Brain Atlas differentially expressed genes workflow. Unzip the Files.zip folder prior to running the scripts located in the scripts folder. 
Also note that you will need to update the working directory of the R scripts prior to running. 
## 1. Create a counts matrix 
- The counts matrix will contains all hippocampus samples from the Allen Brain Atlas Aging, Dementia and TBI dataset.
  - © 2017 Allen Institute for Brain Science. Aging, Dementia and TBI. Available from: https://aging.brain-map.org/
- The script **Allen_create_hippocampus_counts.Rmd** will create a counts matrix. 
  - 3 files are used as for input.  They came directly from the Aging, Dementia and TBI download page.
    - **rsem_GRCh38.p2.gtf**
    - **tbi_data_files.csv**
    - **DonorInformation.csv**
  - The script will output 2 files.
    - **geneInfo.txt** which contains gene annotation information 
    - **hippocampus_tpm_counts.txt** which contains counts in TPM
    - **hippocampus_metadata.txt** which contains donor metadata for downstream analyses
## 2. Find differentially expressed genes between clean and contaminated hippocampus samples.
- Run the script **Allen_hip_DEGs.Rmd**.  It will read in 3 files.
  - **hippocampus_tpm_counts.txt**
  - **geneInfo.txt**
  - **metadata.txt**
- 2 files will be output.
  - **DEG_dirty_vs_clean_FDRq1_log2FC0.txt** which contains a differentially expressed genes list with the specified cutoffs.
  - **DEG_dirty_vs_clean_FDRq0.05_Log2FC1.txt** whcih contains a differentially expressed genes list with the specified cutoffs. 
## 3. gencode annotation file
- gencode.v22.annotation.gtf will need to be downloaded and added to the Files folder
- https://www.gencodegenes.org/human/release_22.html 
