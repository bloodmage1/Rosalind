# ros = """>Rosalind_0498
# AAATAAA
# >Rosalind_2391
# AAATTTT
# >Rosalind_2323
# TTTTCCC
# >Rosalind_0442
# AAATCCC
# >Rosalind_5013
# GGGTGGG"""

import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_grph.txt") as f:
    ros = f.read()

dic = {}

for line in ros.split("\n"):
    if line.startswith(">"):
        a = line[1:].strip()
        b= ""
    else:
        b += line.strip()

    dic[a] = b

for i in range(len(dic.values())):
    for j in range(i+1, len(dic.values())):
        if list(dic.values())[i][-3:] == list(dic.values())[j][:3]:
            print(list(dic.keys())[i], list(dic.keys())[j])
        if list(dic.values())[i][:3] == list(dic.values())[j][-3:]:
            print(list(dic.keys())[j], list(dic.keys())[i])