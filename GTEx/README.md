## Run the script **GTEx_DEG_all_samples.Rmd** to find differentially expressed genes between clean and contaminated hippocampus samples.  
- 3 input files are required.
  - **Brain_hippocampus** which is the hippocampus counts matrix
  - **GTEx_Analysis_v8_Annotations_SubjectPhenotypesDS.txt** which is the metadata
  - **gencode.v26.GRCh38.genes.gtf** which is the annotation file
- The script will output 2 files.
  - DEG_dirty_vs_clean_FDRq1_Log2FC0.txt
  - DEG_dirty_vs_clean_FDRq0.05_Log2FC1.txt 
