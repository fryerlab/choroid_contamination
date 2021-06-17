# profile number -> (experimental groups (title), value)
# profile number -> (experimental groups (title), rank)

from bs4 import BeautifulSoup
import csv
import requests
import re
from scipy.stats import f_oneway
import matplotlib.pyplot as plt
import numpy as np

# PARAMETERS
group_1_cutoff = 0.05
group_2_cutoff = 0.1
group_4_bounds = 0.1
group_4_majority = 0.8
group_5_bounds = 0.1
group_5_majority = 0.8

# MAP CHANGE
title_and_value = {}
title_and_rank = {}
title_and_value_p_vals = {}
title_and_rank_p_vals = {}
title_and_value_priority = {}
title_and_rank_priority = {}

# Creating URL_list
with open('geo_values.csv') as csv_file:
	reader = csv.reader(csv_file, delimiter=',')
	vals = list(reader)

for i in range(0, len(vals)):
	vals[i] = str(vals[i]).replace("['",'').replace("']",'')

URL_list = ["https://www.ncbi.nlm.nih.gov/geoprofiles/" + num for num in vals]
#URL_list = ["https://www.ncbi.nlm.nih.gov/geoprofiles/45635549", "https://www.ncbi.nlm.nih.gov/geoprofiles/97812756"]
#URL_list = ["https://www.ncbi.nlm.nih.gov/geoprofiles/97812756"]

# Populating map with rank and value
for URL in URL_list:
	print(URL)
	profile_number = URL.split('/')[-1]
	title_and_value[profile_number] = set()
	title_and_rank[profile_number] = set()

	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	table_URL = "https://www.ncbi.nlm.nih.gov" + soup.find('a', attrs={'href': re.compile("geo/tools/profileGraph")}).get('href')
	page = requests.get(table_URL)
	soup = BeautifulSoup(page.content, 'html.parser')

	for tr in soup.find_all('tr')[2:]:
	    tds = tr.find_all('td')
	    if len(tds) == 4 and (len(str(tds[2])) > 9) and (len(str(tds[3])) > 9):
	    	title = str(tds[1])[4:-5]
	    	val = float(str(tds[2])[4:-5])
	    	rank = int(str(tds[3])[4:-5])
	    	# MAP CHANGE 
	    	title_and_value[profile_number].add((title, val))
	    	title_and_rank[profile_number].add((title, rank))

