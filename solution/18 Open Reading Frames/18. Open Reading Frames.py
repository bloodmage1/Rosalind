ros = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

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

# import os

# os.chdir(r"C:\Users\user\Desktop")

# with open("rosalind_orf.txt") as f:
#     a = f.read().split("\n")
# ros = ""

# for line in a[1:]:
#     ros += line

ros = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

stop_codons = ['TAA', 'TAG', 'TGA']

index = []


# def trans(a):
#     a_reverse = a[::-1]

#     a_reverse1 = a_reverse.replace("A","t")
#     a_reverse2 = a_reverse1.replace("C","g")
#     a_reverse3 = a_reverse2.replace("G","c")
#     a_reverse4 = a_reverse3.replace("T","a")

#     a = a_reverse4.upper()
#     return a
# for i in range(len(ros)):
#     if ros[i:i+3] == "ATG":
#         index.append(i)

# for ind in index:

#     for j in range(ind, len(ros), 3):
#         if ros[j:j+3] in stop_codons:
#             break
#         else:
#             print(table[ros[j:j+3]], end = "")
#     print()
        
# ros = trans(ros)/


for i in range(len(ros)):
    if ros[i:i+3] == "ATG":
        index.append(i)

for ind in index:

    for j in range(ind, len(ros), 3):
        if ros[j:j+3] in stop_codons:
            break
        else:
            print(table[ros[j:j+3]], end = "")
    print()