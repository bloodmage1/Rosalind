dic = {}

import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_gc.txt") as f:
    for line in f.readlines():
        if line.startswith(">"):
            a = line[1:].strip()
            b = ""
        else:
            b += line.strip()
                
        dic[a] = b          

for i,j in dic.items():
    a = (j.count("G")+ j.count("C"))/ len(j)
    dic[i] = a

for k, v in dic.items():
    if v == max(dic.values()):
        print(k)
print((max(dic.values()))*100)