for URL in title_and_rank:
	example = title_and_rank[URL]
	example_value = title_and_value[URL]

	example = sorted(list(example))
	example_value = sorted(list(example_value))

	temp_dict_rank = {}
	temp_dict_value = {}

	for i in range(0, len(example)):
		sub_example = list(example[i])
		sub_example_value = list(example_value[i])
		group = str(sub_example[0])
		
		if URL == "10280281":
			if "#4" in group or "#5" in group or "#6" in group:
				group = "control"
				sub_example[0] = "control"
			if "#1" in group or "#2" in group or "#3" in group:
				group = "HuD Overexpression"
				sub_example[0] = "HuD overexpression"

		if "Brain area 8/9_8yp_RTT" in group or "Brain area 8/9_6y_RTT" in group:
			sub_example[0] = "Superior Frontal Gyrus_2-4y_RTT"

		if "Cerebellum_naive_ISS55_B" in group or "Cerebellum_naive_ISS56_B" in group:
			sub_example[0] = "inbred short sleep"

		if "Cerebellum_naive_ILS48_B" in group or "Cerebellum_naive_ILS51_B" in group:
			sub_example[0] = "inbred long sleep"
		
		if "Sample" in group:
			head,sep,tail = group.partition(' Sample')
			sub_example[0] = head

		if "USHT" in group:
			head,sep,tail = group.partition(' USHT')
			sub_example[0] = head

		if "(430B)" in group:
			head,sep,tail = group.partition(' (430B)')
			group = head

		if "(technical replicate)" in group:
			head,sep,tail = group.partition(' (technical replicate)')
			group = head
		elif "technical" in group:
			head,sep,tail = group.partition(' technical')
			group = head
		elif ", tech rep " in group:
			head,sep,tail = group.partition(', tech rep ')
			group = head

		if "-MGU74A" in group:
			head,sep,tail = group.partition('-MGU74A')
			group = head

		if "Hippocampus Fluoxetine Group 1" in group:
			group = "Hippocampus Fluoxetine group 1"

		if "_e1_le1" in group:
			head,sep,tail = group.partition('_e1_le1')
			group = head
		elif "_le1" in group:
			head,sep,tail = group.partition('_le1')
			group = head			 

		if "B62E" in group:
			head,sep,tail = group.partition(' B62E')
			sub_example[0] = head

		if "B63E" in group:
			head,sep,tail = group.partition(' B63E')
			sub_example[0] = head

		if "_040702" in group:
			head,sep,tail = group.partition('_040702')
			group = head

		if "_110702" in group:
			head,sep,tail = group.partition('_110702')
			group = head			

		if "_120902" in group:
			head,sep,tail = group.partition('_120902')
			group = head

		if "_130902" in group:
			head,sep,tail = group.partition('_130902')
			group = head

		if "_271102" in group:
			head,sep,tail = group.partition('_271102')
			group = head

		if "_291102" in group:
			head,sep,tail = group.partition('_291102')
			group = head

		if "3405" in group and "brain, hippocampus: " in group:
			head,sep,tail = group.partition('3405')
			sub_example[0] = head + tail

		if "3406" in group and "brain, hippocampus: " in group:
			head,sep,tail = group.partition('3406')
			sub_example[0] = head + tail

		if "3396" in group and "brain, hippocampus: " in group:
			head,sep,tail = group.partition('3396')
			sub_example[0] = head + tail

		if "3363" in group and "brain, hippocampus: " in group:
			head,sep,tail = group.partition('3363')
			sub_example[0] = head + tail

		if "3389" in group and "brain, hippocampus: " in group:
			head,sep,tail = group.partition('3389')
			sub_example[0] = head + tail

		if "3403" in group and "brain, hippocampus: " in group:
			head,sep,tail = group.partition('3403')
			sub_example[0] = head + tail

		if group[-1] == ")":
			head,sep,tail = group.partition(')')
			group = head

		if "bis" in group:
			head,sep,tail = group.partition('bis')
			group = head

		if "Wildtype (untreated) 5176" in group:
			group = "Wild type (untreated) 5176"

		if "11 wk C3H cerebral cortex,rep1" in group:
			group = "11 wk C3H cerebral cortex, rep1"

		if "Sca1cerebellum-knock-in biological rep3" in group:
			group = "Sca1cerebellum-knock-in-biological rep3"

		if group[-1] == "B" and group[-2] == ' ':
			group = group[:-2]

		if " [EGCG, Rot]" in group:
			head,sep,tail = group.partition(' [EGCG, Rot]')
			group = head

		if "G42-CingulateCortex replicate" in group or "G30-CingulateCortex replicate" in group:
			group = "GIN-CingulateCortex replicate1"

		if "YFPH-CingulateCortex-replicate" in group:
			group = "CT6-CingulateCortex-replicate1"

		if "G30-Amygdala-replicate" in group:
			group = "YFPH-Amygdala-replicate1"

		if "G42-Homogenate-CingulateCortex replicate" in group:
			group = "GIN-Homogenate-CingulateCortex replicate1"

		if " (430 2.0 Array" in group:
			head,sep,tail = group.partition(' (430 2.0 Array')
			group = head

		if "MSS-Spa3+moM-1aAv2-s2" in group:
			group = "MSS-Spa-sev-3moM-1aAv2-s2"

		if "MSS-Spa2-2moF-1aAv2-s2" in group:
			group = "MSS-Spa1-2moF-1aAv2-s2"

		if "Av2-s2" in group:
			head,sep,tail = group.partition('Av2-s2')
			group = head[:-1]

		if "KTaj-NSM-" in group:
			group = group[:-1]

		if " of 3" in group:
			head,sep,tail = group.partition(' of 3')
			group = head

		if "Cerebellum_nontransgenic control A61_8 months_replicate 1" in group:
			group = "Cerebellum_nontransgenic control A39_8 months_replicate 4"

		if "Lateral substantia nigra disease-control case MS155 - A chip" in group or "Lateral substantia nigra control case PDC1 - A chip" in group:
			group = "Lateral substantia nigra control case 9 - A chip"

		if "Medial substantia nigra disease-control case MS155 - A chip" in group or "Medial substantia nigra control case PDC1 - A chip" in group:
			group = "Medial substantia nigra control case 9 - A chip"

		if " - A chip" in group:
			head,sep,tail = group.partition(' - A chip')
			group = head
			if group[-1] == ' ':
				group = group[:-1]
		elif " -A chip" in group:
			head,sep,tail = group.partition(' -A chip')
			group = head

		if "1st " in group:
			head,sep,tail = group.partition('1st ')
			if "CA" in group:
				group = tail
			else: sub_example[0] = tail

		if "2nd " in group:
			head,sep,tail = group.partition('2nd ')
			if "CA" in group:
				group = tail
			else: sub_example[0] = tail

		if "3rd " in group:
			head,sep,tail = group.partition('3rd ')
			if "CA" in group:
				group = tail
			else: sub_example[0] = tail

		if group[-2] == "M" and group[-1] == "P":
			group = group[:-2]


		if group[0] == "." and group[1] == ".":
			group = group[2:]
		elif group[0] == ".":
			group = group[1:]

		if (group[0] == "A" or group[0] == "B" or group[0] == "C" or group[0] == "D") and group[1].isdigit() and group[2] == "_":
			sub_example[0] = group[3:]

		if group[0].isdigit() and group[1] == '_':
			group = group[1:]

		if group[-1].isdigit() and group[-2].isdigit() and group[-3].isdigit() and group[-4].isdigit():
			sub_example[0] = group[:-4]
		elif group[-1].isdigit() and group[-2].isdigit() and group[-3].isdigit():
			if group[-4] == ' ' and group[-5] == ' ':
				sub_example[0] = group[:-4]
			else: sub_example[0] = group[:-3]
		elif group[-1].isdigit() and group[-2].isdigit():
			if group[-3] == ' ':
				sub_example[0] = group[:-3]
			else: sub_example[0] = group[:-2]
		else:
			if group[-1].isdigit():
				sub_example[0] = group[:-1]

		if (group[-1] == "T" and group[-2] == "W") or (group[-1] == "O" and group[-2] == "K"):
			sub_example[0] = group[-2:]

		if "Ctrl Pt" in group:
			sub_example[0] = "Ctrl"

		if "Exp pt" in group:
			sub_example[0] = "Exp"

		if "C57BL/6J wild-type mouse brains, NLX treated, 10mins" in group:
			sub_example[0] = "wild-type"

		if "NY1DD Sickle Cell Mouse brains, NLX treated, 10mins" in group:
			sub_example[0] = "Sickle Cell"

		if "brain_DLPFC_bipolar C" in group:
			sub_example[0] = "control"

		if "brain_DLPFC_bipolar B" in group:
			sub_example[0] = "bipolar disorder"

		if "brain_healthy_control_sampleid_jg" in group or "brain_control_sampleid_mr" in group:
			sub_example[0] = "control"

		if "brain_Down_syndrome_sampleid_jg" in group:
			sub_example[0] = "Down syndrome"

		if "CA9" in group or "CA01-103" in group or "CCC103" in group:
			sub_example[0] = "control"

		if "HA9" in group or "HA0" in group:
			sub_example[0] = "HIVE"

		if "DRG0" in group:
			sub_example[0] = "dorsal root ganglion"

		if "NG0" in group:
			sub_example[0] = "nodose root ganglion"

		if "brain_OFC_control C_mr" in group:
			sub_example[0] = "control"

		if "brain_OFC_bipolar B_mr" in group:
			sub_example[0] = "bipolar disorder"

		if "2 month Old" in group:
			sub_example[0] = "2 months"

		if "15 month Old" in group:
			sub_example[0] = "15 months"

		if "Brain_Wild-type_MiceNo" in group:
			sub_example[0] = "wild-type"

		if "Brain_nAChRbeta4SubunitDeficent_MiceNo" in group:
			sub_example[0] = "nAChRbeta4 Subunit Deficient"

		if "WT #" in sub_example[0]:
			sub_example[0] = "WT#"

		if "Brain_C57 Wildtype_affs275" in group:
			sub_example[0] = "wild type"

		if "Brain_Melanotransferrin Knockout_affs275" in group:
			sub_example[0] = "melanotransferrin knockout"

		if "P5.221EA" in group:
			if "_Wildtype" in group:
				sub_example[0] = "wild type"
			elif "_SmoA2 mutant" in group:
				sub_example[0] = "SmoA2 mutant"
		if "P5.SS1NN" in group and "_Smo/Smo mutant" in group:
			sub_example[0] = "SmoA1 (Smo/Smo) mutant"

		if "NM Spinal cord" in group:
			sub_example[0] = "nontransgenic"

		if "WT-SOD1 mouse spinal cord " in group:
			sub_example[0] = "wild type SOD1 transgenic"

		if "G93A-SOD1 mouse spinal cord " in group:
			sub_example[0] = "G93A-SOD1 transgenic"

		if "litter 1, P14 V1 Litter " in group:
			sub_example[0] = "14 d"
		if "litter 1, P28 V1 Litter " in group:
			sub_example[0] = "28 d"
		if "litter 1, P60 V1 Litter " in group:
			sub_example[0] = "60 d"

		if "ALS gray matter" in group:
			if "Sporadic" in group:
				sub_example[0] = "sporadic ALS"
			if "Familial" in group:
				sub_example[0] = "familial ALS"

		if "sham-operated control" in group:
			if "lateral motoneurons (LMN)"in group:
				sub_example[0] = "lateral motoneurons"
			if "medial motoneurons (MMN)" in group:
				sub_example[0] = "medial motoneurons"
			if "intermediolateral column motoneurons (IML)" in group:
				sub_example[0] = "intermediolateral column motoneurons"

		if "brain, " in group and " proxT65H, 430A" in group:
			sub_example[0] = "newborn brain"

		if "embryo, " in group and " proxT65H, 430A" in group:
			sub_example[0] = "13.5 dpc embryo"

		if "Mouse_Brain_ChimpanzeeDiet__Batch_"in group:
			sub_example[0] = "chimpanzee diet"
		if "Mouse_Brain_FastFoodDiet__Batch_" in group:
			sub_example[0] = "human fast food diet"
		if "Mouse_Brain_HumanCafeDiet__Batch_" in group:
			sub_example[0] = "human cafe diet"
		if "Mouse_Brain_PelletDiet__Batch_" in group:
			sub_example[0] = "control"

		if "Semeralul_PFC_Development_Week2_Batch" in group:
			sub_example[0] = "2 wk"
		if "Semeralul_PFC_Development_Week3_Batch" in group:
			sub_example[0] = "3 wk"
		if "Semeralul_PFC_Development_Week4_Batch" in group:
			sub_example[0] = "4 wk"
		if "Semeralul_PFC_Development_Week5_Batch" in group:
			sub_example[0] = "5 wk"
		if "Semeralul_PFC_Development_Week10_Batch" in group:
			sub_example[0] = "10 wk"

		if "Brain_Adult_LPSip_4hr_mouse" in group:
			sub_example[0] = "adult LPS"

		if "Brain_Adult_Salineip_4hr_mouse" in group:
			sub_example[0] = "adult saline"

		if "Brain_Aged_LPSip_4hr_mouse" in group:
			sub_example[0] = "aged LPS"

		if "Brain_Aged_Salineip_4hr_mouse" in group:
			sub_example[0] = "aged saline"

		if "Control brain " in group and " biological rep" in group:
			sub_example[0] = "control"

		if "Untreated HAND brain " in group and " biological rep" in group:
			sub_example[0] = "untreated HAND"

		if "Treated HAND brain " in group and " biological rep" in group:
			sub_example[0] = "treated HAND"

		if "Wildtype saline, technical replicate " in group:
			sub_example[0] = "Wildtype saline, biological replicate "

		if "Wildtype cocaine, technical replicate " in group:
			sub_example[0] = "Wildtype cocaine, biological replicate "

		if "Knockout saline, technical replicate " in group:
			sub_example[0] = "Knockout saline, biological replicate "

		if "Knockout cocaine, technical replicate " in group:
			sub_example[0] = "Knockout cocaine, biological replicate "

		if "NFIa E18KO" in sub_example[0]:
			sub_example[0] = "NFIA E18KO"

		if "NFIa E18KO" in sub_example[0]:
			sub_example[0] = "NFIA E18KO"

		if ".wt.ctrl.rep" in group:
			sub_example[0] = "wild-type control"

		if ".wt.hca.rep" in group:
			sub_example[0] = "wild-type hca"

		if ".ko.ctrl.rep" in group:
			sub_example[0] = "KO control"

		if ".ko.hca.rep" in group:
			sub_example[0] = "KO HCA"

		if "C57 wild type vehicle treatment biological rep" in group:
			sub_example[0] = "C57 wild type vehicle treatment, biological rep"

		if "Caveolin-1 knockout vehicle treatment biological rep" in group:
			sub_example[0] = "Caveolin-1 knockout vehicle treatment, biological rep"

		if "EAE, 1,25(OH)2D2 treated #" in group:
			sub_example[0] = "EAE, 1,25(OH)2D3-treated #"

		if "EAE, placebo treated #" in group:
			sub_example[0] = "EAE, placebo-treated #"

		if "15E8" in group or "DFFC" in group or "F272" in group or "C835" in group or "O7A2" in group or "OAD3" in group or "1338" in group or "B9F2" in group or "D494" in group or "C627" in group or "5D42" in group or "BC91" in group or "BBB4" in group or "BD1Bv1" in group or "2C4C" in group or "75F3" in group or "O8AE" in group or "OE41" in group:
			head,sep,tail = group.partition('_')
			sub_example[0] = head

		if "wild-type rep_" in group and " (CWT" in group:
			sub_example[0] = "wild-type"

		if "ApoD KO rep_" in group and " (CKO" in group:
			sub_example[0] = "ApoD KO"

		if "ApoD transgenic mouse rep_" in group and " (CTG" in group:
			sub_example[0] = "ApoD transgenic"

		if "wild-type+PQ rep_" in group and " (PQWT" in group:
			sub_example[0] = "wild-type Paraquat"

		if "ApoD KO+PQ rep_" in group and " (PQKO" in group:
			sub_example[0] = "ApoD KO Paraquat"

		if "ApoD transgenic mouse+PQ rep_" in group and " (PQTG" in group:
			sub_example[0] = "ApoD transgenic Paraquat"	

		if "XX" in group and "_Paf" in group:
			sub_example[0] = "XX Paf"

		if "XX" in group and "_InX" in group:
			sub_example[0] = "XX InX"

		if "mutant_ANT_PDE_" in group:
			sub_example[0] = "mutant ANT PDE"

		if "WT_ANT_PDE_" in group:
			sub_example[0] = "WT ANT PDE"


		if "NH" in group and group[-1] == "h":
			sub_example[0] = "naive hippocampus"

		if "CS" in group and group[-1] == "h":
			sub_example[0] = "cond hippocampus"

		if "FC" in group and group[-1] == "h":
			sub_example[0] = "cond footshock hippocampus"

		if "NH" in group and group[-1] == "A":
			sub_example[0] = "naive amygdala"

		if "CS" in group and group[-1] == "A":
			sub_example[0] = "cond amygdala"

		if "FC" in group and group[-1] == "A":
			sub_example[0] = "cond footshock amygdala"

		if "XX" in group and "-M" in group:
			sub_example[0] = "XX muscle"

		if "XmO" in group and "-M" in group:
			sub_example[0] = "XmO muscle"

		if "XpO" in group and "-M" in group:
			sub_example[0] = "XpO muscle"

		if "XX" in group and "-L" in group:
			sub_example[0] = "XX liver"

		if "XmO" in group and "-L" in group:
			sub_example[0] = "XmO liver"

		if "XpO" in group and "-L" in group:
			sub_example[0] = "XpO liver"

		if "XX" in group and "-K" in group:
			sub_example[0] = "XX kidney"

		if "XmO" in group and "-K" in group:
			sub_example[0] = "XmO kidney"

		if "XpO" in group and "-K" in group:
			sub_example[0] = "XpO kidney"

		if "XX" in group and "-B" in group:
			sub_example[0] = "XX brain"

		if "XmO" in group and "-B" in group:
			sub_example[0] = "XmO brain"

		if "XpO" in group and "-B" in group:
			sub_example[0] = "XpO brain"

		if "Chronic active plaque " in sub_example[0] and " (CAP" in sub_example[0]:
			sub_example[0] = "chronic active plaque"

		if "Chronic plaque " in sub_example[0] and " (CP" in sub_example[0]:
			sub_example[0] = "chronic plaque"

		if "Braak I-II, APOE e4- temporal cortex astrocytes" in group:
			sub_example[0] = "Braak I-II, APOE e4- sample"

		if "Braak I-II, APOE e4+ temporal cortex astrocytes" in group:
			sub_example[0] = "Braak I-II, APOE e4+ sample"

		if "Braak III-IV, APOE e4- temporal cortex astrocytes" in group:
			sub_example[0] = "Braak III-IV, APOE e4- sample"

		if "Braak III-IV, APOE e4+ temporal cortex astrocytes" in group:
			sub_example[0] = "Braak III-IV, APOE e4+ sample"

		if "Braak V-VI, APOE e4+ temporal cortex astrocytes" in group:
			sub_example[0] = "Braak V-VI, APOE e4+ sample"

		if " wild-type after nicotine-induced seizures" in group:
			sub_example[0] = "wild-type nicotine"

		if " wild-type untreated" in group or " wilt-type untreated" in group:
			sub_example[0] = "wild-type untreated"

		if " +/T after nicotine-induced seizures" in group:
			sub_example[0] = "+/T after nicotine-induced seizures"

		if " +/T untreated" in group:
			sub_example[0] = "+/T untreated"

		if " b4-/- after nicotine-induced seizures" in group:
			sub_example[0] = "b4-/- after nicotine-induced seizures"

		if " b4-/- untreated" in group or " b4-/- untraeted" in group:
			sub_example[0] = "b4-/- untreated"

		if "A Normal-frontal" in group:
			sub_example[0] = "A Normal-frontal"

		if "C Normal-hippocampus" in group:
			sub_example[0] = "C Normal-hippocampus"

		if "B Normal-cerebellum" in group or "B Normal-cerebelum" in group:
			sub_example[0] = "B Normal-cerebellum"

		if "A Progranulin-frontal" in group:
			sub_example[0] = "A Progranulin-frontal"

		if "C Progranulin-hippocampus" in group:
			sub_example[0] = "C Progranulin-hippocampus"

		if "B Progranulin-cerebellum" in group:
			sub_example[0] = "B Progranulin-cerebellum"

		if "A Sporadic-frontal" in group:
			sub_example[0] = "A Sporadic-frontal"

		if "C Sporadic-hippocampus" in group:
			sub_example[0] = "C Sporadic-hippocampus"

		if "B Sporadic-cerebellum" in group:
			sub_example[0] = "B Sporadic-cerebellum"

		if "brain, Entorhinal Cortex: " in group and " normal" in group:
			sub_example[0] = "normal"

		if "brain, Entorhinal Cortex: " in group and " tangle" in group:
			sub_example[0] = "tangle"

		if "JMR-MurNaive-" in group:
			sub_example[0] = "JMR-MurNaive-"

		if "JMR-MurSham4h-" in group:
			sub_example[0] = "JMR-MurSham4h-"

		if "JMR-MurSham8h-" in group:
			sub_example[0] = "JMR-MurSham8h-"

		if "JMR-MurSham24h-" in group:
			sub_example[0] = "JMR-MurSham24h-"

		if "JMR-MurSham72h-" in group:
			sub_example[0] = "JMR-MurSham72h-"

		if "JMR-MurInj4h-" in group:
			sub_example[0] = "JMR-MurInj4h-"

		if "JMR-MurInj8h-" in group:
			sub_example[0] = "JMR-MurInj8h-"

		if "JMR-MurInj24h-" in group:
			sub_example[0] = "JMR-MurInj24h-"

		if "JMR-MurInj72h-" in group:
			sub_example[0] = "JMR-MurInj72h-"


		updated_group = sub_example[0]
		if updated_group[-1] == ' ' and updated_group[-2] == ' ':
			sub_example[0] = updated_group[:-2]
		elif updated_group[-1] == ' ':
			sub_example[0] = updated_group[:-1]

		if sub_example[0] in temp_dict_rank:
			temp_dict_rank[sub_example[0]].append(sub_example[1])
		else:
			temp_dict_rank[sub_example[0]] = []
			temp_dict_rank[sub_example[0]].append((sub_example[1]))
		example[i] = sub_example

		if sub_example[0] in temp_dict_value:
			temp_dict_value[sub_example[0]].append(sub_example_value[1])
		else:
			temp_dict_value[sub_example[0]] = []
			temp_dict_value[sub_example[0]].append((sub_example_value[1]))
		example_value[i] = sub_example

	F_rank, p_rank = f_oneway(*list(temp_dict_rank.values()))
	F_value, p_value = f_oneway(*list(temp_dict_value.values()))

	title_and_rank_p_vals[URL] = p_rank
	title_and_value_p_vals[URL] = p_value

	value_nums = sum(list(temp_dict_value.values()),[])
	rank_nums = sum(list(temp_dict_rank.values()),[])

	#min-max noramlizing values
	value_nums = [((x - min(value_nums)) / (max(value_nums) - min(value_nums))) for x in value_nums]

	# filling priority for value
	if (not np.isnan(p_value)) and p_value<group_1_cutoff:
		title_and_value_priority[URL] = 1
	elif (not np.isnan(p_value)) and p_value >= group_1_cutoff and p_value < group_2_cutoff:
		title_and_value_priority[URL] = 2
	elif sum(1 for i in value_nums if i > (0.9)) > group_4_majority * len(value_nums):
		title_and_value_priority[URL] = 4
	elif sum(1 for i in value_nums if i < (0.10)) > group_5_majority * len(value_nums):
		title_and_value_priority[URL] = 5
	# elif sum(1 for i in value_nums if i > (max(max(temp_dict_value.values())) - group_4_bounds * max(max(temp_dict_value.values())))) > group_4_majority * len(value_nums):
	# 	title_and_value_priority[URL] = 4
	# elif sum(1 for i in value_nums if i < (min(min(temp_dict_value.values())) + group_5_bounds * min(min(temp_dict_value.values())))) > group_5_majority * len(value_nums):
	# 	title_and_value_priority[URL] = 5
	else: title_and_value_priority[URL] = 3

	#filling priority for rank
	if (not np.isnan(p_rank)) and p_rank<group_1_cutoff:
		title_and_rank_priority[URL] = 1
	elif (not np.isnan(p_rank)) and p_rank >= group_1_cutoff and p_rank < group_2_cutoff:
		title_and_rank_priority[URL] = 2
	elif sum(1 for i in rank_nums if i > (90)) > group_4_majority * len(rank_nums):
		title_and_rank_priority[URL] = 4
	elif sum(1 for i in rank_nums if i < (10)) > group_5_majority * len(rank_nums):
		title_and_rank_priority[URL] = 5
	# elif sum(1 for i in rank_nums if i > (max(max(temp_dict_rank.values())) - group_4_bounds * max(max(temp_dict_rank.values())))) > group_4_majority * len(rank_nums):
	# 	title_and_rank_priority[URL] = 4
	# elif sum(1 for i in rank_nums if i < (min(min(temp_dict_rank.values())) + group_5_bounds * min(min(temp_dict_rank.values())))) > group_5_majority * len(rank_nums):
	# 	title_and_rank_priority[URL] = 5
	else: title_and_rank_priority[URL] = 3

with open('title_and_value_p_vals.csv', 'w') as f:
    w = csv.DictWriter(f, title_and_value_p_vals.keys())
    w.writeheader()
    w.writerow(title_and_value_p_vals)

with open('title_and_value_priority.csv', 'w') as f:
    w = csv.DictWriter(f, title_and_value_priority.keys())
    w.writeheader()
    w.writerow(title_and_value_priority)

with open('title_and_rank_p_vals.csv', 'w') as f:
    w = csv.DictWriter(f, title_and_rank_p_vals.keys())
    w.writeheader()
    w.writerow(title_and_rank_p_vals)

with open('title_and_rank_priority.csv', 'w') as f:
    w = csv.DictWriter(f, title_and_rank_priority.keys())
    w.writeheader()
    w.writerow(title_and_rank_priority)




 	