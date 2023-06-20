table = {
'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S',
'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'TAT': 'Y', 'TAC': 'Y',
'TGT': 'C', 'TGC': 'C', 'TGG': 'W', 'CTT': 'L', 'CTC': 'L',
'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P',
'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I',
'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T',
'ACA': 'T', 'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K',
'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A',
'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D', 'GAC': 'D',
'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G',
'GGG': 'G'}

stop_codons = ['TAA', 'TAG', 'TGA']

import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_splc.txt") as f:
    ros = f.read().strip()

dic = {}
lis = []

for line in ros.split("\n"):
    if line.startswith(">"):
        a = line
        b = ""
    else:
        b += line
    
    dic[a] = b

for k,v in dic.items():
    lis.append(v)

answer = lis[0]

for i in range(1, len(lis)):
    answer = answer.replace(lis[i],"")

for i in range(0, len(answer),3):
    if answer[i:i+3] in stop_codons:
        break
    else:
        print(table[answer[i:i+3]], end= "")

