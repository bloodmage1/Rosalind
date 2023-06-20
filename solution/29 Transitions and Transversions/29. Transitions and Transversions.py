import os

os.chdir(r"C:\Users\user\Desktop")

with open("rosalind_tran_3_dataset.txt") as f:
    a = f.read().strip()

dic = {}

for line in a.split("\n"):
    if line.startswith(">"):
        a = line
        b = ""

    else:
        b += line
    dic[a] = b

ros = []

for k,v in dic.items():
    ros.append(v)

a = ros[0]
b = ros[1]

transition = 0
transversion = 0

for i in range(len(a)):
    if a[i] != b[i]:
        if a[i] == "A" and b[i] =="G":
            transition += 1
        elif a[i] == "G" and b[i] =="A":
            transition += 1
        elif a[i] == "C" and b[i] =="T":
            transition += 1
        elif a[i] == "T" and b[i] =="C":
            transition += 1
        else:
            transversion += 1

print(transition/transversion)
        





