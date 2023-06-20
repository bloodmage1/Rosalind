from itertools import product

import os

os.chdir(r"C:\Users\user\Desktop")


with open("rosalind_kmer.txt") as f:
    a = f.read().strip()

for line in a.split("\n"):
    if line.startswith(">"):
        a= line
        b = ""
    else:
        b += line

    ros = b
    
dna = ["A", "C", "G", "T"]

mer = list(product(dna, repeat = 4))

mer4 = []

for i in mer:
    mer4.append("".join(i))

dic = {}

for i in mer4:
    dic[i] = 0

for i in range(0, len(ros)):
    if ros[i:i+4] in list(dic.keys()):
        dic[ros[i:i+4]] += 1

for i in dic.values():
    print(i, end = " ")
    